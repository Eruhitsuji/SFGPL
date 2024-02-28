{page_header}

SFGPLの単語は，基本的に使い方が定まっている．
例えば，借用語を使用する方法などが決まっている．
本章ではこれら単語の種類と使用方法について記載する．
また，単語の詳細は[dict.csv](../../dict.csv)に記述されている．

また，SFGPLの単語では，基本的に，冠詞，数，性，格などによる変形は行われない．
数や性を示したいときには，[名詞限定詞]({docs_DeterminerN})を使用する．

## 借用語について

SFGPLは基礎単語以外は借用語にて代用する．
ただし，半角ダブルクオーテーション(")と半角スペース( )は使用できない．
また，半角シングルクォーテーション(')は，借用語であることを示す記号であるため，最初と最後に付けたい場合は注意が必要である．

名詞，動詞，修飾語にて，借用語を使用するためには，次の表のように表す．

|元の語|品詞|SFGPL|
|:-:|:-:|:-:|
|apple|名詞|{noun_apple}|
|open|動詞|{verb_open}|
|tall|修飾語|{modifier_tall}|

これらの単語を使った例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I have an apple.|{I_have_an_apple}|
|I open a door.|{I_open_a_door}|
|I am tall.|{I_am_tall}|

### 借用語と借用元の言語

借用語はあらゆる言語より借用することが可能である．
ただし，話者間双方で理解できる単語を選ぶことが望ましい．

例えば，あらゆる言語の「言語」という単語をSFGPLに借用するには次の表のようにする．

|Language|Raw Word|SFGPL|
|:-:|:-:|:-:|
|English|language|{language_en}|
|Japanese|言語|{language_ja}|
|Spanish|idioma|{language_es}|
|French|langue|{language_fr}|
|Russian|язык|{language_ru}|
|Portuguese|linguagem|{language_pt}|
|Esperanto|lingvo|{language_eo}|

このように，様々な言語から借用することができる．
また，この資料では基本的に借用語は英語から借用している．

## 固有単語について

SFGPLでは，動詞と修飾語については，いくつかの固有単語が用意されている．
WordV，WordMクラスでは，SFGPLに固有に存在する単語群である．

これらの単語群は，品詞が既に決定していおり，また広い意味を持っているため汎用性は高いが，意味の詳細の特定はしにくいものである．

次の表は，固有単語の例である．

|English|SFGPL|
|:-:|:-:|
|create|{create}|
|big|{big}|

これらの単語を使った例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I create a door.|{I_create_a_door}|
|The apple is big.|{the_apple_is_big}|

### 固有単語のルール

SFGPLの固有単語に関しては一意性があり，異なる意味の単語は異なる発音となる．
また音節構造は，一単語一音節（CVまたはCVC）である．

## 限定詞について

文法上の機能として，単語を単純に修飾する語である限定詞が存在する．
限定詞には，名詞を限定する名詞限定詞と，動詞を限定する動詞限定詞が存在する．

### 名詞限定詞

SFGPLには[名詞限定詞]({docs_DeterminerN})が存在する．
これは，元々名詞を修飾する特別な語である．
しかし，限定詞自体の意味をそのまま名詞にすることもできる．
そのためには，```{noun_none}```を使用する．
使用例を次の表に表す．

|English|SFGPL|
|:-:|:-:|
|human|{human}|

これらの単語を使った例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I am human.|{I_am_human}|

### 動詞限定詞

SFGPLには[動詞限定詞]({docs_DeterminerV})が存在する．
これは，動詞を修飾する特別な語である．
そしてこれらは，動詞の時制や相として使われる語や，助動詞的に動詞の意味を付加するものが存在している．

## 無意味単語について

SFGPLには，意味を付加しない単語が存在する．
これらの単語は，品詞ごとに存在し，文法上必要なときに使われる．

||SFGPL|
|:-:|:-:|
|Noun|{noun_none}|
|Verb|{verb_none}|
|Modifier|{modifier_none}|

はじめに，無意味名詞の```{noun_none}```では，[名詞限定詞]({docs_DeterminerN})をそのままの意味で表すときによく使われる．
また，無意味動詞の```{verb_none}```は，特に[文型]({docs_sentence_pattern})で，動詞が必要ない場合など使われる．
一方，無意味修飾詞```{modifier_none}```は，あまり使われない．
これらの例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I am human.|{I_am_human}|
|I have an apple.|{I_have_an_apple}|

## 代名詞について

SFGPLでは[代名詞]({docs_pronoun})が存在する．
代名詞は次の表のようなものがある．

||English|SFGPL|
|:-:|:-:|:-:|
|一人称代名詞|I|{pronoun_I}|
|二人称代名詞|you|{pronoun_you}|
|三人称代名詞|he/she/it|{pronoun_he}|
|近称代名詞|this|{pronoun_proximal}|
|遠称代名詞|that|{pronoun_distal}|
|疑問代名詞|what|{pronoun_interrogative}|
|不定代名詞|something|{pronoun_indefinite}|

## 数値や論理的に使われる語

SFGPLには，[数値的な単語]({docs_Number})や[真偽値に関する単語]({docs_Bool})，[リストに関する単語]({docs_LangList})，[関数に関する単語]({docs_LangFunc})が存在している．
これらの単語は，一般的な文ではあまり使われないが，論理的なことを示す際に使われる．
