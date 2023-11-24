{page_header}

## 修飾語について

SFGPLには形容詞と副詞の違いがなく，修飾する語はすべて修飾語となる．

修飾語は，修飾の反対の意を表すための単語が用意されている．
それによって，英語の"big"に対応する```{WordM_big}```を```{Neg_WordM_big}```とすることで，"small"という意味にすることができる．

## 比較表現

SFGPLには2項の名詞に対しての比較を行う文の```{Noun_gt}```が存在する．
```{Noun_gt} A F B C```で，"AはCよりBである．"という意味となる．

## 各品詞に対する修飾語

各品詞を単純に修飾語で修飾するためには，次の表になる．

||SFGPL|
|:-:|:-:|
|Noun|{Modifier_N} Noun Modifier|
|Verb|{Modifier_V} Verb Modifier|
|Modifier|{Modifier_M} Modifier Modifier|

## 修飾語の応用

修飾語では，英語の前置詞と名詞含む句を修飾語として代用する事ができる．
このとき，名詞を修飾語に変換する```{Modifier_N2M}```と，[名詞限定詞]({docs_DeterminerN})がよく組み合わされて表現される．
例えば，"I live in Tokyo."と表す場合は，次のように表せる．

```SFGPL
{I_live_in_Tokyo}
```

また，```{DeterminerN_place}```は，場所を表す限定詞である．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|live|{live}|
|in Tokyo|{in_Tokyo}|
