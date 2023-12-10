{page_header}

この章では，SFGPLを学ぶための基本的知識や文法を説明する．
特に，現在形の肯定形の基本的な文について説明する．

また前提として[aboutSFGPL]({docs_aboutSFGPL})を読んでおくことを推奨する．
さらにこの資料の全体として，例文等は英語を元に作成しているため，少し英語が分かること（中学卒業程度）が望ましい．

## SFGPL文構造の特徴について

SFGPLでは英語と同様に，SOV型で語の役割が位置で決まる言語である．
また，SFGPLの最大の特徴として，[文型]({docs_sentence_pattern})が重視されていることが挙げられる．
この文型は，それぞれどのような引数（どのような品詞の単語）を何個とるかが定義されている．
そのため，文の意味が一意に決まる．
また，この文型を決定する機能語が文（句）の先頭に付属する．
そして，この文（句）全体では，名詞としてみなされ，入れ子的に文を作ることができる（[複文]({docs_CompoundSentences})）．

## SFGPLの文型の具体例

### {noun_do}による構文

まず，```{noun_do}```を使用した例を提示する．
この```{noun_do}```では，2つの引数を持ち，第一引数が文の主語，第二引数が文の動詞を表す．
つまり，```{noun_do}```では，英語の第一文型SVと同等の文を作ることができる．

例としてSFGPLで"I run."を表すには次のようにする．

```SFGPL
{I_run}
```

このとき，```{noun_do}```は，文型が"SV"のときに付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

そして，```{run}```は，動詞"run"を表す．
この```{run}```は2単語から構成されている．
このような借用語などでは，品詞を表す語（この場合は動詞を表す，```{verb_init}```）が付いている．
このような品詞を表す語は，次の3つが存在する．

||SFGPL|
|:-:|:-:|
|名詞|{noun_init}|
|動詞|{verb_init}|
|修飾語|{modifier_init}|

### {noun_eq}による構文

次に，```{noun_eq}```を使用した例を提示する．
この```{noun_eq}```は3つの引数を持ち，第一引数が文の主語，第二引数が文の動詞，第三引数が主語に対する補語を表す．
また，第三引数の補語は名詞でないといけない．
つまり```{noun_eq}```では，英語の第二文型SVCと同等の文を作ることができる．

例としてSFGPLで"I am a student."を表すには次のようにする．

```SFGPL
{I_am_a_student}
```

このとき，```{noun_eq}```は，文型が"SVC"のときに付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

次に，```{verb_none}```は，動詞が無意味であることを示す単語である．
この```{verb_none}```では，場所によって意味が変わる．
このとき例文のときは，英語のbe動詞と同等の意味となる．

そして，```{student}```は，名詞"student"を表す．
このとき，英語などにある冠詞はSFGPLでは存在しないため，何もつけなくても良い．

### {noun_haveP}による構文

次に，```{noun_haveP}```を使用した例を提示する．
この```{noun_haveP}```は3つの引数を持ち，第一引数が文の主語，第二引数が文の動詞，第三引数が主語に対する補語を表す．
また，第三引数の補語は修飾語でないといけない．
つまり```{noun_haveP}```では，英語の第二文型SVCと同等の文を作ることができる．

例としてSFGPLで"I am happy."を表すには次のようにする．

```SFGPL
{I_am_happy}
```

このとき，```{noun_haveP}```は，文型が"SVC"のときに付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

次に，```{verb_none}```は，動詞が無意味であることを示す単語である．
この```{verb_none}```では，場所によって意味が変わる．
このとき例文のときは，英語のbe動詞と同等の意味となる．

そして，```{happy}```は，修飾語"happy"を表す．

### {noun_doT}による構文

そして，```{noun_doT}```を使用した例を提示する．
この```{noun_doT}```は3つの引数を持ち，第一引数が文の主語，第二引数が文の動詞，第三引数が目的語を表す．
つまり，```{noun_doT}```では，英語の第三文型のSVOと同等の文を作ることができる．

例としてSFGPLで"I open the door."を表すには次のようにする．

```SFGPL
{I_open_the_door}
```

このとき，```{noun_doT}```は，文型が"SVO"のときに付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

次に，```{open}```は，動詞"open"を表す．

そして，```{door}```は，名詞"door"を表す．

### {noun_give}による構文

次に，```{noun_give}```を使用した例を提示する．
この```{noun_give}```は4つの引数を持ち，第一引数が文の主語，第二引数が文の動詞，第三引数が間接目的語，第四引数が直接目的語を表す．
つまり，```{noun_give}```では，英語の第四文型のSVOOと同等の文を作ることができる．

例としてSFGPLで"I give you a box."を表すには次のようにする．

```SFGPL
{I_give_you_a_box}
```

このとき，```{noun_give}```は，文型が"SVOO"のときに付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

次に，```{verb_none}```は，動詞が無意味であることを示す単語である．
この```{verb_none}```では，場所によって意味が変わる．
このとき例文のときは，英語のgiveと同等の意味となる．

そして，```{you}```は，二人称代名詞"you"を表す．

さらに，```{box}```は，名詞"box"を表す．

### {noun_makeN}による構文

次に，```{noun_makeN}```を使用した例を提示する．
この```{noun_makeN}```は4つの引数を持ち，第一引数が文の主語，第二引数が文の動詞，第三引数が目的語，第四引数が目的語に対する補語を表す．
第四引数の補語は名詞でないといけない．
つまり，```{noun_makeN}```では，英語の第四文型のSVOCと同等の文を作ることができる．

例としてSFGPLで"I make you a teacher."を表すには次のようにする．

```SFGPL
{I_make_you_a_teacher}
```

このとき，```{noun_makeN}```は，文型が"SVOC"のときに付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

次に，```{verb_none}```は，動詞が無意味であることを示す単語である．
この```{verb_none}```では，場所によって意味が変わる．
このとき例文のときは，英語で使役動詞のmakeと同等の意味となる．

そして，```{you}```は，二人称代名詞"you"を表す．

さらに，```{teacher}```は，名詞"teacher"を表す．

### {noun_makeM}による構文

次に，```{noun_makeM}```を使用した例を提示する．
この```{noun_makeM}```は4つの引数を持ち，第一引数が文の主語，第二引数が文の動詞，第三引数が目的語，第四引数が目的語に対する補語を表す．
第四引数の補語は修飾語でないといけない．
つまり，```{noun_makeM}```では，英語の第四文型のSVOCと同等の文を作ることができる．

例としてSFGPLで"I make you happy."を表すには次のようにする．

```SFGPL
{I_make_you_happy}
```

このとき，```{noun_makeM}```は，文型が"SVOC"のときに付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

次に，```{verb_none}```は，動詞が無意味であることを示す単語である．
この```{verb_none}```では，場所によって意味が変わる．
このとき例文のときは，英語で使役動詞のmakeと同等の意味となる．

そして，```{you}```は，二人称代名詞"you"を表す．

さらに，```{happy}```は，修飾語"happy"を表す．

### {noun_have}による構文

次に，```{noun_have}```を使用した例を提示する．
この```{noun_have}```は3つの引数を持ち，第一引数が文の主語（持ち主），第二引数が文の動詞，第三引数が目的語（持ち物）を表す．
そのため```{noun_have}```では"S has O"という文を表すことができる．

例としてSFGPLで"I have a box."を表すには次のようにする．

```SFGPL
{I_have_a_box}
```

このとき，```{noun_have}```は，所有を表す文を作る際に付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

次に，```{verb_none}```は，動詞が無意味であることを示す単語である．
この```{verb_none}```では，場所によって意味が変わる．
このとき例文のときは，英語でhaveと同等の意味となる．

さらに，```{box}```は，名詞"box"を表す．

### {noun_belong}による構文

次に，```{noun_belong}```を使用した例を提示する．
この```{noun_belong}```は3つの引数を持ち，第一引数が文の主語（所属している人や物），第二引数が文の動詞，第三引数が目的語（所属先）を表す．
そのため```{noun_belong}```では"S belongs to O"という文を表すことができる．

例としてSFGPLで"I belong to a school."を表すには次のようにする．

```SFGPL
{I_belong_to_a_school}
```

このとき，```{noun_belong}```は，所属していることを表す文を作る際に付ける語である．

また，```{I}```は，一人称代名詞"I"を表す．

次に，```{verb_none}```は，動詞が無意味であることを示す単語である．
この```{verb_none}```では，場所によって意味が変わる．
このとき例文のときは，英語で"belong to"と同等の意味となる．

さらに，```{school}```は，名詞"school"を表す．

### その他の構文

その他の構文は，[文型]({docs_sentence_pattern})で示されている．

## 修飾方法

### 名詞の修飾方法

名詞の修飾方法としては，主に，修飾語を用いる方法と名詞を用いる方法の2種類が存在する．

#### 名詞に対して修飾語で修飾する方法

たとえば，ある箱に対してそれが大きいことを表すとき，英語では"The box is big."と表す．
同様にSFGPLでもSVCを表す```{noun_haveP}```を用いて，次のように表せる．

```SFGPL
{the_box_is_big}
```

このとき，```{big}```は大きいという意味である．

#### 名詞に対して名詞で修飾する方法

この方法は，英語の前置詞"of"や日本語の助詞"の"を使用するような場面で使われる．
しかし，SFGPLでは簡潔に記すことができず，このような場合でも英語の関係代名詞のような文によって修飾する（[複文]({docs_CompoundSentences})）．

例えば，"My box is big."を表すには，次のような文で表す．

```SFGPL
{my_box_is_big}
```

この文では，主文の主語に```{I_have_a___box_}```という文が入れ子的に入っている．
この```{I_have_a___box_}```は"I have a box."という意味であり，それが主語であることを示している．
また，特にその文の中で重要な語を```{determinerN_stressed}```を使うことで強調することができる．
そのため，この文では```{stressed_box}```で"box"を強調している．

総合的に，直訳すると"[I have a **box**] is big."という意味になり，結果的に"My box is big."と同じ意味になる．

### 動詞の修飾方法

#### 単純な動詞の修飾方法

動詞の修飾方法は，```{verb_add}```を使用して，修飾できる．
この```{verb_add}```では第一引数が動詞，第二引数が修飾語となる．

例えば，"I quickly run."を表すには，次のようにする．

```SFGPL
{I_quickly_run}
```

このとき，```{quickly}```は"quickly"という意味である．
また，```{run_quickly}```では"quickly run"という意味で，動詞の"run"を修飾語の"quickly"で修飾している．

#### 名詞句を修飾語に変換し動詞を修飾する方法

SFGPLではある名詞句を修飾語に変換し，それを動詞を修飾することができる．
これは，英語の前置詞を用いた副詞化と同様の方法である．

まず，SFGPLには，[品詞間の変換ができる語]({docs_partOfSpeechConversion})があり，この場合では，名詞から修飾語に変換する```{modifier_N2M}```が使われる．
またこの用法では，```{modifier_N2M}```と並行して，名詞句の意味を限定する[名詞限定詞]({docs_DeterminerN})が使われ，意味の限定が行われる．

例えば，"I go to Tokyo."をSFGPLで表すには次のようにする．

```SFGPL
{I_go_to_Tokyo}
```

まず，```{go}```は英語の"go"を表していて，そしてその行き先は動詞を修飾することで表される．
特に，```{to_Tokyo}```の4語で"to Tokyo"を表す．
その中の```{modifier_N2M}```が名詞から修飾語に変換する語，```{determinerN_place}```は場所を表す名詞限定詞である．
その2語と場所を表す```{Tokyo}```（東京）を組み合わせることで，"to Tokyo"という意味を表している．

### 修飾詞の修飾方法

修飾詞の修飾方法は，```{modifier_add}```を使用して表現する．
この```{modifier_add}```では第一引数の修飾語に対して第二引数の修飾語が修飾する．

例えば，SFGPLで"Your box is a little big."を表すには次のようにする．

```SFGPL
{Your_box_is_a_little_big}
```

このとき，```{big}```(= "big")に```{a_little}```(= "a little")が修飾しているため，この```{a_little_big}```では"a little big"という意味となる．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|run|{run}|
|student|{student}|
|happy|{happy}|
|open|{open}|
|door|{door}|
|you|{you}|
|box|{box}|
|teacher|{teacher}|
|school|{school}|
|big|{big}|
|quickly|{quickly}|
|go|{go}|
|Tokyo|{Tokyo}|
|a little|{a_little}|