# 4. 否定文と否定表現

[TOP](../../readme.md)
/
[EN](../en/negativeSentence.md)

## 否定文

否定文を作成するためには```pa```を使用する．
この語は，文章に付属することで否定文を作る．
"I have a table."はSFGPLでは```mi ga so fa 'table'```である．
それを否定文の"I don't have a table."という意味にする場合，SFGPLでは次のように表現できる．

```SFGPL
pa mi ga so fa 'table'
```

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
|big|wan|
