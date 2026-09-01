#!/usr/bin/env python3
"""Measure the critical query portfolio with Google Search Console.

This is a first-party performance measurement, not a live rank scraper. It writes
credential-free CSV/JSON artifacts and never stores OAuth values in the repo.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

SITE = "https://www.atapamukcu.com/"
COUNTRY = "tur"
DEVICES = ("MOBILE", "DESKTOP")
CRITICAL_COUNT = 25
ROOT = Path(__file__).resolve().parents[2]
OPS = ROOT / "seo-ops"
TOKEN_PATH = Path(os.environ.get("HERMES_GOOGLE_TOKEN", Path.home() / ".hermes/google_token.json"))
CLIENT_PATH = Path(os.environ.get("HERMES_GOOGLE_CLIENT", Path.home() / ".hermes/google_client_secret.json"))


def request_json(url: str, *, token: str | None = None, body: dict | None = None) -> dict:
    headers = {"User-Agent": "atapamukcu-seo-ops/1.0"}
    data = None
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=45) as response:
        return json.load(response)


def access_token() -> str:
    token = json.loads(TOKEN_PATH.read_text())
    now = dt.datetime.now(dt.timezone.utc).timestamp()
    if token.get("expires_at") and float(token["expires_at"]) > now + 300:
        return token["token"]
    client_raw = json.loads(CLIENT_PATH.read_text())
    client = client_raw.get("installed") or client_raw.get("web")
    refresh_token = token.get("refresh_token")
    if not refresh_token:
        raise RuntimeError("Google refresh token missing")
    payload = urllib.parse.urlencode({
        "client_id": client["client_id"],
        "client_secret": client["client_secret"],
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req, timeout=45) as response:
        refreshed = json.load(response)
    token["token"] = refreshed["access_token"]
    token["expires_in"] = refreshed.get("expires_in", 3600)
    token["expires_at"] = now + int(token["expires_in"])
    TOKEN_PATH.write_text(json.dumps(token, indent=2))
    TOKEN_PATH.chmod(0o600)
    return token["token"]


def critical_queries() -> list[dict[str, str]]:
    with (OPS / "query-portfolio.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    active = [(index, row) for index, row in enumerate(rows) if row["status"] == "active"]
    active.sort(key=lambda item: (
        0 if item[1]["priority"] == "P0" else 1 if item[1]["priority"] == "P1" else 2,
        -int(item[1]["business_value"]),
        item[0],
    ))
    return [row for _, row in active[:CRITICAL_COUNT]]


def periods(as_of: dt.date) -> list[dict[str, str]]:
    # Search Console final data normally trails by roughly three days.
    current_end = as_of - dt.timedelta(days=3)
    current_start = current_end - dt.timedelta(days=27)
    previous_end = current_start - dt.timedelta(days=1)
    previous_start = previous_end - dt.timedelta(days=27)
    return [
        {"label": "previous_28d", "start": str(previous_start), "end": str(previous_end)},
        {"label": "current_28d", "start": str(current_start), "end": str(current_end)},
    ]


def fetch_rows(token: str, period: dict[str, str]) -> list[dict]:
    site = urllib.parse.quote(SITE, safe="")
    url = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{site}/searchAnalytics/query"
    output: list[dict] = []
    start_row = 0
    while True:
        response = request_json(url, token=token, body={
            "startDate": period["start"],
            "endDate": period["end"],
            "dimensions": ["query", "page", "country", "device"],
            "dimensionFilterGroups": [{"filters": [{
                "dimension": "country", "operator": "equals", "expression": COUNTRY,
            }]}],
            "type": "web",
            "dataState": "final",
            "rowLimit": 25000,
            "startRow": start_row,
        })
        batch = response.get("rows", [])
        output.extend(batch)
        if len(batch) < 25000:
            break
        start_row += len(batch)
    return output


def normalize(value: str) -> str:
    return " ".join(value.casefold().split())


def summarize(raw_rows: list[dict], portfolio: list[dict[str, str]], period: dict[str, str]) -> list[dict]:
    wanted = {normalize(row["query"]): row for row in portfolio}
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in raw_rows:
        query, page, country, device = row["keys"]
        key = normalize(query)
        if key in wanted and country == COUNTRY and device in DEVICES:
            grouped[(key, device)].append(row)

    output = []
    for portfolio_row in portfolio:
        key = normalize(portfolio_row["query"])
        for device in DEVICES:
            rows = grouped.get((key, device), [])
            impressions = sum(float(row.get("impressions", 0)) for row in rows)
            clicks = sum(float(row.get("clicks", 0)) for row in rows)
            if impressions:
                position = sum(float(row["position"]) * float(row["impressions"]) for row in rows) / impressions
                selected = max(rows, key=lambda row: (float(row["impressions"]), float(row["clicks"])))
                selected_url = selected["keys"][1]
                status = "OBSERVED"
                ctr = clicks / impressions
            else:
                position = ctr = None
                selected_url = ""
                status = "UNKNOWN"
            output.append({
                "period": period["label"],
                "start_date": period["start"],
                "end_date": period["end"],
                "query": portfolio_row["query"],
                "target_canonical": portfolio_row["target_canonical"],
                "country": "TUR",
                "device": device.lower(),
                "status": status,
                "gsc_average_position": "" if position is None else f"{position:.2f}",
                "google_selected_url": selected_url,
                "canonical_match": "UNKNOWN" if not selected_url else str(selected_url.rstrip("/") == portfolio_row["target_canonical"].rstrip("/")).lower(),
                "clicks": "" if position is None else f"{clicks:.0f}",
                "impressions": "" if position is None else f"{impressions:.0f}",
                "ctr": "" if ctr is None else f"{ctr:.6f}",
                "top20": "UNKNOWN" if position is None else str(position <= 20).lower(),
                "top10": "UNKNOWN" if position is None else str(position <= 10).lower(),
                "top3": "UNKNOWN" if position is None else str(position <= 3).lower(),
            })
    return output


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--as-of", type=dt.date.fromisoformat, default=dt.date.today())
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    portfolio = critical_queries()
    date_periods = periods(args.as_of)
    token = access_token()
    all_rows = []
    raw_counts = {}
    for period in date_periods:
        raw = fetch_rows(token, period)
        raw_counts[period["label"]] = len(raw)
        all_rows.extend(summarize(raw, portfolio, period))

    coverage_by_period_device = {}
    for period in date_periods:
        coverage_by_period_device[period["label"]] = {}
        for device in ("mobile", "desktop"):
            scope = [r for r in all_rows if r["period"] == period["label"] and r["device"] == device]
            observed = [r for r in scope if r["status"] == "OBSERVED"]
            top3 = [r for r in observed if r["top3"] == "true"]
            coverage_by_period_device[period["label"]][device] = {
                "portfolio_queries": len(scope),
                "observed_queries": len(observed),
                "unknown_queries": len(scope) - len(observed),
                "top3_queries": len(top3),
                "top3_coverage_observed": None if not observed else round(len(top3) / len(observed), 6),
                "top3_coverage_status": "UNKNOWN" if not observed else "CALCULATED",
            }
    current_mobile = coverage_by_period_device["current_28d"]["mobile"]
    report = {
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "site": SITE,
        "measurement_type": "GSC first-party web performance, not a live universal rank",
        "critical_query_count": len(portfolio),
        "periods": date_periods,
        "raw_api_row_counts": raw_counts,
        "coverage_by_period_device": coverage_by_period_device,
        "primary_kpi": current_mobile,
        "limitations": [
            "GSC average position is an impression-weighted historical metric, not a personalized or live rank.",
            "Low-volume/anonymized queries may be omitted by GSC; absent rows remain UNKNOWN, not zero.",
            "The primary KPI uses the portfolio-assigned mobile device; desktop is retained as an auxiliary split.",
            "A single period does not establish a durable gain; use consecutive measurements and period trends.",
        ],
    }
    if args.write:
        write_csv(OPS / "rank-baseline.csv", all_rows)
        (OPS / "rank-baseline-summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, ensure_ascii=False))
        sys.exit(1)
