# 7. 複文

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

### 一般的な従属節

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

### 副詞節

副詞節で述語や文全体に対して修飾することができる．
SFGPLで"I ate sushi, when I went to Tokyo."を表すには次のようにする．

```SFGPL
di te ga na sa 'eat' li ta ga na sa 'go' li pun fa 'Tokyo' fa 'sushi'
```

また，SFGPLで"I went grocery shopping while my kids were sleeping."を表すためには次のようにする．

```SFGPL
di ta ga na sa 'go' ba li ma fi ni sa 'shop' so fa 'grocery' li ta mi ga so san don fa 'kid' ni sa 'sleep'
```

## 名詞による名詞の修飾

ある名詞XとYにおいて，YがXを修飾するとき，日本語では"YのX"，英語では"Y X"または"X of Y"と表されるがSFGPLでは，主に3種類の用法を使い分けて使用する．
SFGPLでは，先述のように，従属節で修飾をすることが多いが，名詞を名詞で修飾する場合も例外ではない．
そのため名詞の修飾方法は，```ma```，```mi```と```mu```で使い分けられる．

### Noun.eq (ma)

まず，```ma```では，主に修飾語と被修飾語が同等のもののときに使われる．
例えば"This pen is big."をSFGPLで表すには次のようにする．

```SFGPL
me ma gu so san fa 'pen' so wan
```

このとき，"this"と"pen"は同等のものを指している．
そのため，```ma```が使われる．

### Noun.have (mi)

次に，```mi```では，主に何かが何かを持ているときに使われる．
SFGPLで"My pen is big."を表すには次のようにする．

```SFGPL
me mi ga so san fa 'pen' so wan
```

### Noun.belong (mu)

また，```mu```では，主に何かがなにかに所属しているときに使われる．
SFGPLで"My school is big."を表すには次のようにする．

```SFGPL
me mu ga so san fa 'school' so wan
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
|grocery|fa 'grocery'|
|kid|fa 'kid'|
|sleep|sa 'sleep'|
|this|gu|
|pen|fa 'pen'|
|school|fa 'school'|
