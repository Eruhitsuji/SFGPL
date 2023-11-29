{page_header}

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

## 動詞から名詞

動詞から名詞は"This is building."のように使用される．

```SFGPL
{this_is_building}
```

また元の単語の動詞は[動詞の活用]({docs_verbConjugation})に従って事前に活用させることも可能である．

## 名詞から修飾語

名詞から修飾語は，英語の前置詞と名詞が組み合わされた句と同等の意味を作成するときに使われる．
またそのときは，```{N2M}```と限定詞([DeterminerN]({docs_DeterminerN}))が組み合わされて使用する．
"I live in Tokyo."をSFGPLにすると次のようになる．
このとき，```{determinerN_place}```は場所を表す限定詞である．

```SFGPL
{I_live_in_Tokyo}
```

また，名詞を抽象化する単語の```{determinerN_abstract}```と組み合わせることで，"～的な"という意味にすることができる．
"My daughter has a cat-like stuffed toy."をSFGPLで表すには次のようになる．

```SFGPL
{my_daughter_has_a_cat_like_stuffed_toy}
```

## 動詞から修飾語

動詞から修飾語に変換すると，印欧語族に多く見られる分詞に相当する用法を使用できる．
また元の単語の動詞は[動詞の活用]({docs_verbConjugation})に従って事前に活用させることも可能である．

"There is a sleeping boy."をSFGPLで表すには次のようにする．

```SFGPL
{there_is_a_sleeping_boy}
```

また，"I lived in that destroyed building."を表すには次のように表現する．

```SFGPL
{I_lived_in_that_destroyed_building}
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|this|{this}|
|build|{build}|
|I|{I}|
|live|{live}|
|in Tokyo|{in_Tokyo}|
|daughter|{daughter}|
|cat|{cat}|
|stuffed|{stuffed}|
|toy|{toy}|
|there|{there}|
|sleep|{sleep}|
|boy|{boy}|
|that|{that}|
|destroy|{destroy}|
