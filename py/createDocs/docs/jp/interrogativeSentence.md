{page_header}

## 諾否疑問文

疑問文を作成するためには```{phrase_interrogative}```を使用する．
この単語を文につけると疑問文になる．
"You have a table."はSFGPLでは```{you_have_a_table}```である．
それを疑問文の"Do you have a table?"という意味にする場合，SFGPLでは次のように表現できる．

```SFGPL
{do_you_have_a_table}
```

このような疑問文を返答する場合は次のように，Bool.B2N```{Bool_B2N}```を使用して命題が正か偽かを示すことで表す．

```SFGPL
{yes_I_have_it}
{no_I_dont_have_it}
```

## 疑問詞疑問文

また，疑問詞を含む疑問文の場合，不定のところを疑問詞に置き換えることで表す．
疑問詞は疑問代名詞```{pronoun_interrogative}```と[名詞限定詞]({docs_DeterminerN})を組み合わせて表す．

"Who has a table?"は次のように表す．

```SFGPL
{who_has_a_table}
```

"What do you have?"は次のように表す．

```SFGPL
{what_do_you_have}
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|you|{you}|
|table|{table}|
|true|{Bool_true}|
|false|{Bool_false}|
|who|{who}|
|what|{what}|
