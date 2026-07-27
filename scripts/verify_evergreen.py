#!/usr/bin/env python3
"""Targeted validator for the evergreen guide-system rollout."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ROOT / "kaygi-dongusu.html",
    ROOT / "uygulamalar/kacinma-haritasi.html",
    ROOT / "araclar/islevsel-takip.html",
    ROOT / "ogrenme-yollari/kaygi.html",
    ROOT / "site-haritasi.html",
]
EXPECTED_URLS = {
    "https://www.atapamukcu.com/kaygi-dongusu",
    "https://www.atapamukcu.com/uygulamalar/kacinma-haritasi",
    "https://www.atapamukcu.com/araclar/islevsel-takip",
    "https://www.atapamukcu.com/ogrenme-yollari/kaygi",
}

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.scripts = []
        self.canonicals = []
        self.titles = []
        self._title = False
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get("id"): self.ids.append(data["id"])
        if tag == "a" and data.get("href"): self.links.append(data["href"])
        if tag == "script" and data.get("src"): self.scripts.append(data["src"])
        if tag == "link" and data.get("rel") == "canonical": self.canonicals.append(data.get("href", ""))
        if tag == "title": self._title = True
    def handle_endtag(self, tag):
        if tag == "title": self._title = False
    def handle_data(self, data):
        if self._title: self.titles.append(data)

def local_target(href):
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
        return None
    path = href.split("#", 1)[0].split("?", 1)[0]
    if not path:
        return None
    path = path.lstrip("/")
    candidate = ROOT / path
    if candidate.suffix:
        return candidate
    return ROOT / (path + ".html")

errors = []
canonicals = set()
titles = set()
json_count = 0
links_checked = 0
for page in PAGES:
    if not page.exists():
        errors.append(f"missing page: {page.relative_to(ROOT)}")
        continue
    text = page.read_text(encoding="utf-8")
    parser = AuditParser(); parser.feed(text)
    if parser.get_starttag_text() is None and "<html" not in text:
        errors.append(f"not html: {page.name}")
    duplicates = {x for x in parser.ids if parser.ids.count(x) > 1}
    if duplicates: errors.append(f"duplicate ids {page.name}: {sorted(duplicates)}")
    if len(parser.canonicals) != 1: errors.append(f"canonical count {page.name}: {len(parser.canonicals)}")
    else:
        if parser.canonicals[0] in canonicals: errors.append(f"duplicate canonical: {parser.canonicals[0]}")
        canonicals.add(parser.canonicals[0])
    title = "".join(parser.titles).strip()
    if not title: errors.append(f"missing title: {page.name}")
    elif title in titles: errors.append(f"duplicate title: {title}")
    titles.add(title)
    for src in parser.scripts:
        target = local_target(src)
        if target and not target.exists(): errors.append(f"missing script {src} from {page.name}")
    for href in parser.links:
        target = local_target(href)
        if target:
            links_checked += 1
            if not target.exists(): errors.append(f"broken local link {href} from {page.relative_to(ROOT)}")
    blocks = re.findall(r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>', text, re.S)
    if not blocks: errors.append(f"no JSON-LD: {page.name}")
    for block in blocks:
        try:
            data = json.loads(block)
            json_count += 1
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON-LD {page.name}: {exc}")
            continue
        objects = data if isinstance(data, list) else [data]
        for obj in objects:
            if isinstance(obj, dict) and obj.get("@type") == "Article" and obj.get("citation"):
                schema_urls = set(obj["citation"])
                source_match = re.search(r'<section class="article-sources".*?</section>', text, re.S)
                visible_urls = set(re.findall(r'href="(https://(?:www\.)?(?:nimh\.nih\.gov|nice\.org\.uk|doi\.org)/?[^"]*)"', source_match.group(0) if source_match else ""))
                if schema_urls != visible_urls:
                    errors.append(f"citation mismatch {page.name}: schema={schema_urls} visible={visible_urls}")

# Page-specific functional and safety checks.
REQUIRED_TEXT = {
    "kaygi-dongusu.html": ["Bu rehber tanı değildir", "ciddi nefes darlığı", "kısa vadeli rahatlama", "uzun vadeli sonuçlarını"],
    "uygulamalar/kacinma-haritasi.html": ["Ne değildir?", "Kimin için uygun olmayabilir?", "Durma ölçütü", "Acil destek"],
    "araclar/islevsel-takip.html": ['id="trackerForm"', 'id="downloadCsv"', "sunucuya gönderilmez", "tarayıcı depolamasına yazılmaz"],
    "ogrenme-yollari/kaygi.html": ["Kaygının genel çerçevesini okuyun", "Döngünün nasıl sürdüğünü öğrenin", "Tek bir kaçınma örneğini haritalayın", "Örüntünün tekrarını gözlemleyin", "Profesyonel ve acil destek"],
}
for rel, needles in REQUIRED_TEXT.items():
    page = ROOT / rel
    text = page.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text: errors.append(f"missing required phrase {needle!r} in {page.name}")

# Sitemap integrity and inclusion.
try:
    root = ET.parse(ROOT / "sitemap.xml").getroot()
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = {node.text for node in root.findall("s:url/s:loc", ns)}
    missing_urls = EXPECTED_URLS - urls
    if missing_urls: errors.append(f"sitemap missing: {sorted(missing_urls)}")
except Exception as exc:
    errors.append(f"invalid sitemap: {exc}")

# Cross-page discovery points.
index = (ROOT / "araclar.html").read_text(encoding="utf-8")
for href in ["/uygulamalar/kacinma-haritasi", "/araclar/islevsel-takip", "/araclar/kaygi-dongusu-haritasi"]:
    if f'href="{href}"' not in index: errors.append(f"tools index missing {href}")

if errors:
    print("FAILED")
    for error in errors: print("-", error)
    sys.exit(1)
print("passed / ad_hoc / targeted")
print(f"pages={len(PAGES)}/{len(PAGES)} json_ld={json_count} local_links={links_checked} sitemap={len(EXPECTED_URLS)}/{len(EXPECTED_URLS)}")
print("citation_alignment=PASS privacy_checks=PASS duplicate_ids=PASS")
