#!/usr/bin/env python3
"""Create a reproducible, site-wide quality inventory for atapamukcu.com."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from html import unescape
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "seo-ops" / "research"
CSV_PATH = OUT_DIR / "sitewide-quality-inventory.csv"
MD_PATH = OUT_DIR / "sitewide-quality-inventory.md"
SITE = "https://www.atapamukcu.com"
EXCLUDED_DIRS = {"node_modules", ".git", ".vercel", ".hermes", ".tmp-editorial"}

TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.I | re.S)
LINK_RE = re.compile(r"<a\b[^>]*href=[\"']([^\"']+)[\"']", re.I)
SCHEMA_RE = re.compile(r"<script\b[^>]*type=[\"']application/ld\+json[\"'][^>]*>(.*?)</script>", re.I | re.S)


def text_of(raw: str) -> str:
    raw = SCRIPT_STYLE_RE.sub(" ", raw)
    raw = TAG_RE.sub(" ", raw)
    return re.sub(r"\s+", " ", unescape(raw)).strip()


def first(raw: str, pattern: str) -> str:
    m = re.search(pattern, raw, re.I | re.S)
    return text_of(m.group(1)) if m else ""


def schema_types(raw: str) -> list[str]:
    found: list[str] = []
    for block in SCHEMA_RE.findall(raw):
        try:
            data = json.loads(unescape(block))
        except Exception:
            continue
        stack = [data]
        while stack:
            item = stack.pop()
            if isinstance(item, dict):
                value = item.get("@type")
                if isinstance(value, str):
                    found.append(value)
                elif isinstance(value, list):
                    found.extend(str(v) for v in value)
                stack.extend(item.values())
            elif isinstance(item, list):
                stack.extend(item)
    return sorted(set(found))


def classify(path: Path, schemas: list[str]) -> str:
    name = path.stem
    if name == "404":
        return "utility"
    if name == "index":
        return "home"
    if "Service" in schemas or name in {"online-psikolog", "antalya-psikolog"}:
        return "service"
    if name in {"hakkimda", "gizlilik", "site-haritasi", "araclar", "online-terapi-nasil-isler", "antalya-online-psikolog"}:
        return "trust-or-navigation"
    if "araclar" in path.parts:
        return "interactive-tool"
    if "uygulamalar" in path.parts:
        return "guided-practice"
    if "ogrenme-yollari" in path.parts:
        return "learning-path"
    return "clinical-guide"


def internal_target(href: str, source_route: str) -> str | None:
    if href.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None
    absolute = urljoin(SITE + source_route, href)
    parsed = urlparse(absolute)
    if parsed.netloc not in {"atapamukcu.com", "www.atapamukcu.com"}:
        return None
    path = parsed.path or "/"
    if path.endswith(".html"):
        path = path[:-5]
    return path.rstrip("/") or "/"


def page_route(path: Path) -> str:
    rel = path.relative_to(ROOT).with_suffix("")
    return "/" if rel.as_posix() == "index" else "/" + rel.as_posix()


def main() -> int:
    files = sorted(
        p for p in ROOT.rglob("*.html")
        if not any(part in EXCLUDED_DIRS for part in p.relative_to(ROOT).parts)
    )
    routes = {page_route(p) for p in files}
    inbound = Counter()
    links_by_page: dict[str, list[str]] = {}
    for path in files:
        route = page_route(path)
        raw = path.read_text(encoding="utf-8")
        targets = [t for h in LINK_RE.findall(raw) if (t := internal_target(h, route))]
        links_by_page[route] = targets
        inbound.update(t for t in set(targets) if t != route)

    rows = []
    title_counts = Counter()
    desc_counts = Counter()
    for path in files:
        raw = path.read_text(encoding="utf-8")
        route = page_route(path)
        title = first(raw, r"<title[^>]*>(.*?)</title>")
        desc_match = re.search(r"<meta\b[^>]*name=[\"']description[\"'][^>]*content=[\"']([^\"']*)", raw, re.I)
        if not desc_match:
            desc_match = re.search(r"<meta\b[^>]*content=[\"']([^\"']*)[\"'][^>]*name=[\"']description", raw, re.I)
        desc = unescape(desc_match.group(1)).strip() if desc_match else ""
        h1s = re.findall(r"<h1\b[^>]*>(.*?)</h1>", raw, re.I | re.S)
        canonical = re.search(r"<link\b[^>]*rel=[\"']canonical[\"'][^>]*href=[\"']([^\"']+)", raw, re.I)
        schemas = schema_types(raw)
        body = first(raw, r"<main\b[^>]*>(.*?)</main>") or text_of(raw)
        words = len(re.findall(r"\b[\wÇĞİÖŞÜçğıöşü'-]+\b", body, re.U))
        external = [h for h in LINK_RE.findall(raw) if urlparse(h).netloc and urlparse(h).netloc not in {"atapamukcu.com", "www.atapamukcu.com"}]
        has_sources = bool(re.search(r"Kaynak(?:lar|ça)|İleri okuma|article-sources", raw, re.I)) and len(external) > 0
        has_author = bool(re.search(r"rel=[\"']author[\"']|author-box|Psikolog Ata Pamukçu", raw, re.I))
        has_visible_date = bool(re.search(r"<time\b[^>]*datetime=|güncellendi|Güncellenme|İlk yayın:|İçerik ve kaynak güncellemesi:", raw, re.I))
        has_date_modified = bool(re.search(r'"dateModified"\s*:', raw))
        has_breadcrumb = bool(re.search(r"aria-label=[\"']Sayfa yolu[\"']|BreadcrumbList", raw, re.I))
        kind = classify(path, schemas)
        is_editorial = kind in {"clinical-guide", "guided-practice", "learning-path"}
        thin_threshold = 700 if kind == "clinical-guide" else 350
        checks = {
            "title": bool(title),
            "description": bool(desc),
            "one_h1": len(h1s) == 1,
            "canonical": bool(canonical),
            "schema": bool(schemas),
            "breadcrumb": has_breadcrumb or kind in {"home", "utility"},
            "author": has_author or not is_editorial,
            "visible_date": has_visible_date or not is_editorial,
            "date_modified": has_date_modified or not is_editorial,
            "sources": has_sources or not is_editorial,
            "depth": words >= thin_threshold or kind in {"interactive-tool", "utility", "home"},
            "inbound": inbound[route] > 0 or route == "/",
        }
        score = round(100 * sum(checks.values()) / len(checks))
        rows.append({
            "route": route,
            "file": path.relative_to(ROOT).as_posix(),
            "type": kind,
            "words": words,
            "inbound_pages": inbound[route],
            "internal_links": len(set(links_by_page[route])),
            "external_links": len(set(external)),
            "title": title,
            "description": desc,
            "h1_count": len(h1s),
            "canonical": canonical.group(1) if canonical else "",
            "schema_types": ";".join(schemas),
            "has_author": int(has_author),
            "has_visible_date": int(has_visible_date),
            "has_date_modified": int(has_date_modified),
            "has_sources": int(has_sources),
            "quality_score": score,
            "failed_checks": ";".join(k for k, ok in checks.items() if not ok),
        })
        title_counts[title] += 1
        desc_counts[desc] += 1

    for row in rows:
        row["duplicate_title"] = int(bool(row["title"]) and title_counts[row["title"]] > 1)
        row["duplicate_description"] = int(bool(row["description"]) and desc_counts[row["description"]] > 1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    editorial = [r for r in rows if r["type"] in {"clinical-guide", "guided-practice", "learning-path"}]
    low = sorted(rows, key=lambda r: (r["quality_score"], r["words"], r["route"]))
    type_counts = Counter(r["type"] for r in rows)
    missing = Counter()
    for row in rows:
        missing.update(filter(None, row["failed_checks"].split(";")))
    broken_targets = sorted({t for values in links_by_page.values() for t in values if t not in routes and t not in {"/robots.txt", "/sitemap.xml"}})

    lines = [
        "# Site Çapında İçerik ve SEO Kalite Envanteri",
        "",
        "Bu rapor `python3 scripts/audit_site_quality.py` ile yeniden üretilebilir. Puan bir sıralama tahmini değil; sayfa içi kalite kapılarının kapsama oranıdır.",
        "",
        "## Kapsam",
        f"- HTML sayfası: **{len(rows)}**",
        f"- Editoryal/klinik sayfa: **{len(editorial)}**",
        f"- İç link hedefi bulunamayan rota: **{len(broken_targets)}**",
        "- Sayfa türleri: " + ", ".join(f"{k}={v}" for k, v in sorted(type_counts.items())),
        "",
        "## Site çapında açıklar",
    ]
    lines.extend(f"- `{k}`: {v} sayfa" for k, v in missing.most_common())
    lines += ["", "## En düşük puanlı ilk 30 sayfa", "", "| Sayfa | Tür | Kelime | Inbound | Puan | Açıklar |", "|---|---|---:|---:|---:|---|"]
    for row in low[:30]:
        lines.append(f"| `{row['route']}` | {row['type']} | {row['words']} | {row['inbound_pages']} | {row['quality_score']} | {row['failed_checks'] or '—'} |")
    lines += ["", "## Doğrulama notları", "- Yinelenen title ve description alanları CSV'de ayrı sütunlardır.", "- Kaynak kontrolü görünür bir kaynak başlığı ile harici bağlantının birlikte bulunmasını ister.", "- Klinik rehberlerde derinlik eşiği 700 kelimedir; bu eşik tek başına kalite kanıtı değildir.", "- Aktif SEO deneylerindeki sayfalar bu envanterle değiştirilmez; değişiklik sırası deney kayıtlarıyla birlikte yönetilir."]
    if broken_targets:
        lines += ["", "## Çözümlenemeyen iç link hedefleri"] + [f"- `{x}`" for x in broken_targets]
    MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"pages={len(rows)} editorial={len(editorial)} csv={CSV_PATH.relative_to(ROOT)} md={MD_PATH.relative_to(ROOT)}")
    print("missing=" + json.dumps(missing, ensure_ascii=False, sort_keys=True))
    print("bottom=" + ", ".join(f"{r['route']}:{r['quality_score']}" for r in low[:10]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
