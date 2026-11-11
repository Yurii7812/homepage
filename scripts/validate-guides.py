#!/usr/bin/env python3
"""Check current guide links, image assets, anchors and language parity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__();self.path=path;self.ids=[];self.links=[];self.images=[];self.figures=0;self.headings=[];self.lang=None
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a:self.ids.append(a['id'])
  if t=='html':self.lang=a.get('lang')
  if t=='a' and 'href' in a:self.links.append(a['href'])
  if t in ['link','script'] and (a.get('src') or a.get('href')):self.links.append(a.get('src') or a['href'])
  if t=='img':self.images.append(a);self.links.append(a['src'])
  if t=='figure':self.figures+=1
pages={}
for lang in ['ja','en']:
 for name in ['index.html','paper-pkm/index.html','yuriinote/index.html']:
  p=ROOT/lang/name;q=Page(p);q.feed(p.read_text());pages[p.resolve()]=q
errors=[];checked=0
for p,page in pages.items():
 if len(page.ids)!=len(set(page.ids)):errors.append(f'duplicate anchors: {p}')
 for image in page.images:
  if not image.get('alt'):errors.append(f'image without alt: {p}: {image}')
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'broken local link: {p.relative_to(ROOT)} -> {link}');continue
  checked+=1
  if u.fragment and target.suffix=='.html':
   parser=pages.get(target)
   if not parser:parser=Page(target);parser.feed(target.read_text())
   if unquote(u.fragment) not in parser.ids:errors.append(f'missing anchor: {link}')
for kind in ['paper-pkm','yuriinote']:
 ja=pages[(ROOT/'ja'/kind/'index.html').resolve()];en=pages[(ROOT/'en'/kind/'index.html').resolve()]
 if set(ja.ids)!=set(en.ids):errors.append(f'language anchor mismatch: {kind}: {set(ja.ids)^set(en.ids)}')
 if ja.figures!=en.figures:errors.append(f'language figure count mismatch: {kind}')
 if kind=='paper-pkm' and ja.figures<12:errors.append('fewer than 12 paper diagrams')
 if kind=='yuriinote' and ja.figures<12:errors.append('fewer than 12 app figures')
for section in json.loads((ROOT/'docs/yuriinote-guide.json').read_text()):
 if len(section['ja']['steps'])!=len(section['en']['steps']):errors.append(f'step mismatch: {section["id"]}')
 for file in section['sources']:
  if (ROOT.parent/'YuriiNote').exists() and not (ROOT.parent/'YuriiNote'/file).exists():errors.append(f'missing implementation source: {file}')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} current pages; {checked} local links/assets; bilingual anchors and steps match.')
for kind in ['paper-pkm','yuriinote']:
 print(f'{kind}: {pages[(ROOT/"ja"/kind/"index.html").resolve()].figures} figures per language')
