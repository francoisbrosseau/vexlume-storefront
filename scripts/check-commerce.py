import copy,json
from pathlib import Path
from commerce import validate,checkout_for,GATES

config=json.loads((Path(__file__).resolve().parents[1]/'src/commerce.json').read_text())
assert checkout_for('inner-compass',config) is None
base=copy.deepcopy(config)
base['launchEnabled']=True
base['seller']={'displayName':'Synthetic test seller','supportEmail':'qa@example.org','legalDetailsVerified':True}
p=base['products']['inner-compass'];p['checkoutUrl']='https://payhip.com/b/Test123'
for g in GATES:p[g]=True
assert checkout_for('inner-compass',base)=='https://payhip.com/b/Test123'
assert checkout_for('financial-clarity-kit',base) is None
for g in GATES:
    bad=copy.deepcopy(base);bad['products']['inner-compass'][g]=False
    try:validate(bad)
    except ValueError:pass
    else:raise AssertionError('Missing gate accepted: '+g)
for url in ['http://payhip.com/b/Test123','https://payhip.com.evil.test/b/Test123','javascript:alert(1)','https://payhip.com@evil.test/b/Test123','https://user:pass@payhip.com/b/Test123','https://payhip.com/b/Test123?redirect=elsewhere']:
    bad=copy.deepcopy(base);bad['products']['inner-compass']['checkoutUrl']=url
    try:validate(bad)
    except ValueError:pass
    else:raise AssertionError('Unsafe checkout accepted')
bad=copy.deepcopy(base);bad['seller']['supportEmail']=None
try:validate(bad)
except ValueError:pass
else:raise AssertionError('Missing support accepted')
print('PASS: disabled checkout, all launch gates, safe provider URLs, seller support and unavailable products.')
