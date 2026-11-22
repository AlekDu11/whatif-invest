#!/bin/bash
# One-off probe of Binance Web3 public market endpoints (owner 2026-11-22: test as the memes data source)
H=(-H 'Content-Type: application/json' -H 'Accept-Encoding: identity' -H 'User-Agent: binance-web3/1.1 (Skill)')
B=https://web3.binance.com/bapi/defi
for c in CT_501 56 8453; do
  echo "== trending $c"; curl -s -m 20 -w '\n%{http_code} %{time_total}s\n' -X POST "$B/v1/public/wallet-direct/buw/wallet/market/token/pulse/unified/rank/list/ai" "${H[@]}" -d "{\"rankType\":10,\"chainId\":\"$c\",\"period\":50,\"page\":1,\"size\":3}" | head -c 1500; echo
done
echo "== meme rush new sol"; curl -s -m 20 -w '\n%{http_code} %{time_total}s\n' -X POST "$B/v1/public/wallet-direct/buw/wallet/market/token/pulse/rank/list/ai" "${H[@]}" -d '{"chainId":"CT_501","rankType":10,"limit":3}' | head -c 1500; echo
echo "== meme rush migrated sol"; curl -s -m 20 -w '\n%{http_code} %{time_total}s\n' -X POST "$B/v1/public/wallet-direct/buw/wallet/market/token/pulse/rank/list/ai" "${H[@]}" -d '{"chainId":"CT_501","rankType":30,"limit":3}' | head -c 1200; echo
echo "== audit"; curl -s -m 20 -w '\n%{http_code}\n' -X POST "$B/v1/public/wallet-direct/security/token/audit" "${H[@]}" -H 'User-Agent: binance-web3/1.4 (Skill)' -d '{"binanceChainId":"CT_501","contractAddress":"DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263","requestId":"6f1c8d2e-1a2b-4c3d-9e8f-0a1b2c3d4e5f"}' | head -c 1500; echo
