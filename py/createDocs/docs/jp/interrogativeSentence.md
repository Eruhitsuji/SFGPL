# 疑問文

[TOP](../../readme.md)
/
[EN](../en/interrogativeSentence.md)

疑問文を作成するためには```{phrase_interrogative}```を使用する．
この単語を文につけると疑問文になる．
"You have a table."はSFGPLでは```{you_have_a_table}```である．
それを疑問文の"Do you have a table?"という意味にする場合，SFGPLでは次のように表現できる．

```SFGPL
{do_you_have_a_table}
```

また，疑問詞を含む疑問文の場合，不定のところを疑問詞に置き換えることで表す．

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
|who|{who}|
|what|{what}|
