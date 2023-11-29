{page_header}

## SFGPLの文型の一覧

SFGPLでは，文を構成するためには，必ず文型を決定する機能語が文の先頭に付属する．
SFGPLでは以下の表のような文型が存在し，それらの文の組み合わせにより，文自体が構成される．また，単語の修飾なども行われる．

|||単語|関数|引数|補足|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|S V|{noun_do}|Noun.do|S,V||
|2|S V C|{noun_eq}|Noun.eq|S,V,C|Cが名詞|
|2|S V C|{noun_haveP}|Noun.haveP|S,V,C|Cが修飾語|
|3|S V O|{noun_doT}|Noun.doT|S,V,O||
|4|S V O1 O2|{noun_give}|Noun.give|S,V,O1,O2||
|5|S V O C|{noun_makeN}|Noun.makeN|S,V,O,C|Cが名詞|
|5|S V O C|{noun_makeM}|Noun.makeM|S,V,O,C|Cが修飾語|
|-|A has B|{noun_have}|Noun.have|A,V,B|AがBを所有している|
|-|A belongs to B|{noun_belong}|Noun.belong|A,V,B|AがBに所属している|
|-|A is more B than C|{noun_gt}|Noun.gt|A,V,B,C|AがCよりBである|
|-|According to C, A V B|{noun_hearSay}|Noun.hearSay|A,V,B,C|Bという内容をCという情報源から，AはFする|

## Noun.do

Noun.do ```{noun_do}```では，特に，英語の第一文型と同じ形のSが主語，Vが動詞で，主語が何かの動作をするという．単純な文章を表すことができる．
"I run."をSFGPLで表すには，次のようになる．

```SFGPL
{I_run}
```

## Noun.eq

Noun.eq ```{noun_eq}```では，特に，英語の第二文型である"S is C"に相当し，その中でも，補語Cが名詞であるものを表す表すことができる．
また，この構文ではSとCが等価であることも示している．
Vが英語でbe動詞に相当する場合，動詞として```{verb_none}```を使用する．
"This is a table."をSFGPLで表すには，次のようになる．

```SFGPL
{this_is_a_table}
```

"You become a teacher."をSFGPLで表すには，次のようになる．

```SFGPL
{you_become_a_teacher}
```

## Noun.haveP

Noun.haveP ```{noun_haveP}```では，特に，英語の第二文型である"S is C"に相当し，その中でも，補語Cが修飾語であるものを表す表すことができる．
また，この構文ではSがCという性質や状態であるということを表す．
Vが英語でbe動詞に相当する場合，動詞として```{verb_none}```を使用する．
"The table is red."をSFGPLで表すには，次のようになる．

```SFGPL
{the_table_is_red}
```

"You look sad."をSFGPLで表すには，次のようになる．

```SFGPL
{you_look_sad}
```

## Noun.doT

Noun.doT ```{noun_doT}```では，特に，英語の第三文型に相当し，Sが主語，Vが動詞，Oが目的語である．
"I study English."をSFGPLで表すには，次のようになる．

```SFGPL
{I_study_English}
```

## Noun.give

Noun.give ```{noun_give}```では，特に，英語の第四文型に相当し，Sが主語，Vが動詞，O1とO2が目的語である．特に，この構文では，SがO1にO2をVするという意味となる．
Vが英語で"give"に相当する場合，動詞として```{verb_none}```を使用する．
"I give you a table."をSFGPLで表すには，次のようになる．

```SFGPL
{I_give_you_a_table}
```

## Noun.makeNとNoun.makeM

Noun.makeN ```{noun_makeN}```とNoun.makeM ```{noun_makeM}```では，特に，英語の第五文型に相当し，Sが主語，Vが動詞，Oが目的語，Cが補語である．
Noun.makeNはCが名詞，Noun.makeMはCが修飾語のときに使用する．
この構文では"SがOをCにさせる"という意味になる．
Vが英語で"make"に相当する場合，動詞として```{verb_none}```を使用する．

"I make you a teacher."をSFGPLで表すには，次のようになる．

```SFGPL
{I_make_you_a_teacher}
```

"I make you sad."をSFGPLで表すには，次のようになる．

```SFGPL
{I_make_you_sad}
```

## Noun.have

Noun.have ```{noun_have}```は"AがBを所有している"という意味になる．
Vが英語で"have"に相当する場合，動詞として```{verb_none}```を使用する．
"I have a table."をSFGPLで表すには，次のようになる．

```SFGPL
{I_have_a_table}
```

## Noun.belong

Noun.belong ```{noun_belong}```は"AがBに所属している"という意味になる．
Vが英語で"belong to"に相当する場合，動詞として```{verb_none}```を使用する．
"I belong to a school."をSFGPLで表すには，次のようになる．

```SFGPL
{I_belong_to_a_school}
```

## Noun.gt

Noun.gt ```{noun_gt}```は"AはCよりBである"という意味になる．
このときAとBが比較対象の名詞，Cは修飾語である．
Vが英語でbe動詞に相当する場合，動詞として```{verb_none}```を使用する．
"The bed is bigger than yours."をSFGPLで表すには，次のようになる．

```SFGPL
{The_bed_is_bigger_than_yours}
```

## Noun.hearSay

Noun.hearSay ```{noun_hearSay}```は"Bという内容をCという情報源から，AはVする"という意味になる．
このとき，Aは情報を受け取った人や物，Vは動詞，Bは情報の内容，Cは情報源の人や物である．
Vが英語でhear，sayやseeなどの伝聞に関する動詞に相当する場合，動詞として```{verb_none}```を使用する．
"According to the book, I saw that Japan is located in East Asia."をSFGPLで表すには，次のようになる．

```SFGPL
{According_to_the_book_I_saw_that_Japan_is_located_in_East_Asia}
```

## 文構造を使用した名詞の修飾方法

SFGPLでは名詞の修飾を行う際に，これらの文構造を使用する．
また，文が生成されたとき，その全体は名詞となり，それを別の文に埋め込むことができる．

"Your table is red."をSFGPLで表すには，次のようになる．

```SFGPL
{your_table_is_red}
```

このように"You have table"である```{you_have_table}```が主語となり，そのテーブルが赤い```{red}```ということが説明できる．
また，同等の意味である，"You have red table."は次のように表すことができる．

```SFGPL
{you_have_red_table}
```

### 強調形

特に文中で主語以外の単語を強調したい場合には，強調形 ```{determinerN_stressed}```を使用する事もできる．
"Your table is red."のtableを強調形にするためには次のようにする．

```SFGPL
{stressed_your_table_is_red}
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|run|{run}|
|this|{this}|
|table|{table}|
|red|{red}|
|you|{you}|
|become|{become}|
|teacher|{teacher}|
|look|{look}|
|sad|{sad}|
|study|{study}|
|English|{English}|
|school|{school}|
|bed|{bed}|
|big|{big}|
|yours|{yours_possessive}|
|book|{book}|
|Japan|{Japan}|
|in East Asia|{in_East_Asia}|
