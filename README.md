# VEXLUME — Beautiful Tools for Real Life.

Public development storefront. Checkout is disabled. Paid product masters and their generation source are stored separately in a private repository.

## Source and hosting

This GitHub repository is the authoritative storefront source; Sites hosts a deployment mirror. Publish only `dist/`. The checked-in site needs no build dependencies. `scripts/build.py` regenerates HTML and vector covers with Python standard libraries; `dist/assets/style.css` and `app.js` are editable source. Never add paid product masters or credentials here.

The free planner and three-page evaluation sample are intentionally public. Other products are marked in development.

## Development checks

`node --check dist/assets/app.js` and `node scripts/check-interactions.cjs`. Browser/device QA remains outstanding. Search and mobile navigation have source-level interaction checks.

## Launch status

Public preview authorized October 16, 2026. This is not an operational paid store: payment/delivery, seller information, final policies, naming/domain clearance and product completion remain required. Search indexing remains disabled during development. See `docs/launch-readiness.md`.
