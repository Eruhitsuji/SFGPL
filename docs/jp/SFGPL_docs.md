# 1. SFGPLについて

## はじめに

SFGPLは"Simple Functional General Purpose Language"の略で，自然言語を形式化するための言語である．
この言語は，文の構造や意味を容易に解釈でき，かつコミュニケーションができるようにするために考案した言語である．

また，この言語は私が趣味で作成したものであり，厳密に検証を行っていないため不備等がある可能性がある．

## SFGPL作成の背景と目的

多くの自然言語の文法では，多くの例外や存在し，学習者を悩ませることが多い．
また，それを解決するために，世界共通語を目的とした人工言語が提案されたが，それらは多くの自然言語と同様に曖昧な意味や複数の解釈ができる場合が存在する．
特に，接続詞や関係代名詞などを含む，長くて複雑な文章は解釈が困難であることが多い．
それらを解決するために，形式的，論理的に理解できるような言語を目的として作成した人工言語がSFGPLである．

## SFGPLの特徴

SFGPLでは，関数型の言語で，また関数のとる引数の型が厳密に定義されている．
SFGPLでは，文構造それぞれに関数が割り振られているため，主語，述語，目的語，補語などの文法上の役割が分かりやすくなっている．
また，文構造を組み合わせることによって複雑な文章を作成することができる．

## SFGPLの基本文法

- SFGPLには機能語と少しの単語のみが存在し，厳密に定義された意味を持つ．その他の単語は他の言語から借用される．
- 機能語の後にはいくつかの引数が付き，その引数によって意味が決まる．
- 原則として，各引数は1つの単語または1つのオブジェクトに対応するが，原語が複数の単語である場合は，アンダースコアで接続することで1つの単語とみなすことができる．
- 借用語の前後にはシングルクォーテーションを付けることで区別する．
- 文法上の性や数などの区別をすることはなく，また，冠詞も存在しない．
- 文末にはセミコロン(;)を付ける．ただし，単文の場合は省略可能である．

### SFGPLの文構造

SFGPLでは固有語によって，文構造が厳密に定義されている．
以下の表は，SFGPLで表現できる文構造の表である．
また使用方法等の詳細は，[文型](#17-文型)に記述してある．

|||単語|関数|引数|補足|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|S V|ta|Noun.do|S,V||
|2|S V C|ma|Noun.eq|S,V,C|Cが名詞|
|2|S V C|me|Noun.haveP|S,V,C|Cが修飾語|
|3|S V O|te|Noun.doT|S,V,O||
|4|S V O1 O2|ti|Noun.give|S,V,O1,O2||
|5|S V O C|tu|Noun.makeN|S,V,O,C|Cが名詞|
|5|S V O C|to|Noun.makeM|S,V,O,C|Cが修飾語|
|-|A has B|mi|Noun.have|A,V,B|AがBを所有している|
|-|A belongs to B|mu|Noun.belong|A,V,B|AがBに所属している|
|-|A is more B than C|mo|Noun.gt|A,V,B,C|AがCよりBである|

## SFGPLの発音

SFGPLの固有単語においては，発音の例外が存在しない．
また，以下の表の国際音声記号(IPA)は発音例である．

SFGPLの子音は次の表のようなものがある．

|表記|IPA|
|:-:|:-:|
|p|/p/|
|b|/b/|
|f|/f/|
|m|/m/|
|t|/t/|
|d|/d/|
|s|/s/|
|n|/n/|
|l|/l/|
|k|/k/|
|g|/g/|
|w|/w/|

一方，SFGPLの母音は次の表のようなものがある．

|表記|IPA|
|:-:|:-:|
|a|/a/|
|e|/e/|
|i|/i/|
|u|/u/|
|o|/o/|

また，借用語は借用語固有の発音で読む．

## SFGPLの単語

SFGPLの[単語](#3-単語)は主に，SFGPLの固有の単語と借用語に分かれる．

固有単語は，主に文構造に必要な機能語と，動詞と修飾語の基礎単語が存在する．
またそれ以外は，借用語が使用される．

そして，SFGPLの文構造では，品詞の場所が決定されており，それに従った品詞の単語を使わなければならない．

### SFGPLの品詞

SFGPLの品詞は名詞(Noun)，動詞(Verb)，修飾詞(Modifier)の三種類がある．
また，名詞のサブクラスとして句(Phrase)，代名詞（Pronoun），Bool配列型（BoolList），LangListとLangFuncが存在する．
BoolList，LangList，LangFuncは一般的な文以外に論理的な文を作る際に使用される．
さらに，名詞や動詞を修飾する特殊な語として，名詞限定語（DeterminerN）と動詞限定語（DeterminerV）が存在する．
そして，真偽を表すBool型が存在する．

それぞれの品詞にはそれぞれ特有の関数（機能語）が存在し，それによって品詞の変更や意味の決定などが行われる．
その他に，基礎単語を実装する，単語（Word）が存在する．
単語は，品詞別に動詞の単語の"WordV"，修飾語の単語の"WordM"が存在する．

名詞は，あらゆる物体，物質，人物，場所などのあらゆる概念を表す語である．
動詞は，あらゆる動作，作用，状態，存在などを表す語である．
修飾語は，他の語を修飾する語である．SFGPLでは形容詞と副詞の区別はつけない．

PythonライブラリSFGPLでは品詞ごとにクラスが存在する．

![PartOfSpeach](../img/PartOfSpeach.jpg)

### SFGPLの機能語

機能語により，文の役割や品詞等の決定がされる．
機能語の機能，役割や意味は引数内でのみしか適応されない．

この機能語らは，Pythonの関数と一対一となっている．
また，引数の数も決まっていて，引数の場所によって，役割が決まっている．

機能語の一覧と利用方法は，[dict.csv](../../dict.csv)に記述されている．

### SFGPLの借用語

SFGPLで存在しない単語は借用語を使用する．
借用語は，英語などの世界でよく使われる言語から借用することが好ましいが，相手に伝わる単語であれば問題とはならないはずである．
ただし，借用語は原型で使い，活用がある場合はSFGPLの機能語で行うことを推奨している．

## SFGPLとプログラミング

SFGPLの文は，Pythonオブジェクトに書き換えることができる．
このプロジェクトは，SFGPLが定義されているファイルが含まれている．
PythonでSFGPLを使用するためには，[SFGPL.py](../../SFGPL/SFGPL.py)をインポートすることで使用することができる．
使用例は[samples](../../py/samples)のPythonファイルに記載されている．
また，PythonでのSFGPLライブラリの詳細な実行方法は，[How_to_Use_SFGPL_in_Python.ipynb](../../How_to_Use_SFGPL_in_Python.ipynb)に記載されている．

# 2. 文型

## SFGPLの文型の一覧

SFGPLでは以下の表のような文型が存在し，それらの文の組み合わせにより，文自体が構成される．また，単語の修飾なども行われる．

|||単語|関数|引数|補足|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|S V|ta|Noun.do|S,V||
|2|S V C|ma|Noun.eq|S,V,C|Cが名詞|
|2|S V C|me|Noun.haveP|S,V,C|Cが修飾語|
|3|S V O|te|Noun.doT|S,V,O||
|4|S V O1 O2|ti|Noun.give|S,V,O1,O2||
|5|S V O C|tu|Noun.makeN|S,V,O,C|Cが名詞|
|5|S V O C|to|Noun.makeM|S,V,O,C|Cが修飾語|
|-|A has B|mi|Noun.have|A,V,B|AがBを所有している|
|-|A belongs to B|mu|Noun.belong|A,V,B|AがBに所属している|
|-|A is more B than C|mo|Noun.gt|A,V,B,C|AがCよりBである|

## Noun.do

Noun.do ```ta```では，特に，英語の第一文型と同じ形のSが主語，Vが動詞で，主語が何かの動作をするという．単純な文章を表すことができる．
"I run."をSFGPLで表すには，次のようになる．

```SFGPL
ta ga sa 'run'
```

## Noun.eq

Noun.eq ```ma```では，特に，英語の第二文型である"S is C"に相当し，その中でも，補語Cが名詞であるものを表す表すことができる．
また，この構文ではSとCが等価であることも示している．
Vが英語でbe動詞に相当する場合，動詞として```so```を使用する．
"This is a table."をSFGPLで表すには，次のようになる．

```SFGPL
ma gu so fa 'table'
```

"You become a teacher."をSFGPLで表すには，次のようになる．

```SFGPL
ma ge sa 'become' fa 'teacher'
```

## Noun.haveP

Noun.haveP ```me```では，特に，英語の第二文型である"S is C"に相当し，その中でも，補語Cが修飾語であるものを表す表すことができる．
また，この構文ではSがCという性質や状態であるということを表す．
Vが英語でbe動詞に相当する場合，動詞として```so```を使用する．
"The table is red."をSFGPLで表すには，次のようになる．

```SFGPL
me fa 'table' so la 'red'
```

"You look sad."をSFGPLで表すには，次のようになる．

```SFGPL
me ge sa 'look' la 'sad'
```

## Noun.doT

Noun.doT ```te```では，特に，英語の第三文型に相当し，Sが主語，Vが動詞，Oが目的語である．
"I study English."をSFGPLで表すには，次のようになる．

```SFGPL
te ga sa 'study' fa 'English'
```

## Noun.give

Noun.give ```ti```では，特に，英語の第四文型に相当し，Sが主語，Vが動詞，O1とO2が目的語である．特に，この構文では，SがO1にO2をVするという意味となる．
Vが英語で"give"に相当する場合，動詞として```so```を使用する．
"I give you a table."をSFGPLで表すには，次のようになる．

```SFGPL
ti ga so ge fa 'table'
```

## Noun.makeNとNoun.makeM

Noun.makeN ```tu```とNoun.makeM ```to```では，特に，英語の第五文型に相当し，Sが主語，Vが動詞，Oが目的語，Cが補語である．
Noun.makeNはCが名詞，Noun.makeMはCが修飾語のときに使用する．
この構文では"SがOをCにさせる"という意味になる．
Vが英語で"make"に相当する場合，動詞として```so```を使用する．

"I make you a teacher."をSFGPLで表すには，次のようになる．

```SFGPL
tu ga so ge fa 'teacher'
```

"I make you sad."をSFGPLで表すには，次のようになる．

```SFGPL
to ga so ge la 'sad'
```

## Noun.have

Noun.have ```mi```は"AがBを所有している"という意味になる．
Vが英語で"have"に相当する場合，動詞として```so```を使用する．
"I have a table."をSFGPLで表すには，次のようになる．

```SFGPL
mi ga so fa 'table'
```

## Noun.belong

Noun.belong ```mu```は"AがBに所属している"という意味になる．
Vが英語で"belong to"に相当する場合，動詞として```so```を使用する．
"I belong to a school."をSFGPLで表すには，次のようになる．

```SFGPL
mu ga so fa 'school'
```

## Noun.gt

Noun.gt ```mo```は"AはCよりBである"という意味になる．
このときAとBが比較対象の名詞，Cは修飾語である．
Vが英語でbe動詞に相当する場合，動詞として```so```を使用する．
"The bed is bigger than yours."をSFGPLで表すには，次のようになる．

```SFGPL
mo fa 'bed' so wan sen ge
```

## 文構造を使用した名詞の修飾方法

SFGPLでは名詞の修飾を行う際に，これらの文構造を使用する．
また，文が生成されたとき，その全体は名詞となり，それを別の文に埋め込むことができる．

"Your table is red."をSFGPLで表すには，次のようになる．

```SFGPL
me mi ge so fa 'table' so la 'red'
```

このように"You have table"である```mi ge so fa 'table'```が主語となり，そのテーブルが赤い```la 'red'```ということが説明できる．
また，同等の意味である，"You have red table."は次のように表すことができる．

```SFGPL
mi ge so me fa 'table' so la 'red'
```

### 強調形

特に文中で主語以外の単語を強調したい場合には，強調形 ```san```を使用する事もできる．
"Your table is red."のtableを強調形にするためには次のようにする．

```SFGPL
me mi ge so san fa 'table' so la 'red'
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|run|sa 'run'|
|this|gu|
|table|fa 'table'|
|red|la 'red'|
|you|ge|
|become|sa 'become'|
|teacher|fa 'teacher'|
|look|sa 'look'|
|sad|la 'sad'|
|study|sa 'study'|
|English|fa 'English'|
|school|fa 'school'|
|bed|fa 'bed'|
|big|wan|
|yours|sen ge|

# 3. 単語

## 借用語について

SFGPLは基礎単語以外は借用語にて代用する．
名詞，動詞，修飾語にて，借用語を使用するためには，次の表のように表す．

|元の語|品詞|SFGPL|
|:-:|:-:|:-:|
|apple|名詞|fa 'apple'|
|open|動詞|sa 'open'|
|tall|修飾語|la 'tall'|

これらの単語を使った例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I have an apple.|mi ga so fa 'apple'|
|I open a door.|te ga sa 'open' fa 'door'|
|I am tall.|me ga so la 'tall'|

## 固有単語について

SFGPLでは，動詞と修飾語については，いくつかの固有単語が用意されている．
WordV，WordMクラスでは，SFGPLに固有に存在する単語群である．

これらの単語群は，品詞が既に決定していおり，また広い意味を持っているため汎用性は高いが，意味の詳細の特定はしにくいものである．

次の表は，固有単語の例である．

|English|SFGPL|
|:-:|:-:|
|create|kan|
|big|wan|

これらの単語を使った例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I create a door.|te ga kan fa 'door'|
|The apple is big.|me fa 'apple' so wan|

## 限定詞について

SFGPLには[名詞限定詞](#12-名詞限定詞)が存在する．
これは，元々名詞を修飾する特別な語である．
しかし，限定詞自体の意味をそのまま名詞にすることもできる．
そのためには，```fo```を使用する．
使用例を次の表に表す．

|English|SFGPL|
|:-:|:-:|
|human|ben fo|

これらの単語を使った例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I am human.|ma ga so ben fo|

## 無意味単語について

SFGPLには，意味を付加しない単語が存在する．
これらの単語は，品詞ごとに存在し，文法上必要なときに使われる．

||SFGPL|
|:-:|:-:|
|Noun|fo|
|Verb|so|
|Modifier|lo|

```fo```では，[名詞限定詞](#12-名詞限定詞)をそのままの意味で表すときによく使われる．
また，```so```は，特に[文型](#17-文型)で，動詞が必要ない場合など使われる．
一方，```lo```は，あまり使われない．
これらの例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I am human.|ma ga so ben fo|
|I have an apple.|mi ga so fa 'apple'|

## 代名詞について

SFGPLでは[代名詞](#4-代名詞)が存在する．
代名詞は次の表のようなものがある．

||English|SFGPL|
|:-:|:-:|:-:|
|一人称代名詞|I|ga|
|二人称代名詞|you|ge|
|三人称代名詞|he/she/it|gi|
|近称代名詞|this|gu|
|遠称代名詞|that|go|
|疑問代名詞|what|wa|
|不定代名詞|something|we|

# 4. 代名詞

## 代名詞一覧

代名詞は次の表のようなものがある．

||English|SFGPL|
|:-:|:-:|:-:|
|一人称代名詞|I|ga|
|二人称代名詞|you|ge|
|三人称代名詞|he/she/it|gi|
|近称代名詞|this|gu|
|遠称代名詞|that|go|
|疑問代名詞|what|wa|
|不定代名詞|something|we|

## 代名詞の応用

SFGPLの代名詞は原則として人，生物，物，概念，場所，時間，理由，方法等の区別はされない．
そして，性別や，数による区別も存在しない．
これらの区別をする場合は，[名詞限定詞](#12-名詞限定詞)を使用することで限定できる．


疑問詞に対する名詞限定詞の使用方法は次の表となる．

|English|SFGPL|
|:-:|:-:|
|what|pen wa|
|who|ben wa|
|when|pin wa|
|where|pun wa|
|why|pon wa|
|how|ban wa|

また，複数形を明示するためには```don```を使用する．
例えば，"We"を表すには```don ga```とする．

SFGPLでは性の区別が存在しない．
また，人と物の区別も存在しない．
例えば，三人称代名詞の男性，女性，事物を明示するためには，次のようにする．

||English|SFGPL|
|:-:|:-:|:-:|
|男性|he|lan gi|
|女性|she|len gi|
|事物|it|pen gi|

さらに，所有代名詞，再帰代名詞を作成するには```sen```や```sin```を使用する．
次の表は，一人称代名詞の所有代名詞，再帰代名詞である．

||English|SFGPL|
|:-:|:-:|:-:|
|所有代名詞|mine|sen ga|
|再帰代名詞|myself|sin ga|

# 5. 否定文

否定文を作成するためには```pa```を使用する．
この語は，文章に付属することで否定文を作る．
"I have a table."はSFGPLでは```mi ga so fa 'table'```である．
それを否定文の"I don't have a table."という意味にする場合，SFGPLでは次のように表現できる．

```SFGPL
pa mi ga so fa 'table'
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|table|fa 'table'|

# 6. 疑問文

疑問文を作成するためには```da```を使用する．
この単語を文につけると疑問文になる．
"You have a table."はSFGPLでは```mi ge so fa 'table'```である．
それを疑問文の"Do you have a table?"という意味にする場合，SFGPLでは次のように表現できる．

```SFGPL
da mi ge so fa 'table'
```

また，疑問詞を含む疑問文の場合，不定のところを疑問詞に置き換えることで表す．

"Who has a table?"は次のように表す．

```SFGPL
da mi ben wa so fa 'table'
```

"What do you have?"は次のように表す．

```SFGPL
da mi ge so pen wa
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|you|ge|
|table|fa 'table'|
|who|ben wa|
|what|pen wa|

# 7. 命令文

命令文を作成するためには```de```を使用する．
この単語を文につけると命令文になる．
"You buy a table."はSFGPLでは```te ge sa 'buy' fa 'table'```である．
それを命令文の"Buy a table, you!"という意味にする場合，SFGPLでは次のように表現できる．

```SFGPL
de te ge sa 'buy' fa 'table'
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|you|ge|
|buy|sa 'buy'|
|table|fa 'table'|

# 8. 動詞の活用

## 動詞の時制

SFGPLでは以下の図のような動詞の時制が存在する．

![BasingPoint](../img/BasingPoint.jpg)

このように，SFGPLでは①過去形，②現在形，③未来形の3つの時制が存在する．
これら時制は動詞の活用として基礎的なもので，文の時間の基準点となる．
時制を使用した例文は次の表のようになる．

|時制|English|SFGPL|
|:-:|:-:|:-:|
|①過去形|I lived in Tokyo.|di ta ga na sa 'live' li pun fa 'Tokyo'|
|②現在形|I live in Tokyo.|ta ga na sa 'live' li pun fa 'Tokyo'|
|③未来形|I will live in Tokyo.|du ta ga na sa 'live' li pun fa 'Tokyo'|

特に```di```と```du```では，文章自体に付属し形容する．

### 動詞の拡張時制

前項で説明した動詞は，一番基本的な動詞の時制の表し方である．
しかし，SFGPLではDeterminVクラスにによって，主に時制を組み合わせるための単語が存在する．
また，このDeterminerVクラスによる拡張時制は，Phraseクラスによる基礎時制より優先度が低く，基本的には基礎時制で文全体の時制を表す．
以下の表は拡張時制を表す単語である．

|時制|単語|
|:-:|:-:|
|①過去形|bak|
|②現在形|bik|
|③未来形|bok|

これらの時制を組み合わせることで，未来過去形や過去未来形などの複合時制を作ることができる．
次の例は，未来の時点で過去を表す未来過去形の例である．  

```SFGPL
du ta ga na bak sa 'live' li pun fa 'Tokyo'
```

まとめるとSFGPLにおける時制は以下の表のようなものが存在する．
以下の表の列名はPhraseによる基礎時制の種類，行名はDeterminerVによる拡張時制の種類を表している．
また，```A/B```でAは基礎時制，B拡張時制を表す，

||Past Tense|-|Future Tense|
|:-:|:-:|:-:|:-:|
|**-**|di/-|-/-|du/-|
|**Past Tense**|di/bak|-/bak|du/bak|
|**Present Tense**|di/bik|-/bik|du/bik|
|**Future Tense**|di/bok|-/bok|du/bok|

## 相

SFGPLでは下の図のように，①起動相，②経過相，③完結相，④継続相，⑤終了相，⑥進行相の6つが存在する．

![ProgressiveForm](../img/ProgressiveForm.jpg)

"I wear dress"という意味の```te ga sa 'wear' fa 'dress'```について，それぞれの相での例文を次の表に示す．

|相|単語|English|SFGPL|
|:-:|:-:|:-:|:-:|
|①起動相|tak|I begin wear a dress.|te ga tak sa 'wear' fa 'dress'|
|②経過相|tek|I am (in the process of) wearing a dress.|te ga tek sa 'wear' fa 'dress'|
|③完結相|tik|I wear a dress. (I just finished wearing it.)|te ga tik sa 'wear' fa 'dress'|
|④継続相|tuk|I am wearing a dress. (The state in which it is worn.)|te ga tuk sa 'wear' fa 'dress'|
|⑤終了相|tok|I finish wear a dress. (I stopped wearing it.)|te ga tok sa 'wear' fa 'dress'|
|⑥進行相|ni|I am wearing a dress.|te ga ni sa 'wear' fa 'dress'|

これらの相は，現在形以外にも，過去形，未来形にできる．
⑥進行相は②経過相と④継続相が含まれている．
また③完結相と⑤終了相が同じである場合もある．
"I begin wear a dress."を過去形，未来形にすると次のようになる．

```SFGPL
di te ga tak sa 'wear' fa 'dress'
du te ga tak sa 'wear' fa 'dress'
```

また，原則として相単体では，時間の幅はなく，その瞬間だけを表す．
時間の幅を表す場合は，完了形を付け加える．
進行形に完了形を加えた"I have been wearing a dress."を表すには，次のようになる．

```SFGPL
te ga nu ni sa 'wear' fa 'dress'
```

### 一般的な進行形

SFGPLでは前節の①～⑤のような相を考えずに，⑥のように単純な進行形にすることができる．
SFGPLは次のように，"I am wearing the dress."という意味の進行形を表すことができる．

```te ga ni sa 'wear' fa 'dress'```

進行形を表す```ni```は動詞に付属する．
これらは，現在形以外にも，過去形，未来形にできる．
"I am wearing the dress."を過去形，未来形にすると次のようになる．

```SFGPL
di te ga ni sa 'wear' fa 'dress'
du te ga ni sa 'wear' fa 'dress'
```

## 完了形

SFGPLでは，以下の図のような，英語と同等な完了形が存在する．

![PerfectForm](../img/PerfectForm.jpg)

この完了形では過去に起こったことが続いていることを表す際に使用する．
3つの時制に対する完了形の例は次のようになる．

|時制|English|SFGPL|
|:-:|:-:|:-:|
|①過去完了形|I had lived in Tokyo.|di ta ga nu na sa 'live' li pun fa 'Tokyo'|
|②現在完了形|I have lived in Tokyo.|ta ga nu na sa 'live' li pun fa 'Tokyo'|
|③未来完了形|I will have lived in Tokyo.|du ta ga nu na sa 'live' li pun fa 'Tokyo'|

完了形を表す```nu```では，動詞自体に付属し，修飾する．

## 受動態

SFGPLは次のように，"The dress is worn."という意味の受動態を表すことができる．

```ta fa 'dress' ne sa 'wear'```

受動態を表す```ne```は動詞に付属する．
これらは，現在形以外にも，過去形，未来形にできる．
"The dress is worn."を過去形，未来形にすると次のようになる．

```SFGPL
di ta fa 'dress' ne sa 'wear'
du ta fa 'dress' ne sa 'wear'
```

## その他の動詞の修飾

[DeterminerV](#13-動詞限定詞)クラス内の関数では，その他の動詞の修飾をすることができる．
また，それらは，英語の助動詞と似ている．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|live|sa 'live'|
|in Tokyo|li pun fa 'Tokyo'|
|wear|sa 'wear'|
|dress|fa 'dress'|

# 9. 修飾語

## 修飾語について

SFGPLには形容詞と副詞の違いがなく，修飾する語はすべて修飾語となる．

修飾語は，修飾の反対の意を表すための単語が用意されている．
それによって，英語の"big"に対応する```wan```を```ke wan```とすることで，"small"という意味にすることができる．

## 比較表現

SFGPLには2項の名詞に対しての比較を行う文の```mo```が存在する．
```mo A F B C```で，"AはCよりBである．"という意味となる．

"My table is bigger than yours."のような比較表現は次のようにして表す．

```SFGPL
mo mi ga so san fa 'table' so wan sen ge
```

## 各品詞に対する修飾語

各品詞を単純に修飾語で修飾するためには，次の表になる．

||SFGPL|
|:-:|:-:|
|Noun|me Noun Modifier|
|Verb|na Verb Modifier|
|Modifier|ka Modifier Modifier|

## 修飾語の応用

修飾語では，英語の前置詞と名詞含む句を修飾語として代用する事ができる．
このとき，名詞を修飾語に変換する```li```と，[名詞限定詞](#12-名詞限定詞)がよく組み合わされて表現される．
例えば，"I live in Tokyo."と表す場合は，次のように表せる．

```SFGPL
ta ga na sa 'live' li pun fa 'Tokyo'
```

また，```pun```は，場所を表す限定詞である．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|table|fa 'table'|
|yours|sen ge|
|live|sa 'live'|
|in Tokyo|li pun fa 'Tokyo'|

# 10. 品詞変換

SFGPLでは，名詞，動詞，修飾語の相互の品詞を変換することができる．
以下の表はSFGPLで品詞変換する語の一覧である．

||変換前の品詞|変換後の品詞|単語|
|:-:|:-:|:-:|:-:|
|V2N|動詞|名詞|fi|
|M2N|修飾語|名詞|fu|
|M2V|修飾語|動詞|si|
|N2V|名詞|動詞|su|
|N2M|名詞|修飾語|li|
|V2M|動詞|修飾語|lu|

特に，動詞から名詞，名詞から修飾語はよく使用される．
動詞から名詞は"This is building."のように使用される．

```SFGPL
ma gu so fi sa 'build'
```

また，名詞から修飾語は，英語の前置詞と名詞が組み合わされた句と同等の意味を作成するときに使われる．
またそのときは，```li```と限定詞([DeterminerN](#12-名詞限定詞))が組み合わされて使用する．
"I live in Tokyo."をSFGPLにすると次のようになる．
このとき，```pun```は場所を表す限定詞である．

```SFGPL
ta ga na sa 'live' li pun fa 'Tokyo'
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|this|gu|
|building|fi sa 'build'|
|I|ga|
|live|sa 'live'|
|in Tokyo|li pun fa 'Tokyo'|

# 11. 接続詞

SFGPLは，文と文や単語と単語を繋ぐものとして接続詞が存在する．
SFGPLの主な接続詞として次のようなものがある．

|Word|English Word|English|SFGPL|
|:-:|:-:|:-:|:-:|
|pe|because|I go to a store, because I want it.|pe ta ga na sa 'go' li pun fa 'store' te ga sa 'want' pen gi|
|pu|so|I want it, so I go to a store.|pu te ga sa 'want' pen gi ta ga na sa 'go' li pun fa 'store'|
|pi|if|I go to a store, if I want it.|pi ta ga na sa 'go' li pun fa 'store' te ga sa 'want' pen gi|
|po|but|I want it, but I don't go to a store.|po te ga sa 'want' pen gi pa ta ga na sa 'go' li pun fa 'store'|
|ba|and|I go to a store, and I go to a library.|ba ta ga na sa 'go' li pun fa 'store' ta ga na sa 'go' li pun fa 'library'|
|be|or|I go to a store, or I go to a library.|I go to a store, or I go to a library.|be ta ga na sa 'go' li pun fa 'store' ta ga na sa 'go' li pun fa 'library'|

また，```ba fa 'store' fa 'library'```や```be fa 'store' fa 'library'```のように，単語同士でも接続することができる．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I go to a store|ta ga na sa 'go' li pun fa 'store'|
|I don't go to a store|pa ta ga na sa 'go' li pun fa 'store'|
|I want it|te ga sa 'want' pen gi|
|I go to a library|ta ga na sa 'go' li pun fa 'library'|
|store|fa 'store'|
|library|fa 'library'|

# 12. 名詞限定詞

名詞限定詞は，名詞を修飾するための最も単純なものである．
また，代名詞と使われたり，名詞から修飾語に変換するときに使用する```li```と一緒に使われることが多い．

次の表は名詞限定詞の例である．

|Word|Base Meaning|English|SFGPL|
|:-:|:-:|:-:|:-:|
|lan|male|He is student.|ma lan gi so fa 'student'|
|len|female|She is student.|ma len gi so fa 'student'|
|don|plural|They are student.|ma don gi so fa 'student'|
|pun|place|I go to Tokyo.|ta ga na sa 'go' li pun fa 'Tokyo'|
|pin|time|I go today.|ta ga na sa 'go' li pin fa 'today'|

また，名詞限定詞は複数個付加することができる．

一般的に，名詞限定詞A,Bと名詞Nの場合で，```A B N```という句は，「Aの(BのN)」という意味になる．

## 単語集

|English|SFGPL|
|:-:|:-:|
|he/she/they|gi|
|student|fa 'student'|
|I|ga|
|go|sa 'go'|
|Tokyo|fa 'Tokyo'|
|today|fa 'today'|

# 13. 動詞限定詞

動詞限定詞は，動詞を修飾するための最も単純なものである．
これらは，英語の助動詞に相当する．
次の表は動詞限定詞の例である．

|Word|Base Meaning|English|SFGPL|
|:-:|:-:|:-:|:-:|
|nak|possible|I can see a sea.|te ga nak sa 'see' fa 'sea'|
|nek|ability|I can swim.|ta ga nek sa 'swim'|
|nuk|obligation|I should swim.|ta ga nuk sa 'swim'|
|nok|necessary|I need to swim.|ta ga nok sa 'swim'|
|lak|duty|I must swim.|ta ga lak sa 'swim'|
|lik|want to|I want to swim.|ta ga lik sa 'swim'|

また，相などの，[動詞の活用](#8-動詞の活用)をすることもできる．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|see|sa 'see'|
|sea|fa 'sea'|
|swim|sa 'swim'|

# 14. Bool関連クラス

SFGPLにはBoolに関連したクラス，Bool型と，BoolList型が存在する．
これらのクラスは，真偽値や，数値などを表すために使われる．

## Bool型について

Bool型は，真偽を表すためのクラスである．
Bool型のFalseとTrueは次のように表される．

||word|
|:-:|:-:|
|False|pas|
|True|pos|

また，```pis```を使用して，Bool型と名詞を次のように接続することで，ある名詞に対する真偽を表すことができる．
次の文は"It is true that I am a student."という例を表す．

```SFGPL
pis ma ga so fa 'student' pos
```

そして，Bool型では，LangObjに備わっている，NOT ```pa```，OR ```be```，AND ```ba```，NOR ```bo```とNAND ```bu```を使用することもできる．
そして，それら関数は論理演算をすることができる．

## BoolList型について

BoolListでは，真偽値の配列を作成することができる．
BoolListには以下のような関数が存在している．

|単語|説明|
|:-:|:-:|
|fas|真偽のリスト（BoolList）を作成する|
|fes A B|BoolList(A)のB番目の値を取得する|
|fis A B|BoolList(A)に1つのBool(B)を末尾に加える|
|fus A B C|AというBoolListに対して，B番目からC番目までのリストを取得する|
|fos A B|2つのBoolList(A,B)を結合する|
|mas A B|2つBoolの値(A,B)からなるBoolListを作成する|
|mis X1~X4|4つBoolの値(x1~x4)からなるBoolListを作成する|
|mos X1~X8|8つBoolの値(x1~x8)からなるBoolListを作成する|
|tas A|BoolList(A)を2進数の自然数とみなす|
|tes A|BoolList(A)を2進数の整数とみなす|
|tis A|BoolList(A)を2進数の浮動小数とみなす|
|tus A|BoolList(A)をASCII文字とみなす|

次のようにすることによって，4byteのデータを使用することができる．

```SFGPL
fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos
```

これは，2進数で```0100 0000 0100 1001 0000 1111 1101 1011```を表している．
また，次のようにすることで，数値として使うことができる．

|Type|SFGPL|Value|
|:-:|:-:|:-:|
|自然数|tas fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|1078530011|
|整数|tes fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|1078530011|
|浮動小数点|tis fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|3.1415927410125732|

## 単語集

|English|SFGPL|
|:-:|:-:|
|I am a student|ma ga so fa 'student'|

# 15. LangList

SFGPLでは基本的なデータ構造型として，LangList型が存在する．
LangListには，以下の関数が存在している．

|単語|説明|
|:-:|:-:|
|fat|LangObjのリストLangListを作成する|
|fet A B|LangList(A)のB番目の値を取得する|
|fit A B|LangList(A)に1つのLangObj(B)を末尾に加える|
|fut A B C|AというLangListに対して，B番目からC番目までのリストを取得する|
|fot A B|2つのLangListを結合する|

LangListは，LangObjを継承しているすべてのクラスを格納することができる．
次はLangListを作成する一例である．

```SFGPL
fit fit fit fit fit fat ga fa 'pen' sa 'go' la 'happy' ma ga so fa 'student'
```

また，このLangListから最初の値を取得するには次のようにする．
このとき```fis fas pas```は[BoolList](#14-bool関連クラス)における0を表している．

```SFGPL
fet fit fit fit fit fit fat ga fa 'pen' sa 'go' la 'happy' ma ga so fa 'student' fis fas pas
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|pen|fa 'pen'|
|go|sa 'go'|
|happy|la 'happy'|
|I am a student|ma ga so fa 'student'|

# 16. LangFunc

SFGPLでは基本的な関数型として，LangFunc型が存在する．
LangFuncには，以下の関数が存在している．

|単語|説明|
|:-:|:-:|
|pat A B|あるLangListを引数とするAという名前のBを返す関数を設定する|
|pit|patの引数用に使用する|
|pot A B|設定したAという名前のLangFuncを引数Bとして実行する|

LangFuncは，```pat```によって関数を設定する．
また，```pit```を```pat```の第二引数内の文内に含ませることができる．
それによって，関数実行時に実際の値が代入されて処理される．
また，```pat```の第一引数は関数名を表す．
そして，関数名は重複して付けることはできない．
以下は，関数設定の例を示す．

```SFGPL
pat fa 'xor' fit fat bu bu fet pit mas pas pas bu fet pit mas pas pas fet pit mas pas pos bu bu fet pit mas pas pas fet pit mas pas pos fet pit mas pas pos
```

この関数は，あるLangListに対して，0番目と1番目のXORを取る関数である．
この関数に(false,false)を与えるときは，次のようにする．

```SFGPL
pot fa 'xor' fit fit fat pas pas
```

# 2. 文型

## SFGPLの文型の一覧

SFGPLでは以下の表のような文型が存在し，それらの文の組み合わせにより，文自体が構成される．また，単語の修飾なども行われる．

|||単語|関数|引数|補足|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|S V|ta|Noun.do|S,V||
|2|S V C|ma|Noun.eq|S,V,C|Cが名詞|
|2|S V C|me|Noun.haveP|S,V,C|Cが修飾語|
|3|S V O|te|Noun.doT|S,V,O||
|4|S V O1 O2|ti|Noun.give|S,V,O1,O2||
|5|S V O C|tu|Noun.makeN|S,V,O,C|Cが名詞|
|5|S V O C|to|Noun.makeM|S,V,O,C|Cが修飾語|
|-|A has B|mi|Noun.have|A,V,B|AがBを所有している|
|-|A belongs to B|mu|Noun.belong|A,V,B|AがBに所属している|
|-|A is more B than C|mo|Noun.gt|A,V,B,C|AがCよりBである|

## Noun.do

Noun.do ```ta```では，特に，英語の第一文型と同じ形のSが主語，Vが動詞で，主語が何かの動作をするという．単純な文章を表すことができる．
"I run."をSFGPLで表すには，次のようになる．

```SFGPL
ta ga sa 'run'
```

## Noun.eq

Noun.eq ```ma```では，特に，英語の第二文型である"S is C"に相当し，その中でも，補語Cが名詞であるものを表す表すことができる．
また，この構文ではSとCが等価であることも示している．
Vが英語でbe動詞に相当する場合，動詞として```so```を使用する．
"This is a table."をSFGPLで表すには，次のようになる．

```SFGPL
ma gu so fa 'table'
```

"You become a teacher."をSFGPLで表すには，次のようになる．

```SFGPL
ma ge sa 'become' fa 'teacher'
```

## Noun.haveP

Noun.haveP ```me```では，特に，英語の第二文型である"S is C"に相当し，その中でも，補語Cが修飾語であるものを表す表すことができる．
また，この構文ではSがCという性質や状態であるということを表す．
Vが英語でbe動詞に相当する場合，動詞として```so```を使用する．
"The table is red."をSFGPLで表すには，次のようになる．

```SFGPL
me fa 'table' so la 'red'
```

"You look sad."をSFGPLで表すには，次のようになる．

```SFGPL
me ge sa 'look' la 'sad'
```

## Noun.doT

Noun.doT ```te```では，特に，英語の第三文型に相当し，Sが主語，Vが動詞，Oが目的語である．
"I study English."をSFGPLで表すには，次のようになる．

```SFGPL
te ga sa 'study' fa 'English'
```

## Noun.give

Noun.give ```ti```では，特に，英語の第四文型に相当し，Sが主語，Vが動詞，O1とO2が目的語である．特に，この構文では，SがO1にO2をVするという意味となる．
Vが英語で"give"に相当する場合，動詞として```so```を使用する．
"I give you a table."をSFGPLで表すには，次のようになる．

```SFGPL
ti ga so ge fa 'table'
```

## Noun.makeNとNoun.makeM

Noun.makeN ```tu```とNoun.makeM ```to```では，特に，英語の第五文型に相当し，Sが主語，Vが動詞，Oが目的語，Cが補語である．
Noun.makeNはCが名詞，Noun.makeMはCが修飾語のときに使用する．
この構文では"SがOをCにさせる"という意味になる．
Vが英語で"make"に相当する場合，動詞として```so```を使用する．

"I make you a teacher."をSFGPLで表すには，次のようになる．

```SFGPL
tu ga so ge fa 'teacher'
```

"I make you sad."をSFGPLで表すには，次のようになる．

```SFGPL
to ga so ge la 'sad'
```

## Noun.have

Noun.have ```mi```は"AがBを所有している"という意味になる．
Vが英語で"have"に相当する場合，動詞として```so```を使用する．
"I have a table."をSFGPLで表すには，次のようになる．

```SFGPL
mi ga so fa 'table'
```

## Noun.belong

Noun.belong ```mu```は"AがBに所属している"という意味になる．
Vが英語で"belong to"に相当する場合，動詞として```so```を使用する．
"I belong to a school."をSFGPLで表すには，次のようになる．

```SFGPL
mu ga so fa 'school'
```

## Noun.gt

Noun.gt ```mo```は"AはCよりBである"という意味になる．
このときAとBが比較対象の名詞，Cは修飾語である．
Vが英語でbe動詞に相当する場合，動詞として```so```を使用する．
"The bed is bigger than yours."をSFGPLで表すには，次のようになる．

```SFGPL
mo fa 'bed' so wan sen ge
```

## 文構造を使用した名詞の修飾方法

SFGPLでは名詞の修飾を行う際に，これらの文構造を使用する．
また，文が生成されたとき，その全体は名詞となり，それを別の文に埋め込むことができる．

"Your table is red."をSFGPLで表すには，次のようになる．

```SFGPL
me mi ge so fa 'table' so la 'red'
```

このように"You have table"である```mi ge so fa 'table'```が主語となり，そのテーブルが赤い```la 'red'```ということが説明できる．
また，同等の意味である，"You have red table."は次のように表すことができる．

```SFGPL
mi ge so me fa 'table' so la 'red'
```

### 強調形

特に文中で主語以外の単語を強調したい場合には，強調形 ```san```を使用する事もできる．
"Your table is red."のtableを強調形にするためには次のようにする．

```SFGPL
me mi ge so san fa 'table' so la 'red'
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|run|sa 'run'|
|this|gu|
|table|fa 'table'|
|red|la 'red'|
|you|ge|
|become|sa 'become'|
|teacher|fa 'teacher'|
|look|sa 'look'|
|sad|la 'sad'|
|study|sa 'study'|
|English|fa 'English'|
|school|fa 'school'|
|bed|fa 'bed'|
|big|wan|
|yours|sen ge|

# 18. 詳細な文法

SFGPLは基本的に，[文型](#17-文型)に記されているような文法は厳守する必要があるが，その他はユーザ側である程度決めてよい．
しかし，模範的な文法を本章で記述しておく．

## 文章を修飾する方法

文章全体に対して修飾するためには，基本的にその文内の動詞を```na```を使用することで修飾する．
例えば，"I go to Tokyo."という例文では，"to Tokyo"の部分が修飾語となる．
その際SFGPLでは次のように表現する．

```SFGPL
ta ga na sa 'go' li pun fa 'Tokyo'
```

また，別の方法として，```me```を使う方法もある．

```SFGPL
me ta ga sa 'go' so li pun fa 'Tokyo'
```

### 英語における前置詞的な用法

特に，英語における前置詞のように動詞を修飾する場合，```li```と[DeterminerN](#12-名詞限定詞)を使用して表現する．
英語の前置詞とSFGPLの一例を次の表に示す．

|English|Meaning|SFGPL|
|:-:|:-:|:-:|
|at/in/on/to/from|Time|li pin|
|at/in/on/to/from|Place|li pun|
|for|Reason|li pon|
|for|Way/Means|li ban|
|from|Start|li fan|
|to|End|li fen|
|between/among|Section|li fin|
|in|In|li fun|
|into|Into|li tun fun|
|out|Out|li fon|
|up/over|Move&Above|li tun man|
|above|Above|li man|
|down|Move&Below|li tun men|
|under|On&Below|li min men|
|below|Below|li men|
|on|On|li min|
|right|Right|li mun|
|left|Left|li mon|
|near|Near|li tin|
|by/about|By/About|li tan tin|
|with|With|li ten tin|

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|ga|
|go|sa 'go'|
|to Tokyo|li pun fa 'Tokyo'|

# 19. バージョンについて

このプロジェクトのバージョンは[\_\_version\_\_.py](../../SFGPL/__version__.py)に記載されている．
特に，Pythonで実行する場合は，以下のコードを実行することで確認できる．

```python
SFGPL.__version__.__version__
```

また，```SFGPL.SFGPLCorpus.saveJson```で出力されるコーパスのJSONファイル内には，実行されたときのバージョンが記載される．

## バージョン更新内容について

|Version|Update contents|
|:-:|:-:|
|1.0.0|正式版公開|
|1.0.1|例文の追加・修正|
|1.0.2|例文の追加・修正|
|1.0.3|バージョンごとの更新内容詳細の追加|
|1.1.0|PythonでのSFGPLの使い方詳細を追加|
|1.1.1|[How_to_Use_SFGPL_in_Python.ipynb](../../How_to_Use_SFGPL_in_Python.ipynb)の修正|
|2.0.0|論理値に関するクラスを追加|
|2.0.1|Pythonプログラムの追加・修正|
|2.0.2|ドキュメントの追加・修正|
|2.1.0|BoolList.get()とBoolList.slice()を追加|
|3.0.0|LangListとLangFuncクラスの追加|
|3.0.1|[How_to_Use_SFGPL_in_Python.ipynb](../../How_to_Use_SFGPL_in_Python.ipynb)の修正|
|3.1.0|LangFunc.runFunc()の修正|
|3.1.1|ドキュメントの追加・修正|
|3.1.2|ドキュメントの追加・修正|
|3.1.3|ドキュメントの追加・修正|
|4.0.0|DeterminerVクラスの追加|
|4.0.1|辞書の修正|
|4.0.2|ドキュメントの追加・修正|
|4.0.3|ドキュメントの追加・修正|
|4.0.4|ドキュメントの追加・修正|
|4.0.5|ドキュメントの追加・修正|
|4.0.6|ドキュメントの追加・修正|
|4.0.7|ドキュメントの追加・修正|
|4.0.8|ドキュメントの追加・修正|
|4.0.9|ドキュメントの追加・修正|
|4.0.10|ドキュメントの追加・修正|
|4.0.11|ドキュメントの追加・修正|
