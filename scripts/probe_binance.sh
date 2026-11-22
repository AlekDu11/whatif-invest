#!/bin/bash
# One-off probe of Binance Web3 public market endpoints: field names of the first item
H=(-H 'Content-Type: application/json' -H 'Accept-Encoding: identity' -H 'User-Agent: binance-web3/1.1 (Skill)')
B=https://web3.binance.com/bapi/defi
echo "== unified"; curl -s -m 20 -X POST "$B/v1/public/wallet-direct/buw/wallet/market/token/pulse/unified/rank/list/ai" "${H[@]}" -d '{"rankType":10,"chainId":"CT_501","period":50,"page":1,"size":2}' | jq -c '.data.tokens[0]' | head -c 3000; echo
echo "== rush"; curl -s -m 20 -X POST "$B/v1/public/wallet-direct/buw/wallet/market/token/pulse/rank/list/ai" "${H[@]}" -d '{"chainId":"CT_501","rankType":30,"limit":2}' | jq -c '.data[0]' | head -c 3000; echo
echo "== rush keys"; curl -s -m 20 -X POST "$B/v1/public/wallet-direct/buw/wallet/market/token/pulse/rank/list/ai" "${H[@]}" -d '{"chainId":"56","rankType":10,"limit":2}' | jq -c '.data[0]|keys'; echo
