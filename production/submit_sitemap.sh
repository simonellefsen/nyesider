#!/usr/bin/env bash
# Ping Google/Bing with sitemap + submit IndexNow (Bing and supporting engines).
set -euo pipefail
SITE="${SITE_URL:-https://nyesider.vercel.app}"
SITEMAP="${SITE}/sitemap.xml"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [[ -z "${INDEXNOW_KEY:-}" ]]; then
  for f in "$ROOT"/web/static/*.txt; do
    [[ -f "$f" ]] || continue
    base=$(basename "$f" .txt)
    if [[ "$base" =~ ^[a-f0-9]{32}$ ]]; then
      INDEXNOW_KEY="$base"
      break
    fi
  done
fi

echo "== Sitemap =="
echo "$SITEMAP"
curl -sI "$SITEMAP" | head -8
URL_COUNT=$(curl -sL "$SITEMAP" | grep -c '<loc>https://nyesider.vercel.app/[^c]' || true)
# count page locs only (not image under /content/)
PAGE_COUNT=$(curl -sL "$SITEMAP" | grep -oE '<loc>https://nyesider\.vercel\.app[^<]*</loc>' | grep -vc '/content/' || true)
echo "Page URLs in sitemap: $PAGE_COUNT"

echo ""
echo "== Google sitemap ping =="
ENC=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$SITEMAP'''))")
curl -sS -o /tmp/g-ping.txt -w "HTTP %{http_code}\n" "https://www.google.com/ping?sitemap=${ENC}" || true
head -c 300 /tmp/g-ping.txt 2>/dev/null; echo

echo ""
echo "== Bing sitemap ping =="
curl -sS -o /tmp/b-ping.txt -w "HTTP %{http_code}\n" "https://www.bing.com/ping?sitemap=${ENC}" || true
head -c 300 /tmp/b-ping.txt 2>/dev/null; echo

if [[ -n "${INDEXNOW_KEY:-}" ]]; then
  echo ""
  echo "== IndexNow (key=${INDEXNOW_KEY}) =="
  KEY_LOC="${SITE}/${INDEXNOW_KEY}.txt"
  code=$(curl -s -o /dev/null -w "%{http_code}" "$KEY_LOC")
  echo "Key location: $KEY_LOC → HTTP $code"
  if [[ "$code" != "200" ]]; then
    echo "ERROR: key file not live — deploy first, then re-run."
    exit 1
  fi
  INDEXNOW_KEY="$INDEXNOW_KEY" KEY_LOC="$KEY_LOC" SITEMAP="$SITEMAP" python3 - <<'PY'
import json, os, re, urllib.request
sitemap = urllib.request.urlopen(os.environ["SITEMAP"]).read().decode()
urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sitemap) if "/content/" not in u]
payload = {
  "host": "nyesider.vercel.app",
  "key": os.environ["INDEXNOW_KEY"],
  "keyLocation": os.environ["KEY_LOC"],
  "urlList": urls,
}
req = urllib.request.Request(
  "https://api.indexnow.org/indexnow",
  data=json.dumps(payload).encode(),
  headers={"Content-Type": "application/json; charset=utf-8"},
  method="POST",
)
try:
  with urllib.request.urlopen(req) as resp:
    print("IndexNow HTTP", resp.status, resp.read()[:200].decode())
except Exception as e:
  if hasattr(e, "code"):
    body = e.read().decode() if hasattr(e, "read") else ""
    print("IndexNow HTTP", e.code, body[:500])
  else:
    print(e)
print(f"Submitted {len(urls)} page URLs via IndexNow")
PY
else
  echo "No IndexNow key found in web/static/*.txt"
fi

echo ""
echo "Manual follow-up if needed:"
echo "  Google Search Console: https://search.google.com/search-console"
echo "  Bing Webmaster Tools:  https://www.bing.com/webmasters"
echo "  Sitemap URL: $SITEMAP"
