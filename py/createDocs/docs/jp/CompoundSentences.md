{page_header}

SFGPLでは1つの文の中に，複数のを組み合わせて表す文を作成することができる．

## 並列節

2つ以上の文を並列に接続するためには，[接続詞]({docs_Conjunction})が使用される．

SFGPLで，"I went to Tokyo and I was shopping there."を表すには次のようにする．

```SFGPL
{I_went_to_Tokyo_and_I_was_shopping_there_01}
```

また，英語のような時制の一致をするにはこのように節ごとに時制を活用させるが，SFGPLでは文全体に基本時制を活用させることができる．

```SFGPL
{I_went_to_Tokyo_and_I_was_shopping_there_02}
```

## 従属節

主節内の名詞に対して従属的に修飾するためには，その名詞の代わりにその名詞を説明する文を入れることで実現できる．
また，SFGPLでは一般的に，名詞を修飾する場合には従属節を使用することが多い．

### 一般的な従属節

SFGPLで，"My bag is big."を表すには次のようにする．
またこのときの"My bag"は，"I have a bag"であるというように表現する．
そしてこのとき，"bag"が修飾されている名詞であるため，その名詞には```{DeterminerN_stressed}```を付ける．

```SFGPL
{my_bag_is_big}
```

また，意味がほぼ同じである，"I have a bag is big."を表すには次のようにする．
またこのときは，"a bag is big"の"bag"は従属節の主語となっているため，```{DeterminerN_stressed}```を付けなくても良い．

```SFGPL
{I_have_a_bag_is_big}
```

そして，"I give you the desk I built."を表すには次のようにする．

```SFGPL
{I_give_you_the_desk_I_built}
```

このように従属節だけの時制を変えることもできる．

### 副詞節

副詞節で述語や文全体に対して修飾することができる．
SFGPLで"I ate sushi, when I went to Tokyo."を表すには次のようにする．

```SFGPL
{I_ate_sushi_when_I_went_to_Tokyo}
```

また，SFGPLで"I went grocery shopping while my kids were sleeping."を表すためには次のようにする．

```SFGPL
{I_went_grocery_shopping_while_my_kids_were_sleeping}
```

## 名詞による名詞の修飾

ある名詞XとYにおいて，YがXを修飾するとき，日本語では"YのX"，英語では"Y X"または"X of Y"と表されるがSFGPLでは，主に3種類の用法を使い分けて使用する．
SFGPLでは，先述のように，従属節で修飾をすることが多いが，名詞を名詞で修飾する場合も例外ではない．
そのため名詞の修飾方法は，```{noun_eq}```，```{noun_have}```と```{noun_belong}```で使い分けられる．

### Noun.eq ({noun_eq})

まず，```{noun_eq}```では，主に修飾語と被修飾語が同等のもののときに使われる．
例えば"This pen is big."をSFGPLで表すには次のようにする．

```SFGPL
{this_pen_is_big}
```

このとき，"this"と"pen"は同等のものを指している．
そのため，```{noun_eq}```が使われる．

### Noun.have ({noun_have})

次に，```{noun_have}```では，主に何かが何かを持ているときに使われる．
SFGPLで"My pen is big."を表すには次のようにする．

```SFGPL
{my_pen_is_big}
```

### Noun.belong ({noun_belong})

また，```{noun_belong}```では，主に何かがなにかに所属しているときに使われる．
SFGPLで"My school is big."を表すには次のようにする．

```SFGPL
{my_school_is_big}
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|go|{go}|
|to Tokyo|{to_Tokyo}|
|shop (Verb)|{shop_verb}|
|there|{there}|
|bag|{bag}|
|big|{big}|
|you|{you}|
|build|{build}|
|desk|{desk}|
|eat|{eat}|
|sushi|{sushi}|
|grocery|{grocery}|
|kid|{kid}|
|sleep|{sleep}|
|this|{this}|
|pen|{pen}|
|school|{school}|
