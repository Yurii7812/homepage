#!/usr/bin/env python3
"""Build matching Japanese/English guides from reviewed, source-based steps."""
from pathlib import Path
from html import escape as E
import json
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'docs/yuriinote-guide.json').read_text())
branch='feature/unified-index-guides-20261111'
for lang in ['ja','en']:
 ja=lang=='ja'; other='en' if ja else 'ja'; out=ROOT/lang/'yuriinote'
 title='YuriiNote 図解付き操作マニュアル' if ja else 'YuriiNote illustrated user manual'
 nav='ホーム' if ja else 'Home'
 html=[f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title><link rel="stylesheet" href="../../style.css"><link rel="stylesheet" href="../../assets/guides.css"><script defer src="../../assets/guide-zoom.js"></script></head><body><main class="manual"><nav><a href="../">{nav}</a> · <a href="../../{other}/yuriinote/">{"English" if ja else "日本語"}</a> · <a href="https://github.com/Yurii7812/YuriiNote">GitHub</a> · <a href="../paper-pkm/">{"紙だけのPKM" if ja else "Paper-only PKM"}</a> · <a href="guide.md">Markdown</a></nav><header><p class="eyebrow">YURIINOTE / GUIDE / 2026-11-11</p><h1>{title}</h1>']
 intro=('既存のYuriiNote 1.1.0と今回の開発ブランチを調べ、実際のElectron画面で主要操作を確認しました。画面は説明用のサンプルデータです。日本語UIのスクリーンショットを使っています。' if ja else 'Based on YuriiNote 1.1.0 and the development branch below. Major workflows were checked in Electron using sample data. Screenshots show the Japanese UI; English instructions identify the corresponding controls.')
 state=('開発版について：共通Index・表示フィルターの拡張・トピック検索と記号の改良は、作業ブランチの機能です。安定版への統合やインストーラーの公開とは別です。' if ja else 'Development version: unified Index, expanded display filtering, Topic Index completion and marker changes belong to the working branch. A source change is separate from a merged stable release or published installer.')
 html += [f'<p>{intro}</p><aside class="status">{state}<br><a href="https://github.com/Yurii7812/YuriiNote/tree/{branch}">{branch}</a></aside></header><nav class="toc" aria-label="Contents"><ol>']
 md=[f'# {title}\n',intro+'\n',state+'\n']
 for section in data:
  html.append(f'<li><a href="#{section["id"]}">{E(section[lang]["title"])}</a></li>')
 html.append('</ol></nav>')
 for i,section in enumerate(data,1):
  d=section[lang];html.append(f'<section id="{section["id"]}"><h2><span class="section-number">{i:02}</span> {E(d["title"])}</h2><p>{d["intro"]}</p><ol class="steps">')
  md += [f'\n## {i}. {d["title"]}\n',d['intro']+'\n']
  for n,step in enumerate(d['steps'],1):html.append(f'<li>{step}</li>');md.append(f'{n}. {step}')
  html.append('</ol>')
  if d.get('note'):html.append(f'<p class="note">{d["note"]}</p>');md.append('\n'+d['note'])
  for fig in section.get('figures',[]):
   caption=fig[lang]; pins=''.join(f'<span class="pin" style="left:{x/12:.3f}%;top:{y/8:.3f}%">{n}</span>' for n,x,y in fig.get('pins',[]))
   html.append(f'<figure class="screen" data-zoom><div class="screen-wrap"><img src="../../assets/yuriinote/{fig["file"]}.png" width="1200" height="800" loading="lazy" alt="{E(caption)}">{pins}</div><figcaption>{E(caption)} <span>({"クリック・タップで拡大" if ja else "Click or tap to enlarge"})</span></figcaption></figure>')
  if section.get('table'):
   table=section['table'][lang];html.append('<div class="table-scroll"><table><thead><tr>'+''.join(f'<th>{x}</th>' for x in table[0])+'</tr></thead><tbody>')
   for row in table[1:]:html.append('<tr>'+''.join(f'<td>{x}</td>' for x in row)+'</tr>')
   html.append('</tbody></table></div>')
  files=section.get('sources',[])
  html.append('<details class="source"><summary>'+('実装の参照先' if ja else 'Implementation sources')+'</summary><ul>'+''.join(f'<li><a href="https://github.com/Yurii7812/YuriiNote/blob/{branch}/{f}">{f}</a></li>' for f in files)+'</ul></details></section>')
 html += ['<footer><p>'+('図の番号は、その図の操作対象を示します。OSによるファイル選択・USB実機連携・配布版の更新は環境に依存し、すべての組み合わせを実機検証したものではありません。' if ja else 'Numbered markers identify controls in each figure. OS file pickers, physical USB transfer and packaged-app updates depend on the environment and were not tested on every platform.')+'</p><a href="versions/2026-11-11-before-integrated-guides/index.html">'+('更新前のページ' if ja else 'Previous page')+'</a> · <a href="../../docs/integrated-guides-changelog.md">Changelog</a></footer></main></body></html>']
 (out/'index.html').write_text('\n'.join(html));(out/'guide.md').write_text('\n'.join(md))
