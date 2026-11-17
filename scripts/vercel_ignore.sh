#!/usr/bin/env bash
# Vercel "Ignored Build Step": exit 0 = skip this deployment, exit 1 = build it.
# Each deployment stores the whole site (~0.6 GB); the Hobby plan allows 10 GB, so we do not deploy on every push.
# Builds happen only for commits whose message contains [deploy]: .github/workflows/deploy.yml makes one every 4 hours
# when something that affects the site changed; urgent fixes put [deploy] in their own commit message.
if git log -1 --pretty=%B | grep -q "\[deploy\]"; then echo "deploy requested"; exit 1; fi
echo "skipped: no [deploy] in the commit message (scheduled deploys every 4 hours)"; exit 0
