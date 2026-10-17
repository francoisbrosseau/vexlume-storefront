from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json
R=Path(__file__).resolve().parents[1];D=R/'dist';issues=[];references=0
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.ids=set();self.refs=[];self.description=False;self.title=False;self.lang=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='html':self.lang=bool(a.get('lang'))
  if tag=='meta' and a.get('name')=='description':self.description=bool(a.get('content'))
  if tag=='img':
   assert 'alt' in a,'missing image alt'
   assert a.get('width') and a.get('height'),'missing image size'
  if a.get('id'):
   assert a['id'] not in self.ids,'duplicate ID';self.ids.add(a['id'])
  for k in ['src','href']:
   if a.get(k):self.refs.append(a[k])
  if a.get('srcset'):
   self.refs.extend(x.strip().split(' ')[0] for x in a['srcset'].split(','))
for f in D.rglob('*.html'):
 p=Parser();p.feed(f.read_text());assert p.h1==1 and p.description and p.title and p.lang,f
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  if not u.path:
   assert not u.fragment or u.fragment in p.ids,(f,ref)
   continue
  dest=D/u.path.lstrip('/') if u.path.startswith('/') else f.parent/u.path
  if u.path.endswith('/'):dest/='index.html'
  assert dest.is_file(),(f,ref)
  references+=1
 assert 'noindex,nofollow' in f.read_text(),f
assert not (R/'products').exists()
assert not (R/'scripts/products.py').exists()
print(json.dumps({'html_pages':len(list(D.rglob('*.html'))),'local_references_checked':references,'paid_masters_in_public_source':False,'broken_local_references':0,'browser_visual_qa':'unavailable: control-browser skill absent','checkout':'disabled'},indent=2))

allowed_pdfs={'weekly-reset-planner.pdf','inner-compass-preview.pdf','financial-clarity-kit-preview.pdf','next-chapter-planner-preview.pdf','steady-strength-preview.pdf'}
assert {p.name for p in D.rglob('*.pdf')} <= allowed_pdfs, 'A full paid file may have been added to public output'
assert not list(D.rglob('*.zip')), 'Paid ZIP must not be public'
