#!/usr/bin/env python3
"""Add a progressive explanation to the existing bilingual paper PKM guides."""
from pathlib import Path
from html import escape as E
import re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/paper-pkm-story';OUT.mkdir(exist_ok=True)
C={'ink':'#253b36','blue':'#244d78','red':'#b33a35','green':'#35664d','line':'#91a897'}
def txt(x,y,s,size=20,color='ink',weight=400):return f'<text x="{x}" y="{y}" font-size="{size}" fill="{C.get(color,color)}" font-weight="{weight}" text-anchor="start">{E(s)}</text>'
def card(x,y,w,h,title,lines=(),kind='note',id='',dot=False):
 fill='#fffdf6' if kind=='note' else '#edf4e9' if kind=='topic' else '#f8efd8'
 out=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{C["line"]}" stroke-width="1.5"/>'
 if kind=='slip':out+=f'<circle cx="{x+15}" cy="{y+h/2}" r="5" fill="none" stroke="#8b815d" stroke-width="2"/>'
 if id:
  out+=txt(x+18,y+30,id,21,'blue',700)
  if dot:out+=f'<circle cx="{x+25}" cy="{y+8}" r="4" fill="{C["red"]}"/>'
  out+=txt(x+18,y+61,title,19,'ink',600);start=y+94
 else:out+=txt(x+30 if kind=='slip' else x+18,y+33,title,20,'ink',600);start=y+65
 for i,line in enumerate(lines):out+=txt(x+30 if kind=='slip' else x+18,start+i*27,line,18,'blue')
 return out
def edge(d,color='green',dashed=False):return f'<path d="{d}" fill="none" stroke="{C[color]}" stroke-width="2"'+(' stroke-dasharray="6 5"' if dashed else '')+' marker-end="url(#arrow)"/>'
def fig(n,lang,title,draw,height=420):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}" role="img" aria-labelledby="title desc"><title id="title">{E(title)}</title><desc id="desc">{E(title)}</desc><defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8" fill="{C["green"]}"/></marker></defs><rect width="900" height="{height}" fill="#f1f5ed"/><g font-family="Noto Sans CJK JP, Noto Sans, sans-serif">{draw}</g></svg>'
 file=f'{lang}-{n:02}.svg';(OUT/file).write_text(svg)
 return f'<figure class="story-figure" id="story-figure-{n}" data-zoom><img src="../../assets/paper-pkm-story/{file}" alt="{E(title)}" width="900" height="{height}"><figcaption>{E(title)}</figcaption></figure>'
JA=[
('一枚なら、まだ困らない','カバンを買おうと思い、A4に気づいたことを書く。まだ必要なのは、考えを書き残す場所だけだ。','「軽い物がよい」「雨で濡れるかもしれない」と書く。最初から分類や索引を作る必要はない。'),
('関連するノートが増えたら、どう置く？','素材、購入候補、耐久性を別々に調べた。全部に独立した番号を付けるだけでは、カバンの話からどのノートが生まれたかが見えにくい。','Folgezettelの分岐を使う。素材は1a、購入候補は1b、素材について考えた耐久性は1a1へ置く。深めるだけでなく、関連する話へ広げるときにも使う。厳密な親子分類ではない。'),
('離れた場所で、関連が見つかったら？','以前の27「旅行用品」を読み返すと、1a「素材」の内容が役立ちそうだ。関連が増えるたびに移動や番号変更をするのは大変だ。','相手のIDを本文に書いて参照する。必要なら双方に書く。配置による関連をFolgezettelが、離れた場所との関連を相互参照が受け持つ。'),
('「買い物全体」を見たいときは？','1からリンクをたどれば素材や旅行用品へ進める。でも、靴や家電も含めた購入検討を一か所で見渡すには、行き来が多い。','2-買い物というTopic Indexを作り、キーワードとIDを並べる。異なる枝の1・1b・15・28を一枚に集められる。同じノートを別のTopic Indexにも載せてよい。'),
('そのTopic Indexは、どこから探す？','「買い物」「旅行」「技術」と索引が増えると、索引の入口自体を覚える必要が出てくる。','キーワードごとに小さな紙片を一枚作り、Global Indexとして読みの五十音順にリングへ綴じる。買い物から2-買い物へ進めるし、カバンから本文1へ直接進んでもよい。'),
('番号に空きができたら、振り直す？','1、1a、1a1、1c、2、5、5b、12のように番号が飛ぶと、連続したページ番号にそろえたくなる。振り直すほど、参照先の修正も増えてしまう。','この運用例では欠番を詰めない。IDはノートの識別と関連の手がかりであり、通しのページ番号ではない。探すときは索引を使い、しまうときは存在する紙をID順に重ねる。'),
('すべてにTopic Indexを作る必要はある？','ノートを一枚作るたびに専用の索引も作ると、考えるより管理に時間がかかる。','必要な話題だけにTopic Indexを作る。この例では買い物2には作り、カバン1は本文だけにする。対応する索引がある2の真上に赤い点を付ける。1つのIDにつきTopic Indexは最大1つで、同じ索引の続きは複数ページでもよい。'),
('書く前に分類を決めなければいけない？','カバンの話は買い物にも旅行にも関係する。先にどちらかへ分類しようとすると、内容を書く前に置き場所で迷ってしまう。','まず書き、内容を見てIDを決める。次に必要なキーワードと索引項目を足す。後で旅行との関連に気づいたら、索引や相互参照を追加すればよい。既存のIDを付け替える必要はない。'),
('アプリが使えなくても、たどれる？','検索やリンクがソフトウェアにしかなければ、それを開けないときに必要なノートへ届かない。','紙片のキーワード、A4のTopic Index、本文に書いたID、ID順のクリアファイルだけで、同じ道順をたどる。YuriiNoteなどのデジタル運用は別に設計でき、紙の方式の成立条件にはしない。'),
('ここで、初めて全体を見る','一つずつ足した道具は、それぞれ違う困りごとを受け持つ。Global IndexとTopic Indexの二つを組み合わせる部分が、Double Index Systemである。','カバンを探すなら紙片から1へ直接、買い物を見渡すなら紙片から2-買い物を経て1・1b・15・28へ。そこから分岐や相互参照を使って読み広げ、読み終えた紙はID順に戻す。')]
EN=[
('One sheet is easy to find','You are thinking about buying a bag and write observations on A4. For now, you only need somewhere to think on paper.','Write “lightweight” and “may get wet in the rain.” You do not need to invent categories or indexes before you begin.'),
('Where do related notes belong?','You investigate materials, candidates and durability. Separate independent numbers identify the notes, but do not reveal how they grew from the bag investigation.','Use Folgezettel branches: 1a for materials, 1b for candidates, and 1a1 for durability developed from the materials note. A branch can deepen an idea or extend it to a related subject; it is not a rigid classification hierarchy.'),
('What if a connection crosses the branches?','An earlier note, 27 “Travel supplies,” turns out to be relevant to materials in 1a. Moving or renumbering notes whenever a relationship appears creates extra work.','Write the other ID in the text, and add a return reference when useful. Folgezettel preserves relationships through placement; cross-references add connections across distant locations.'),
('How do you see the whole shopping project?','Following links from 1 reaches materials and travel supplies. But seeing the purchase research for bags, shoes and appliances together requires a lot of navigation.','Create 2–Shopping as a Topic Index, with keywords and IDs. It collects 1, 1b, 15 and 28 from different branches. A note can appear in more than one Topic Index.'),
('How do you find the indexes themselves?','As Shopping, Travel, Technology and other indexes accumulate, remembering where each index starts becomes another problem.','Make one small slip per keyword and file the slips on a ring in reading/alphabetical order as the Global Index. Shopping leads to 2–Shopping; Bags can also lead straight to content note 1.'),
('Must the numbers be made consecutive?','A sequence such as 1, 1a, 1a1, 1c, 2, 5, 5b, 12 has gaps. Renumbering it to look complete also creates references that need updating.','In this working example, leave the gaps. An ID identifies a note and records a relationship; it is not a consecutive page number. Use the indexes to find notes and file the sheets that actually exist in ID order.'),
('Does every note need a Topic Index?','Creating a dedicated index for every new sheet can make maintaining the collection more work than thinking.','Make a Topic Index where it is useful. Here, Shopping 2 has one while Bags 1 remains a content note. Put a red dot above 2 to indicate its index. Each ID has at most one Topic Index, which may occupy several sheets.'),
('Must you classify a note before writing?','A bag belongs to both shopping and travel. Choosing a category first can interrupt the idea before it reaches the page.','Write first, choose an ID from the content, then add useful keywords and index entries. If a travel connection appears later, add an index entry or cross-reference. The existing note keeps its ID.'),
('Can you still find it without an app?','If all searching and linking depends on software, losing access to that software can block access to the collection.','Keyword slips, A4 Topic Indexes, written ID references and clear folders in ID order provide the entire route on paper. Digital tools such as YuriiNote can be designed as a separate workflow; they are not a prerequisite.'),
('Only now, look at the whole system','Each tool was added to solve a different difficulty. Combining the Global Index and Topic Index is the Double Index System.','For a bag note, go directly from its keyword slip to 1. For the shopping project, go through 2–Shopping to 1, 1b, 15 and 28. Follow branches or cross-references as needed, then return the sheets to ID order.')]
for lang,sections in [('ja',JA),('en',EN)]:
 ja=lang=='ja';T=lambda j,e:j if ja else e
 def note(x,y,id,title,lines=(),w=230,h=130):return card(x,y,w,h,title,lines,id=id)
 figures=[]
 # 0: no indexes and no finished system yet.
 drawing=card(290,20,320,340,T('カバンを買うなら？','Choosing a bag'),[T('軽い物がよい。','Something lightweight.'),T('雨の日にも持ちたい。','Also useful on rainy days.'),T('素材は何がよいだろう。','Which material would work?')],id='1')+txt(290,390,T('今は一枚。まだ探し方には困らない。','One sheet. Finding it is still easy.'),20)
 figures.append(fig(0,lang,T('出発点：一枚のA4ノート','Starting point: one A4 note'),drawing))
 # 1: placement only.
 drawing=note(335,15,'1',T('カバンの調査','Bag investigation'))+note(130,180,'1a',T('素材','Materials'))+note(540,180,'1b',T('購入候補','Candidates'))+note(130,350,'1a1',T('耐久性','Durability'))+edge('M450 145V162H245V178')+edge('M450 162H655V178')+edge('M245 310V348')+txt(405,398,T('深める・広げる・関連する','Develop, extend or relate'),20)
 figures.append(fig(1,lang,T('追加①：内容のつながりに合わせて枝を付ける','Addition 1: branches record relationships'),drawing,510))
 # 2: preserve previous branches, add a distant note and cross references.
 drawing=note(65,25,'1',T('カバンの調査','Bag investigation'),w=230)+note(65,205,'1a',T('素材','Materials'),[T('旅行用品も参照 :27','Travel supplies: :27')],h=150)+note(385,25,'1b',T('購入候補','Candidates'),w=230)+note(65,410,'1a1',T('耐久性','Durability'))+note(605,205,'27',T('旅行用品','Travel supplies'),[T('素材の比較は :1a','Material comparison: :1a')],h=150)
 drawing+=edge('M180 155V203')+edge('M295 90H383')+edge('M180 355V408')+edge('M297 267H603')+edge('M605 313H297',dashed=True)+txt(350,392,T('番号も保管位置も変えない','Keep IDs and filing positions'),18)
 figures.append(fig(2,lang,T('追加②：離れたノートにはIDで参照を足す','Addition 2: cross-reference a distant note'),drawing,565))
 # 3: topic index and heterogeneous branches; no global index.
 drawing=card(20,100,300,270,T('買い物','Shopping'),[T('カバンの調査  1','Bag investigation  1'),T('購入候補  1b','Candidates  1b'),T('靴の調査  15','Shoe research  15'),T('家電の比較  28','Appliance comparison  28')],kind='topic',id='2')
 for y,id,title in [(15,'1',T('カバン','Bags')),(112,'1b',T('購入候補','Candidates')),(209,'15',T('靴','Shoes')),(306,'28',T('家電','Appliances'))]:drawing+=note(440,y,id,title,w=410,h=84)
 for y,target in [(194,57),(221,154),(248,251),(275,348)]:drawing+=edge(f'M320 {y}L438 {target}')
 figures.append(fig(3,lang,T('追加③：Topic Indexでテーマを見渡す','Addition 3: a Topic Index gives an overview'),drawing,420))
 # 4: keyword slips only; full routes are described, not drawn as a full system.
 terms=[T('買い物  → 2','Bags  → 1'),T('カバン  → 1','Shopping  → 2'),T('靴  → 15','Shoes  → 15'),T('旅行用品  → 27','Travel supplies  → 27')]
 drawing=''
 for i,line in enumerate(terms):drawing+=card(150,20+i*92,600,70,line,kind='slip')
 drawing+=txt(150,423,T('一枚に一語。読みの五十音順にリングで管理。','One keyword per slip, filed on a ring.'),20)
 figures.append(fig(4,lang,T('追加④：Global Indexから入口を探す','Addition 4: keyword slips locate entry points'),drawing,455))
 # 5: existing sheets in order, without invented missing sheets.
 drawing=txt(25,40,T('欠番があっても、そのまま置く','Leave gaps; file only existing sheets'),24,'green',700)
 ids=['1','1a','1a1','1c','2','5','5b','12']
 for i,id in enumerate(ids):drawing+=card(25+i*108,105,96,155,'',[],id=id)
 drawing+=txt(30,317,T('手前 → 奥：実在する紙をID順に重ねる','Front → back: existing sheets in ID order'),21)+txt(30,355,T('探すときは索引へ。1bなどの空きを埋める必要はない。','Use indexes to find notes; do not fill gaps just for appearance.'),18)
 figures.append(fig(5,lang,T('運用例：不規則なIDでも保管順は決められる','Working example: irregular IDs, orderly filing'),drawing,390))
 # 6: dot directly above the relevant ID, not at start of the line.
 drawing=card(50,45,370,125,T('買い物','Shopping'),kind='slip')+txt(335,122,'2',25,'blue',700)+'<circle cx="342" cy="92" r="5" fill="#b33a35"/>'
 drawing+=card(50,235,370,125,T('カバン','Bags'),kind='slip')+txt(335,312,'1',25,'blue',700)
 drawing+=card(510,25,340,180,T('買い物','Shopping'),[T('必要になったので索引を作る','Make an index when useful'),T('続きは「2-買い物 2」','More sheets: “2–Shopping 2”')],kind='topic',id='2')+note(510,235,'1',T('カバンの調査','Bag investigation'),[T('本文だけでもよい','A content note is enough')],w=340,h=140)+edge('M422 108H508')+edge('M422 300H508')
 figures.append(fig(6,lang,T('追加⑤：赤い点は「対応するTopic Indexあり」','Addition 5: a red dot means a Topic Index exists'),drawing,405))
 # 7: timeline, no required early category and no new IDs on re-indexing.
 drawing=card(35,25,350,130,T('① まず本文を書く','1. Write the note'),[T('買い物か旅行かは、後で考える','Do not force a category yet')])+card(500,25,350,130,T('② 内容を見てIDを決める','2. Choose an ID'),['1a — '+T('素材','Materials')])
 drawing+=card(35,230,350,150,T('③ 必要な索引に載せる','3. Add useful index entries'),[T('買い物 → 1a','Shopping → 1a'),T('素材 → 1a','Materials → 1a')],kind='topic')+card(500,230,350,150,T('④ 後から関係を足す','4. Add a later connection'),[T('旅行の索引にも → 1a','Travel index → 1a'),T('IDは1aのまま','The ID stays 1a')],kind='topic')
 drawing+=edge('M387 90H498')+edge('M675 157V193H210V228')+edge('M387 300H498')
 figures.append(fig(7,lang,T('追加⑥：書くことと、後から見つけることを分ける','Addition 6: separate writing from later organization'),drawing))
 # 8: paper objects, not an app UI.
 drawing=card(35,40,360,125,T('キーワードの紙片','Keyword slips'),[T('リングで綴じる','Keep on a ring')],kind='slip')+card(500,40,360,125,T('Topic IndexのA4','A4 Topic Index'),[T('キーワードとIDを手書きする','Write keywords and IDs')],kind='topic')+card(35,220,360,140,T('本文のA4','A4 content notes'),[T('文章・図・相手のID','Prose, sketches, reference IDs')])+card(500,220,360,140,T('クリアファイル','Clear folders'),[T('実在する紙をID順に保管','File existing sheets in ID order'),T('日記は別ファイル','Keep diaries separately')])
 figures.append(fig(8,lang,T('紙だけで、すべての役割を実現できる','Every component can be implemented on paper'),drawing,390))
 # 9: all four mechanisms appear together for the first time.
 drawing=card(20,40,240,260,'Global Index',[],kind='group')+card(330,40,240,260,T('買い物','Shopping'),[T('カバン  1','Bags  1'),T('候補  1b','Candidates  1b'),T('靴  15','Shoes  15'),T('家電  28','Appliances  28')],kind='topic',id='2')
 for y in [105,145,185]:drawing+=f'<rect x="32" y="{y-29}" width="216" height="36" rx="3" fill="#f8efd8" stroke="#bcaf8e"/><circle cx="44" cy="{y-8}" r="3" fill="none" stroke="#8b815d"/>'
 for y,word,id in ([(105,'買い物','2'),(145,'カバン','1'),(185,'靴','15')] if ja else [(105,'Bags','1'),(145,'Shopping','2'),(185,'Shoes','15')]):drawing+=txt(60,y,word,18)+txt(215,y,id,20,'blue',700)
 drawing+=f'<circle cx="222" cy="{80 if ja else 120}" r="4" fill="#b33a35"/>'
 drawing+=txt(330,26,'Topic Index',18,'green',700)
 drawing+=note(650,25,'1',T('カバンの調査','Bag investigation'),w=220,h=115)+note(650,195,'1a',T('素材','Materials'),w=220,h=115)+note(650,365,'1a1',T('耐久性','Durability'),w=220,h=115)+note(330,365,'27',T('旅行用品','Travel supplies'),w=240,h=115)
 drawing+=edge('M262 100H328' if ja else 'M262 140H328')+edge('M572 165H610V83H648')+edge('M262 140H290V320H620V83H648' if ja else 'M262 100H294V15H760V23',dashed=True)+edge('M760 142V193')+edge('M760 312V363')+edge('M650 260H610V420H572')+edge('M570 449H615V285H648',dashed=True)
 drawing+=txt(20,350,T('索引から直接本文へも行ける','A slip can lead directly to a note'),16)+txt(20,520,T('読み終えたA4は、クリアファイルのID順へ戻す。日記は別に保管。','Return A4 sheets to their ID order in clear folders. Keep diaries separately.'),18)
 figures.append(fig(9,lang,T('完成図：配置・相互参照・Topic Index・Global Index','Complete picture: placement, cross-references and the two indexes'),drawing,555))
 intro=T('ノートが増えると何に困るのか。カバンの調査を例に、一枚のA4から始め、必要になるたびに道具を足していく。最初から完成形を覚える必要はない。','What becomes difficult as notes accumulate? Start with one A4 sheet about choosing a bag, then add a tool whenever a new problem appears. You do not need to memorize a finished system first.')
 story='<div class="pkm-story" id="why-double-index"><p class="story-lead">'+intro+'</p>'
 md=['# '+T('なぜDouble Index Systemなのか','Why the Double Index System?'),'',intro]
 for i,(title,problem,solution) in enumerate(sections):
  story+=f'<section class="lesson story-step" id="why-step-{i}"><p class="story-kicker">'+(T('出発点','START') if i==0 else T('最後に全体像','THE WHOLE PICTURE') if i==9 else T('問題','PROBLEM')+f' {i:02}')+f'</p><h2>{E(title)}</h2><p class="story-problem">{E(problem)}</p><p><strong>'+T('ここで必要になるもの：','What helps here: ')+f'</strong>{E(solution)}</p>'+figures[i]
  if i==5:story+='<p class="story-rule-note">'+T('欠番を詰めないことや索引を作るタイミングは、この説明で用いる運用例。実例を増やしながら調整できる。','Leaving gaps and deciding when to make an index are working conventions in this example; refine them as you try more cases.')+'</p>'
  if i==6:story+='<p>'+T('赤い点はIDの真上に置く。行頭の●（まとめ・進捗）とは別の意味。索引をまだ作っていないIDには点を付けない。','Place the red dot above the ID. It differs from a leading ● for summary/progress. An ID without a Topic Index has no dot.')+'</p>'
  story+='</section>'
  md+=['',f'## {i}. {title}',problem,'',solution,'',f'![{title}](../../assets/paper-pkm-story/{lang}-{i:02}.svg)']
 story+='</div>'
 p=ROOT/lang/'paper-pkm/index.html';s=p.read_text()
 # Idempotent rebuild: always work from the current revision's archive.
 if 'id="why-double-index"' in s:s=(p.parent/'versions/2026-11-11-before-problem-solution/index.html').read_text().replace('<base href="../../">','',1)
 header=s.index('</header>')+len('</header>');detail=s.index('<section class="lesson"><h3>',header)
 front=s[header:detail]
 benefits=re.search(r'<section aria-labelledby="benefits">.*?</section>',front,re.S).group(0)
 directory=re.search(r'<section class="lesson" id="diagram-directory">.*?</section>',front,re.S).group(0)
 oldmap=re.search(r'<section class="lesson" id="paper-map">.*?</section>',front,re.S).group(0)
 heading=T('書き方と保管の詳しい手順','Detailed writing and filing instructions')
 s=s[:header]+story+f'<h2 id="practical-guide">{heading}</h2><p>'+T('ここからは、実際の記入・参照記法・保管を詳しく確認する。','Continue with the practical details of writing, reference notation and physical filing.')+'</p>'+s[detail:]
 # Prior top-of-page overview is now supplementary material after the practical guide.
 at=s.index('<p><a href="versions/2026-11-11-before-integrated-guides/index.html">')
 s=s[:at]+benefits+directory+oldmap+s[at:]
 s=s.replace('</head>','<link rel="stylesheet" href="../../assets/paper-pkm-story/story.css"></head>',1)
 s=s.replace('https://github.com/Yurii7812/homepage/blob/main/'+lang+'/paper-pkm/guide.md','guide.md')
 # Bring the older dot explanation into line with the latest stated meaning.
 if ja:
  s=s.replace('点を打つのは、二つの条件がそろったとき','赤い点で、Topic Indexの入口を示す')
  s=re.sub(r'<p><strong>一つのキーワードにIDが2つ以上あり、かつ、そのキーワードのトピックIndexを作ったときだけ</strong>.*?</p>','<p><strong>そのIDに対応するTopic Indexを作ったら、IDの真上に赤い点を打つ。</strong>元のIDは消さず、そのまま残す。点は、本文だけでなく索引も開ける入口であることを示す。</p>',s)
  s=s.replace('<tr><td>1つ</td><td>作った</td><td>なし</td></tr>','<tr><td>1つ</td><td>作った</td><td><strong>該当IDの真上</strong></td></tr>')
  s=s.replace('索引に入口IDが一つだけで点がなくても、この並びで両方を見つけられる。','入口IDには対応する索引がある印として点を付け、この並びで本文も見つけられる。')
  s=s.replace('赤い点は、同じキーワードにIDが2つ以上あり、そのキーワードのトピックIndexを作ったときだけ、そのIDの真上。','赤い点は、対応するTopic Indexが存在するIDの真上。')
  s=s.replace('複数IDがある元の行では、専用索引を作ったIDの上に赤い点。単一IDの行には点なし。','元の行では、対応するTopic Indexを作ったIDの上に赤い点。IDの個数ではなく索引の有無を示す。')
 else:
  s=s.replace('Add a dot when both conditions apply','Mark an entry to a Topic Index with a red dot')
  s=re.sub(r'<p><strong>Add a dot only when one keyword lists two or more IDs.*?</p>','<p><strong>When a Topic Index exists for an ID, put a red dot directly above that ID.</strong> Keep the original IDs. The dot tells you that this entry also leads to an index, rather than only to a content note.</p>',s)
  s=s.replace('<tr><td>One</td><td>Made</td><td>None</td></tr>','<tr><td>One</td><td>Made</td><td><strong>Directly above that ID</strong></td></tr>')
  s=s.replace('<p>A keyword with only one ID gets no dot, even if it has an index. A keyword with several IDs gets no dot while its index is still unmade.</p>','<p>The dot depends on the existence of a Topic Index, not the number of IDs listed. An ID without an index has no dot.</p>')
  s=s.replace('You can find both even when the entry lists only one ID and has no dot.','Mark the entry ID with a dot for its index; this filing order also keeps the content note easy to find.')
  s=s.replace('When a keyword lists two or more IDs and has a Topic Index, put a red dot directly above the ID for that index.','When a Topic Index exists for an ID, put a red dot directly above that ID.')
  s=s.replace('An entry with a single ID has no dot.','The dot indicates an existing Topic Index regardless of how many IDs are listed.')
 s=s.replace('キーワードにIDが一つなら、索引があっても点は付けない。IDが複数あっても、まだ索引を作っていなければ点は付けない。','IDの個数ではなく、対応するTopic Indexの有無で点を付ける。まだ索引を作っていないIDには点を付けない。').replace('グローバルIndexを新しい入口のID一つに書き直した場合、その行には点を付けない。','グローバルIndexの入口を変える場合は、新しいIDの真上に点を付け、対応するTopic Indexを示す。').replace('If you rewrite a Global Index slip with only the new entry ID, that row takes no dot.','If you change the entry ID on a Global Index slip, put a dot above the new ID to indicate its Topic Index.').replace('In a multi-ID entry, dot the ID where that index was made. A single-ID entry takes no dot.','Dot the ID where that Topic Index was made, regardless of how many IDs the entry lists.')
 p.write_text(s)
 mdfile=p.parent/'guide.md';original=(p.parent/'versions/2026-11-11-before-problem-solution/guide.md').read_text()
 original=original.replace('点を打つのは、二つの条件がそろったとき','赤い点で、Topic Indexの入口を示す').replace('**一つのキーワードにIDが2つ以上あり、かつ、そのキーワードのトピックIndexを作ったときだけ**','**そのIDに対応するTopic Indexを作ったら**').replace('なし（IDは一つ）','7の真上に赤い点').replace('キーワードにIDが一つなら、索引があっても点は付けない。IDが複数あっても、まだ索引を作っていなければ点は付けない。','IDの個数ではなく、Topic Indexの有無で点を付ける。').replace('グローバルIndexを新しい入口のID一つに書き直した場合、その行には点を付けない。','グローバルIndexの入口を変える場合は、新しいIDの真上に点を付ける。').replace('索引に入口IDが一つだけで点がなくても、この並びで両方を見つけられる。','対応するTopic Indexを示す点をIDの真上に付け、この並びで本文も見つけられる。').replace('赤い点は、同じキーワードにIDが2つ以上あり、そのキーワードのトピックIndexを作ったときだけ、そのIDの真上。','赤い点は、対応するTopic Indexが存在するIDの真上。').replace('複数IDがある元の行では、専用索引を作ったIDの上に赤い点。単一IDの行には点なし。','対応するTopic Indexを作ったIDの上に赤い点。')
 original=original.replace('Add a dot when both conditions apply','Mark an entry to a Topic Index with a red dot').replace('**Add a dot only when one keyword lists two or more IDs and you have made a Topic Index for that keyword.**','**Put a dot above an ID when its Topic Index exists.**').replace('None (only one ID)','Above 7').replace('None (one ID)','Above 7').replace('A keyword with only one ID gets no dot, even if it has an index. A keyword with several IDs gets no dot while its index is still unmade.','The dot indicates an existing Topic Index, regardless of the number of IDs.').replace('If you rewrite a Global Index slip with only the new entry ID, that row takes no dot.','If you change the entry ID, dot the new ID to indicate its Topic Index.').replace('You can find both even when the entry lists only one ID and has no dot.','Dot the entry ID for its Topic Index; the filing order keeps the content note nearby.').replace('When a keyword lists two or more IDs and has a Topic Index, put a red dot directly above the ID for that index.','When a Topic Index exists for an ID, put a red dot directly above that ID.').replace('In a multi-ID entry, dot the ID where that index was made. A single-ID entry takes no dot.','Dot the ID where the Topic Index was made, regardless of how many IDs are listed.')
 mdfile.write_text('\n'.join(md)+'\n\n---\n\n## '+heading+'\n\n'+original)
