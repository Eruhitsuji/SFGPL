# 単語

[TOP](../../readme.md)
/
[EN](../en/Word.md)

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

SFGPLには[名詞限定詞](DeterminerN.md)が存在する．
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

```fo```では，[名詞限定詞](DeterminerN.md)をそのままの意味で表すときによく使われる．
また，```so```は，特に[文型](sentence_pattern.md)で，動詞が必要ない場合など使われる．
一方，```lo```は，あまり使われない．
これらの例を次に表す．

|English|SFGPL|
|:-:|:-:|
|I am human.|ma ga so ben fo|
|I have an apple.|mi ga so fa 'apple'|

## 代名詞について

SFGPLでは[代名詞](pronoun.md)が存在する．
