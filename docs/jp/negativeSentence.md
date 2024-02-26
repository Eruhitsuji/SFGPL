# 4. 否定文と否定表現

[TOP](../../readme.md)
/
[EN](../en/negativeSentence.md)

## 否定文

通常の否定文を作成するためには```pa```を使用する．
この語は，文章に付属することで否定文を作る．
"I have a table."はSFGPLでは```mi ga so fa 'table'```である．
この文の全体を否定し，否定文の"I don't have a table."という意味にする場合，SFGPLでは次のように表現できる．

```SFGPL
pa mi ga so fa 'table'
```

## 動詞の否定

SFGPLでは，文章全体を否定する以外に動詞だけを否定することもできる．
文章全体を否定する場合と動詞だけを否定する場合は，意味が異なる場合がある．
特に英語などの衛星枠付け言語では，それぞれの意味の解釈が異なる場合がある．

例えば，次のように"I don't make a table."という場合は，文全体の否定と動詞のみの否定の意味がほとんど同義である．

|||
|:-:|:-:|
|文全体|pa te ga sa 'make' fa 'table'|
|動詞のみ|te ga pa sa 'make' fa 'table'|

また，次のように"I didn't run to my school."では，文全体の否定と動詞のみの否定の意味が異なる．

|||
|:-:|:-:|
|文全体|di pa ta ga na sa 'run' li pun mu ga so san fa 'school'|
|動詞のみ|di ta ga na pa sa 'run' li pun mu ga so san fa 'school'|

文章全体の否定の場合では，「私は学校に走って行った」以外の事象すべてを表している，
つまり，「私は学校に歩いて行った」や「私は学校に行かなかった」などの意味も含意している．

しかし，動詞のみの否定の場合では，「私は学校に行く」事象の中で「走る」以外の行動をしたという意味になる．
つまり，「私は学校に歩いて行った」などの他の手段である場合は含意するが，「私は学校に行かなかった」は含意しない．

一方で日本語などの動詞枠付け言語では，「走って行く」などの複合動詞によって表現するため，このような意味の差異がなくなる傾向がある．
このときの「走って行く」という複合動詞では，英語と違い「走る」という動作の手法と「行く」という動作の結果が含まれている．

## 修飾語の否定形

ある修飾語において，```ke```を付けることによって，その修飾語の対義語を表すことができる．

例えば，"big"という意味の```wan```に対する対義語の"small"を表す場合，```ke wan```とすることで表すことができる．

"My table is small."をSFGPLで表すと次のようになる．

```SFGPL
me mi ga so san fa 'table' so ke wan
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|table|fa 'table'|
|make|sa 'make'|
|run|sa 'run'|
|my school|mu ga so san fa 'school'|
|big|wan|
