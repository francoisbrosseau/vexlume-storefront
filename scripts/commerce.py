"""Fail-closed hosted checkout configuration. No credentials or card processing."""
import re
from urllib.parse import urlsplit

GATES=('ownerApproved','filesUploaded','paymentConnected','deliveryTested','paymentTested','policiesReady')

def validate(config):
    if config.get('provider') != 'payhip' or config.get('currency') != 'USD':
        raise ValueError('Expected Payhip hosted checkout in USD.')
    for slug,p in config.get('products',{}).items():
        url=p.get('checkoutUrl')
        if url:
            u=urlsplit(url)
            if u.scheme!='https' or u.hostname!='payhip.com' or u.username or u.password or u.query or u.fragment or not re.fullmatch(r'/b/[A-Za-z0-9]+/?',u.path):
                raise ValueError('Checkout must be an exact HTTPS Payhip product link returned by the seller dashboard.')
    if config.get('launchEnabled') is True:
        seller=config.get('seller',{})
        if not seller.get('displayName') or not seller.get('legalDetailsVerified') or not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+',seller.get('supportEmail') or ''):
            raise ValueError('Verified seller identity and monitored support email are required before launch.')
        p=config.get('products',{}).get('inner-compass',{})
        if not p.get('checkoutUrl') or not all(p.get(k) is True for k in GATES):
            raise ValueError('Approval, uploaded files, payment connection, payment and delivery tests, and policies must be complete before launch.')
    return config

def checkout_for(slug,config):
    validate(config)
    if config.get('launchEnabled') is not True:return None
    product=config.get('products',{}).get(slug,{})
    return product.get('checkoutUrl') if all(product.get(k) is True for k in GATES) else None
