#!/usr/bin/env bash
set -euo pipefail
UA='SafeLegalAI-Bot/1.0 (+https://safelegalai.com/datasets; hello@safelegalai.com)'
for doc in $(seq 168 198); do
  u="https://storage.courtlistener.com/recap/gov.uscourts.vaed.535291/gov.uscourts.vaed.535291.${doc}.0.pdf"
  headers=$(curl -sI --max-time 12 -A "$UA" "$u" | tr -d '\r' || true)
  status=$(printf '%s\n' "$headers" | awk 'NR==1{print $2}')
  len=$(printf '%s\n' "$headers" | awk 'tolower($1)=="content-length:"{print $2}')
  lm=$(printf '%s\n' "$headers" | awk 'tolower($1)=="last-modified:"{$1=""; sub(/^ /,""); print}')
  printf '%s\t%s\t%s\t%s\n' "$doc" "$status" "$len" "$lm"
  sleep 5
done
