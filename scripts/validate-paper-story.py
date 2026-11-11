#!/usr/bin/env python3
from pathlib import Path
import re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
for lang in ['ja','en']:
 p=ROOT/lang/'paper-pkm/index.html';s=p.read_text()
 pos=[s.index(f'id="why-step-{i}"') for i in range(10)]
 assert pos==sorted(pos)
 assert s.index('id="paper-map"')>pos[-1]
 assert s.index('id="benefits"')>pos[-1]
 assert s.index('id="diagram-directory"')>pos[-1]
 assert s.index('id="practical-guide"')>pos[-1]
 for i in range(10):
  f=ROOT/'assets/paper-pkm-story'/f'{lang}-{i:02}.svg';r=ET.parse(f).getroot();assert r.attrib['viewBox'].startswith('0 0 900 ')
  text=' '.join(r.itertext())
  if i<3:assert 'Topic Index' not in text
  if i<4:assert 'Global Index' not in text
  assert s.count(f'src="../../assets/paper-pkm-story/{lang}-{i:02}.svg"')==1
 assert 'only one ID gets no dot' not in s
 assert '索引があっても点は付けない' not in s
 print(f'PASS: {lang}, one starting sheet + eight problems + final diagram; later mechanisms withheld')
