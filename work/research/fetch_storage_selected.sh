#!/usr/bin/env bash
set -euo pipefail
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
fetch() {
  local path="$1" slug="$2"
  local url="https://storage.courtlistener.com/${path}"
  sleep 5
  echo "=== $slug $url"
  curl -sL --max-time 90 -A "$UA" "$url" -o "work/sources/${slug}.pdf"
  file "work/sources/${slug}.pdf"
  pdftotext -layout "work/sources/${slug}.pdf" - > "work/texts/${slug}.txt" || true
  rg -n -i 'ChatGPT|Claude|Gemini|large language|artificial intelligence|generative|AI-generated|deepfake|deep fake|ordinary meaning|work product|privilege|technology assisted|Relativity|aiR|authentic|video|audio|voice' "work/texts/${slug}.txt" | head -80 || true
  shasum -a 256 "work/sources/${slug}.pdf"
}
fetch 'pdf/2026/03/25/in_the_interest_of_c.r._a_child_v._the_state_of_texas.pdf' 'in-re-cr-texas-2026-storage'
fetch 'pdf/2026/03/20/state_v._coleman.pdf' 'state-v-coleman-ohio-2026-storage'
fetch 'pdf/2026/03/25/elilton_alves_gouveia_v._meridian_financial_investments_llc.pdf' 'gouveia-v-meridian-fl-2026-storage'
fetch 'pdf/2025/06/30/nimat_shahid_v._sufyan_esaam.pdf' 'shahid-v-esaam-ga-2025-storage'
fetch 'pdf/2026/03/16/gosecure_v._crowdstrike.pdf' 'gosecure-v-crowdstrike-txbiz-2026-storage'
fetch 'pdf/2025/02/24/wadsworth_v._walmart_inc.pdf' 'wadsworth-v-walmart-dwyo-2025-storage'
