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
