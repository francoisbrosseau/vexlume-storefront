# Hosting and checkout / preliminary research, October 2026

## Preferred architecture

Private GitHub source -> approved commercial static hosting of `dist/` only -> Payhip-hosted checkout -> provider-hosted paid download. No custom payment processing, card storage, customer database or backend is needed for the opening collection.

## Payhip

Official pricing reviewed at https://payhip.com/pricing : Free Forever is $0/month with a 5% transaction fee, in addition to PayPal/Stripe processing fees. The page lists unlimited products/revenue and the same features across plans. Do not describe the store as cost-free per sale.

Official product documentation: https://help.payhip.com/article/59-adding-a-digital-product . Provider-hosted digital products are supported. Product IDs, hosted checkout links, uploaded files and receipt emails have NOT been configured.

The pricing page currently describes collection/remittance of certain regional taxes. This is a provider claim, not confirmation of this merchant's GST/HST/QST responsibilities or account-specific coverage. Verify the tax-feature documentation and actual setup before launch. Canadian seller eligibility, PayPal account/currency requirements, receipt/email delivery, refund behavior, embedded checkout limits and tax details still need account-specific verification. No account was created and no terms accepted.

## Hosting

Cloudflare Pages is a candidate for a static boutique. Official documentation https://developers.cloudflare.com/pages/functions/pricing/ states that requests to static assets are free and unlimited on free and paid plans when they do not invoke Functions. This implementation uses static files only. Review current service terms, commercial use, build limits, access controls and account requirements before selecting it. No plan, account or deployment was created.

Deployment configuration: root=`dist/`; no runtime build required, no Functions; `_headers` is prepared for a compatible host. Never select repository root as the upload directory. Disable automatic public production deployment while in private staging; no GitHub Pages configuration is included.

## Cost and checkout approval

No spending has occurred. Domain registration and provider subscriptions require separate approval. A new domain is not technically required to test an owner-access staging environment. Production custom-domain and canonical configuration intentionally remain unset.
