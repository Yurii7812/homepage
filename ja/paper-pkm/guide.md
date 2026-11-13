# 図でわかる 紙の知識管理術

<div id="benefits"></div>

分類を決める前に、まず書く。内容の関係に応じてノートにIDを付け、グローバルインデックスとトピックインデックスから探す。紙だけで使えるダブルインデックス方式の実践ガイドです。A4に長い考察や途中の思考をそのまま残せます。アトミックノートに分ける必要はありません。

**目次**

- [まず書き、IDを付ける](#step-1)

- [ノート同士を矢印で結ぶ](#step-2)

- [小型メモ帳を持ち歩く](#step-3)

- [トピックインデックスを作る](#step-4)

- [上位トピックを後から追加する](#step-5)

- [本ごとに書き、共通の索引で結ぶ](#step-6)

- [大きく発展した枝を独立させる](#step-7)

- [グローバルインデックスを作り、分割する](#step-8)

- [保管して探す](#step-9)

- [早見表](#step-10)


<div id="step-1"></div><div id="branch-layout"></div><div id="folgezettel-tree"></div><div id="infinite-id-tree"></div>


## 1. まず書き、IDを付ける

A4を縦に置き、左上を空けて青で自由に書きます。日付を右上に書いても便利です。内容を書いてから既存のノートとの関係を考え、左上にその紙自身のIDを青で書きます。長い文章、図、箇条書き、途中の考えをそのまま残して構いません。


<figure><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">1</span></div>算数について考える<br>分数 …<br>掛け算 …</div><div class="sheet small"><div class="sheet-title"><span class="own">1a</span></div>分数を理解する …</div></div><figcaption>左上にその紙自身のIDを青で書きます。</figcaption></figure>


IDは書いた順番ではなく、関連する、広げる、深めるという内容上の関係で決めます。例えば次のように分岐します。関連があるからといってすべてを一つの枝に押し込む必要はありません。


<figure><ul class="tree"><li><span>1</span> 算数について考える<ul><li><span>1a</span> 分数を理解する</li><li><span>1b</span> 分数から割合へ広げる</li><li><span>1c</span> 掛け算を考える<ul><li><span>1c1</span> 掛け算の意味を深める</li><li><span>1c2</span> 掛け算の図を考える</li><li><span>1c3</span> 掛け算を応用する</li></ul></li></ul></li></ul><figcaption>1c1〜1c3は1cに関係する別の発展。単に書いた順番だけで枝を深くしません。</figcaption></figure>



<div id="step-2"></div><div id="reference-ink"></div>


## 2. ノート同士を矢印で結ぶ

本文中の参照先IDと矢印は赤で書きます。`->1a` は現在の文章の続きが1aにあること、`1a->` は1aの続きが現在の文章にあることを示します。複数の続きは `->1a, 2, 3` と書けます。


<figure><div class="sheets"><div class="sheet"><div class="sheet-title"><span class="own">1</span></div>分数の考え方。 <span class="ref">-&gt;1a</span></div><div class="sheet"><div class="sheet-title"><span class="own">1a</span></div><span class="ref">1-&gt;</span> 分数の考え方の続き。</div></div><figcaption>左の1から右の1aへ続きます。両方に記せば、どちらから読んでもつながりが分かります。</figcaption></figure>


`(1)`、`(2)` は文章中の特定箇所を示す位置番号で、ノートIDとは別です。元の箇所の番号には赤い下線を引きます。特定箇所を指す必要があれば `->2(3)` のように書けますが、普段は矢印とIDだけで十分です。


<figure><div class="sheets"><div class="sheet"><div class="sheet-title"><span class="own">1</span></div>続きの位置 <span class="ref">-&gt;2(3)</span></div><div class="sheet"><div class="sheet-title"><span class="own">2</span></div><span class="ref">1-&gt;</span> 続きの文章 <span class="underline">(3)</span></div></div><figcaption>赤い下線の(3)は位置番号。必要なときだけIDと組み合わせます。</figcaption></figure>



<div id="step-3"></div>


## 3. 小型メモ帳を持ち歩く

小さな紙のメモ帳を持ち歩き、思いつきを順番に書きます。新しいページに書き始めるたび、自分でページ番号を記入します。このメモ帳ではページ番号がリンク用のIDです。必要なら位置番号も使えます。内容は後で正式なA4ノートへ移せます。メモ帳は捨てることがあるので、正式なノートからメモ帳への戻り参照は原則作りません。


<figure><div class="notebook"><div class="sheet"><div class="sheet-title"><span class="own">ページ 1</span></div>思いつきの続きは <span class="ref">-&gt;2</span></div><div class="sheet"><div class="sheet-title"><span class="own">ページ 2</span></div>別の考えを書き留める。 <span class="ref">-&gt;3</span></div></div><div class="notebook"><div class="sheet"><div class="sheet-title"><span class="own">ページ 3</span></div><span class="ref">2-&gt;</span> 2ページからの続き。</div><div class="sheet"><div class="sheet-title"><span class="own">ページ 4</span></div>さらに考えたこと。</div></div><figcaption>1ページの ->2 は続きの行き先。3ページの 2-> は、その文章が2ページからの続きである印です。ページ番号とFolgezettel IDは別です。</figcaption></figure>



<div id="step-4"></div><div id="evolving-topic-index"></div>


## 4. トピックインデックスを作る

ノートがたまって探しにくくなったら、A4にトピックインデックスを作ります。左上に基点となる通常ノートIDとハイフン付き番号を書き、本文にキーワードと参照先IDを記入します。キーワードは青、参照先IDは赤です。粒度は実際のノートを見て決め、必要のない索引は作りません。

`1-1` は通常ノート1を基点とする最初のインデックス、`1-2` は同じ基点の別のインデックスです。`1c-1` は通常ノート1cを基点とします。基点ひとつにつき複数作れます。索引が複数ページになる場合は、同じインデックスIDにページ番号を添えて区別します。


<figure><div class="sheets"><div class="sheet"><div class="sheet-title"><span class="own">1-1 算数</span></div>分数 <span class="ref">1a</span><br>掛け算 <span class="ref">1c</span></div><div class="sheet"><div class="sheet-title"><span class="own">1-2 算数の応用</span></div>応用 <span class="ref">1c3</span></div><div class="sheet"><div class="sheet-title"><span class="own">1c-1 掛け算</span></div>意味 <span class="ref">1c1</span><br>図 <span class="ref">1c2</span></div></div><figcaption>左上のインデックス自身のIDは青。索引内の参照先IDは赤。</figcaption></figure>



<div id="step-5"></div>


## 5. 上位トピックを後から追加する

最初から「宗教」のような広い分類を作る必要はありません。仏教の本を読み、ノートが増えたら仏教の索引を作り、さらに必要になれば宗教の索引を後から追加できます。上位を参照するときは赤い `↑` を使い、直接の上位インデックスを記します。下位の項目には原則として特別な記号は不要です。関連するインデックスを近くに保管できます。


<figure><div class="diagram-stage">① まず書く</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">1</span></div>仏教の本A</div></div><div class="diagram-stage">② 必要になって索引を作る</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">1-1 仏教の本A</span></div>無我：本A <span class="ref">1a</span></div><div class="sheet small"><div class="sheet-title"><span class="own">1-2 仏教</span></div>仏教の本A <span class="ref">1-1</span></div></div><div class="diagram-stage">③ 上位が必要になったら追加</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">1-2 仏教</span></div><span class="ref">↑</span> 宗教 <span class="ref">1-3</span><br>仏教の本A <span class="ref">1-1</span></div><div class="sheet small"><div class="sheet-title"><span class="own">1-3 宗教</span></div>仏教 <span class="ref">1-2</span></div></div><figcaption>本Aから始め、仏教、宗教の順に必要に応じて追加した例。索引名は出発点であり、内容を縛る分類ではありません。</figcaption></figure>



<div id="step-6"></div>


## 6. 本ごとに書き、共通の索引で結ぶ

異なる本は原則として別のFolgezettel系列から始めます。本Aを1、本Bを2から始めれば、内容が関連していても両者を同じ枝に押し込む必要はありません。仏教全般のインデックスには両方の系列のノートを登録できます。


<figure><div class="sheets"><div class="sheet"><div class="sheet-title"><span class="own">1 仏教の本A</span></div><span class="ref">1a</span> 無我：本A<br><span class="ref">1b</span> 比較</div><div class="sheet"><div class="sheet-title"><span class="own">1-1 仏教の本A</span></div>無我：本A <span class="ref">1a</span></div><div class="sheet"><div class="sheet-title"><span class="own">1-2 共通の仏教索引</span></div>無我：本A <span class="ref">1a</span><br>無我：本B <span class="ref">2a</span></div><div class="sheet"><div class="sheet-title"><span class="own">2-1 仏教の本B</span></div>無我：本B <span class="ref">2a</span></div><div class="sheet"><div class="sheet-title"><span class="own">2 仏教の本B</span></div><span class="ref">2a</span> 無我：本B<br><span class="ref">2b</span> 比較</div></div><figcaption>本ごとの系列は別々のまま、共通のトピックインデックスから両方を探せます。</figcaption></figure>



<div id="step-7"></div>


## 7. 大きく発展した枝を独立させる

枝が大きく発展し、専門化・高度化したら、新しい独立したIDを作れます。例えば掛け算の1cから2を新設し、その後は主に2、2a、2bへ書きます。1cとその既存ノートは削除も移動もしません。


<figure><div class="diagram-stage">① 独立前：元の系列</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">1c 掛け算</span></div><span class="ref">1c1</span> 意味<br><span class="ref">1c2</span> 図</div></div><div class="diagram-stage">② 独立後：新しい系列を追加</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">1c 掛け算</span></div>元のノートは残る<br><span class="ref">1c1</span>, <span class="ref">1c2</span></div><div class="sheet small"><div class="sheet-title"><span class="own">2 掛け算</span></div>以後の記録 <span class="ref">2a</span>, <span class="ref">2b</span></div></div><div class="diagram-stage">③ 3枚のトピックインデックス</div><div class="sheets"><div class="sheet"><div class="sheet-title"><span class="own">1-1 算数</span></div>掛け算 <span class="ref">1c</span>, <span class="ref dot">2</span></div><div class="sheet"><div class="sheet-title"><span class="own">1c-1 掛け算</span></div><span class="ref">↳</span> 掛け算 <span class="ref">2</span></div><div class="sheet"><div class="sheet-title"><span class="own">2-1 掛け算</span></div><span class="ref">↰</span> 掛け算 <span class="ref">1c</span></div></div><figcaption>1c系列は元の位置に残ります。親の1-1には両方のIDを、1c-1には独立先を、2-1には独立元を記します。点と矢印は赤です。</figcaption></figure>



<div id="step-8"></div>


## 8. グローバルインデックスを作り、分割する

グローバルインデックスは、A4用紙にキーワードと対応するIDを書いた全体の入口です。左上に担当する文字範囲を青で書き、キーワードを五十音順に並べ、参照先IDを赤で記します。英語のキーワードはアルファベット順に管理します。独立して発展したIDの上には赤い点を付けます。

1枚がいっぱいになったら、まず登録済みの言葉をすべて読みの五十音順に並べます。その実際の並びを、件数がおおむね均等になるよう4組に分け、それぞれを新しいA4索引に写します。境界は各組の先頭の言葉から決め、左上に担当範囲を書きます。言葉を機械的に文字種で等分する必要はありません。たとえば「掛け算・記録｜工夫・計算｜言葉・宗教｜仏教・分数」と分けたら、2枚目は「工夫から言葉の前まで」です。

境界に書いた言葉そのものは、その言葉から始まる索引に入れます。その直前の言葉までは前の索引です。最初の索引は先頭の言葉より前、最後の索引は末尾より後に新しい言葉が来ても担当します。範囲の境界は重複も空白も生じません。各紙に書き足す余白を残し、途中に入る言葉は空欄に書くか、順番が崩れるときはその範囲を書き直します。別の範囲は書き直しません。

いずれかの範囲がいっぱいになったら、その範囲の言葉を再び順に並べて4組にし、その範囲だけを4枚に分けます。再分割した4枚は元の範囲の上限・下限を引き継ぎます。写し終えたら件数・順序・IDを確認します。これは索引の範囲の分割で、A4用紙を裁断するのではありません。


<figure><div class="diagram-stage">① いっぱいになった1枚</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">あ〜ん</span></div>掛け算 <span class="ref">1c</span>, <span class="ref dot">2</span><br>記録 <span class="ref">1</span><br>工夫 <span class="ref">1a</span><br>計算 <span class="ref">1c1</span><br>言葉 <span class="ref">2a</span><br>宗教 <span class="ref">1-3</span><br>仏教 <span class="ref">1-2</span><br>分数 <span class="ref">1a</span></div></div><div class="diagram-stage">② 分布に合わせて4範囲へ</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">最初〜工夫の前</span></div>掛け算 <span class="ref">1c</span>, <span class="ref dot">2</span><br>記録 <span class="ref">1</span></div><div class="sheet small"><div class="sheet-title"><span class="own">工夫〜言葉の前</span></div>工夫 <span class="ref">1a</span><br>計算 <span class="ref">1c1</span></div><div class="sheet small"><div class="sheet-title"><span class="own">言葉〜仏教の前</span></div>言葉 <span class="ref">2a</span><br>宗教 <span class="ref">1-3</span></div><div class="sheet small"><div class="sheet-title"><span class="own">仏教〜最後</span></div>仏教 <span class="ref">1-2</span><br>分数 <span class="ref">1a</span></div></div><div class="diagram-stage">③ 満杯の範囲だけ再び4分割</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">工夫〜計画の前</span></div>工夫 <span class="ref">1a</span></div><div class="sheet small"><div class="sheet-title"><span class="own">計画〜経験の前</span></div>計画 <span class="ref">1b</span></div><div class="sheet small"><div class="sheet-title"><span class="own">経験〜計算の前</span></div>経験 <span class="ref">2a</span></div><div class="sheet small"><div class="sheet-title"><span class="own">計算〜言葉の前</span></div>計算 <span class="ref">1c1</span></div></div><div class="diagram-stage">ほかの3枚はそのまま</div><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">最初〜工夫の前</span></div>…</div><div class="sheet small"><div class="sheet-title"><span class="own">言葉〜仏教の前</span></div>…</div><div class="sheet small"><div class="sheet-title"><span class="own">仏教〜最後</span></div>…</div></div><figcaption>実際の言葉を順に並べて4組にし、各組の先頭の言葉を境界にします。③では2枚目だけを4枚に再編し、ほかの3枚はそのままです。図では再分割までに計画・経験が追加されています。</figcaption></figure>



<div id="step-9"></div><div id="filing-stack"></div>


## 9. 保管して探す

通常ノートはFolgezettel順にA4クリアファイルへ保管します。例えば 1、1a、1b、1c、1c1、2、2a の順です。量が増えたらファイルを分け、必要に応じてID付きの付箋を目印にします。トピックインデックスは関連するものを近くにまとめ、見つけやすくします。日記は日付を左上に書き、別のクリアファイルに保管します。


<figure><div class="sheets"><div class="sheet small"><div class="sheet-title"><span class="own">通常ノート</span></div><span class="ref">1</span> <span class="ref">→</span> <span class="ref">1a</span> <span class="ref">→</span> <span class="ref">1b</span><br><span class="ref">1c</span> <span class="ref">→</span> <span class="ref">1c1</span> <span class="ref">→</span> <span class="ref">2</span></div><div class="sheet small"><div class="sheet-title"><span class="own">トピックインデックス</span></div><span class="ref">1-1</span><br><span class="ref">1-2</span><br><span class="ref">1c-1</span><br><span class="ref">2-1</span></div><div class="sheet small"><div class="sheet-title"><span class="own">日記・別ファイル</span></div>2026 11 13</div></div><figcaption>通常ノートはID順に、日記は別のクリアファイルへ。</figcaption></figure>


探すときは、グローバルインデックスでキーワードを探し、記されたIDからノートまたはトピックインデックスへ進みます。トピックインデックスから個別のノートを探し、必要に応じて矢印で続きへ進みます。


<div id="step-10"></div>


## 10. 早見表

| | |
|---|---|

| 通常ノート | A4に自由に書き、内容の関係でIDを決める。 |

| 索引のID | 基点ID-番号。1-1、1-2、1c-1、2-1。基点ごとに複数可。 |

| 索引を作る時 | 書き進めて必要になった時。 |

| グローバル索引 | A4に五十音順。満杯の範囲を分布に応じて4分割。 |

| 赤い点 | 独立して発展したIDの上に付ける。 |

| ↑ | 直接の上位トピックインデックス。 |

| ↳ / ↰ | 独立先 / 独立元。一般的な関連とは区別する。 |

| ☆ | 一般的な関連。一筆書きの星。 |

| ○ | まとめ・進捗など。例：○ まとめ 1a、○ 進捗 1b。 |

| ->ID / ID-> | 現在の文章から続きへ / 指定IDから現在の文章へ。 |

| (n) | 位置番号。元の番号に赤い下線。必要なときだけ位置指定。 |

| 青 / 赤 | 本文・キーワード・左上のその紙自身のIDは青。参照先IDと索引用記号は赤。 |

| 携帯メモ | ページ番号をリンクIDにする。一時的で、正式ノートから原則参照しない。 |

| 保管 | A4クリアファイル。日記は別ファイル。 |

紙とペンだけで始められます。まず1枚書き、必要になった索引から育ててください。


## 旧版

- [2026年11月13日更新前](versions/2026-11-13-v1/index.html)
- [2026年11月11日更新前](versions/2026-11-11-before-update/index.html)
