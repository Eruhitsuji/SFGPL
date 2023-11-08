# 品詞変換

[TOP](../../readme.md)
/
[EN](../en/partOfSpeechConversion.md)

SFGPLでは，名詞，動詞，修飾語の相互の品詞を変換することができる．
以下の表はSFGPLで品詞変換する語の一覧である．

||変換前の品詞|変換後の品詞|単語|
|:-:|:-:|:-:|:-:|
|V2N|動詞|名詞|{V2N}|
|M2N|修飾語|名詞|{M2N}|
|M2V|修飾語|動詞|{M2V}|
|N2V|名詞|動詞|{N2V}|
|N2M|名詞|修飾語|{N2M}|
|V2M|動詞|修飾語|{V2M}|

特に，動詞から名詞，名詞から修飾語はよく使用される．
動詞から名詞は"This is building."のように使用される．

```SFGPL
{this_is_building}
```

また，名詞から修飾語は，英語の前置詞と名詞が組み合わされた句と同等の意味を作成するときに使われる．
またそのときは，```{N2M}```と限定詞([DeterminerN](DeterminerN.md))が組み合わされて使用する．
"I live in Tokyo."をSFGPLにすると次のようになる．
このとき，```{determinerN_place}```は場所を表す限定詞である．

```SFGPL
{I_live_in_Tokyo}
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|this|{this}|
|building|{building}|
|I|{I}|
|live|{live}|
|in Tokyo|{in_Tokyo}|
