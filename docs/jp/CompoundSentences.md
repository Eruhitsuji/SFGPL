# 6. 複文

[TOP](../../readme.md)
/
[EN](../en/CompoundSentences.md)

SFGPLでは1つの文の中に，複数のを組み合わせて表す文を作成することができる．

## 並列節

2つ以上の文を並列に接続するためには，[接続詞](Conjunction.md)が使用される．

SFGPLで，"I went to Tokyo and I was shopping there."を表すには次のようにする．

```SFGPL
ba di ta ga na sa 'go' li pun fa 'Tokyo' di ta ga na ni sa 'shop' li pun gu
```

また，英語のような時制の一致をするにはこのように節ごとに時制を活用させるが，SFGPLでは文全体に基本時制を活用させることができる．

```SFGPL
di ba ta ga na sa 'go' li pun fa 'Tokyo' ta ga na ni sa 'shop' li pun gu
```

## 従属節

主節内の名詞に対して従属的に修飾するためには，その名詞の代わりにその名詞を説明する文を入れることで実現できる．
また，SFGPLでは一般的に，名詞を修飾する場合には従属節を使用することが多い．

SFGPLで，"My bag is big."を表すには次のようにする．
またこのときの"My bag"は，"I have a bag"であるというように表現する．
そしてこのとき，"bag"が修飾されている名詞であるため，その名詞には```san```を付ける．

```SFGPL
me mi ga so san fa 'bag' so wan
```

また，意味がほぼ同じである，"I have a bag is big."を表すには次のようにする．
またこのときは，"a bag is big"の"bag"は従属節の主語となっているため，```san```を付けなくても良い．

```SFGPL
mi ga so me fa 'bag' so wan
```

そして，"I give you the desk I built."を表すには次のようにする．

```SFGPL
ti ga so ge di te ga sa 'build' san fa 'desk'
```

このように従属節だけの時制を変えることもできる．

さらに，副詞節で述語や文全体に対して修飾することができる．
SFGPLで"I ate sushi, when I went to Tokyo."を表すには次のようにする．

```SFGPL
di te ga na sa 'eat' li ta ga na sa 'go' li pun fa 'Tokyo' fa 'sushi'
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|go|sa 'go'|
|to Tokyo|li pun fa 'Tokyo'|
|shop (Verb)|sa 'shop'|
|there|pun gu|
|bag|fa 'bag'|
|big|wan|
|you|ge|
|build|sa 'build'|
|desk|fa 'desk'|
|eat|sa 'eat'|
|sushi|fa 'sushi'|
