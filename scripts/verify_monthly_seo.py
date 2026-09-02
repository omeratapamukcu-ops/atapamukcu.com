#!/usr/bin/env python3
"""Regression checks for the August 2026 monthly SEO implementation."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_DATE = "2026-08-05"
errors: list[str] = []


def require(path: str, *needles: str) -> str:
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            errors.append(f"{path}: missing {needle!r}")
    return text


def require_schema_date_not_before(path: str, text: str, minimum: str) -> None:
    match = re.search(r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})"', text)
    try:
        if not match or date.fromisoformat(match.group(1)) < date.fromisoformat(minimum):
            errors.append(f"{path}: dateModified predates {minimum}: {match.group(1) if match else None!r}")
    except ValueError:
        errors.append(f"{path}: invalid dateModified {match.group(1) if match else None!r}")


analytics = require(
    "js/script.js",
    "whatsapp_click",
    "phone_click",
    "email_click",
    "appointment_start",
    "appointment_complete",
    "seans_degerlendirme_cta_click",
    "appointment:complete",
    "verified_success",
)
for forbidden in ("link_url", "link_text", "form_content", "health_data"):
    if forbidden in analytics:
        errors.append(f"js/script.js: privacy-sensitive parameter present: {forbidden}")

general = require(
    "genel-kaygi.html",
    "Genel Kaygı Nedir? Sürekli Endişe Döngüsü",
    "Genel kaygı; tek bir konuya bağlı kalmadan",
    "tanı koyma veya kişisel tedavi planı yerine geçmez",
    'href="/kaygi-dongusu"',
    'href="/antalya-kaygi-psikolog"',
)
exposure = require(
    "maruz-birakma-terapisi.html",
    "Maruz Bırakma Terapisi Nedir?",
    "diğer adıyla maruz kalma terapisi",
    "Maruz kalma terapisi nasıl işler?",
    "kendi başına yoğun maruz bırakma uygulama talimatı değildir",
    "https://doi.org/10.1016/j.brat.2014.04.006",
    'href="/okb"',
    'href="/sosyal-kaygi"',
)
local = require(
    "antalya-okb-psikolog.html",
    "Antalya’da OKB Döngüsüyle Çalışma",
)
about = require(
    "hakkimda.html",
    'href="/antalya-kaygi-psikolog"',
    'href="/antalya-okb-psikolog"',
    'href="/antalya-sosyal-kaygi-psikolog"',
)

for path, text in (
    ("genel-kaygi.html", general),
    ("maruz-birakma-terapisi.html", exposure),
    ("antalya-okb-psikolog.html", local),
):
    require_schema_date_not_before(path, text, EXPECTED_DATE)
    canonicals = re.findall(r'<link rel="canonical" href="([^"]+)"', text)
    if len(canonicals) != 1:
        errors.append(f"{path}: expected one canonical, found {len(canonicals)}")

context = json.loads((ROOT / "ai-context.json").read_text(encoding="utf-8"))
try:
    if date.fromisoformat(context.get("dateModified", "")) < date.fromisoformat(EXPECTED_DATE):
        errors.append(f"ai-context.json: dateModified predates {EXPECTED_DATE}: {context.get('dateModified')!r}")
except ValueError:
    errors.append(f"ai-context.json: invalid dateModified {context.get('dateModified')!r}")

ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap = ET.parse(ROOT / "sitemap.xml").getroot()
expected_urls = {
    "https://www.atapamukcu.com/genel-kaygi",
    "https://www.atapamukcu.com/maruz-birakma-terapisi",
    "https://www.atapamukcu.com/antalya-okb-psikolog",
    "https://www.atapamukcu.com/hakkimda",
}
seen: dict[str, str | None] = {}
for node in sitemap.findall("s:url", ns):
    loc = node.findtext("s:loc", namespaces=ns)
    if loc in expected_urls:
        seen[loc] = node.findtext("s:lastmod", namespaces=ns)
for url in expected_urls:
    try:
        if date.fromisoformat(seen.get(url) or "") < date.fromisoformat(EXPECTED_DATE):
            errors.append(f"sitemap.xml: {url} lastmod predates {EXPECTED_DATE}: {seen.get(url)!r}")
    except ValueError:
        errors.append(f"sitemap.xml: {url} has invalid lastmod {seen.get(url)!r}")

for path in ("llms.txt", "llms-full.txt"):
    text = require(path, "Son güncelleme:")
    match = re.search(r"Son güncelleme:\s*(\d{4}-\d{2}-\d{2})", text)
    try:
        if not match or date.fromisoformat(match.group(1)) < date.fromisoformat(EXPECTED_DATE):
            errors.append(f"{path}: update date predates {EXPECTED_DATE}: {match.group(1) if match else None!r}")
    except ValueError:
        errors.append(f"{path}: invalid update date {match.group(1) if match else None!r}")

if errors:
    print("FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("monthly_seo=PASS")
print("analytics_events=6 privacy_guard=PASS")
print("target_pages=3 internal_links=PASS metadata_dates=PASS")
