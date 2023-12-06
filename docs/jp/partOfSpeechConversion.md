# 11. 品詞変換

[TOP](../../readme.md)
/
[EN](../en/partOfSpeechConversion.md)

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

## 動詞から名詞

動詞から名詞は"This is building."のように使用される．

```SFGPL
ma gu so fi sa 'build'
```

また元の単語の動詞は[動詞の活用](verbConjugation.md)に従って事前に活用させることも可能である．

## 名詞から修飾語

名詞から修飾語は，英語の前置詞と名詞が組み合わされた句と同等の意味を作成するときに使われる．
またそのときは，```li```と限定詞([DeterminerN](DeterminerN.md))が組み合わされて使用する．
"I live in Tokyo."をSFGPLにすると次のようになる．
このとき，```pun```は場所を表す限定詞である．

```SFGPL
ta ga na sa 'live' li pun fa 'Tokyo'
```

また，名詞を抽象化する単語の```son```と組み合わせることで，"～的な"という意味にすることができる．
"My daughter has a cat-like stuffed toy."をSFGPLで表すには次のようになる．

```SFGPL
mi mi ga so san fa 'daughter' so me me fa 'toy' so lu ne sa 'stuff' so li son fa 'cat'
```

## 動詞から修飾語

動詞から修飾語に変換すると，印欧語族に多く見られる分詞に相当する用法を使用できる．
また元の単語の動詞は[動詞の活用](verbConjugation.md)に従って事前に活用させることも可能である．

"There is a sleeping boy."をSFGPLで表すには次のようにする．

```SFGPL
ma pun go so me fa 'boy' so lu ni sa 'sleep'
```

また，"I lived in that destroyed building."を表すには次のように表現する．

```SFGPL
di ta ga na sa 'live' li pun ma go so san me fi sa 'build' so lu ne sa 'destroy'
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|this|gu|
|build|sa 'build'|
|I|ga|
|live|sa 'live'|
|in Tokyo|li pun fa 'Tokyo'|
|daughter|fa 'daughter'|
|cat|fa 'cat'|
|stuffed|lu ne sa 'stuff'|
|toy|fa 'toy'|
|there|pun go|
|sleep|sa 'sleep'|
|boy|fa 'boy'|
|that|go|
|destroy|sa 'destroy'|
