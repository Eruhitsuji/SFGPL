{page_header}

SFGPLでは10進数の数値を表すために，NumberとNumberListクラスが存在する．

## Numberクラス

Numberクラスは，基数詞用のクラスであり，単体では使用されない．
このクラスでは以下の表のように，0~9までの値が定義されている．

|Meaning|SFGPL|
|:-:|:-:|
|0|{number_zero}|
|1|{number_one}|
|2|{number_two}|
|3|{number_three}|
|4|{number_four}|
|5|{number_five}|
|6|{number_six}|
|7|{number_seven}|
|8|{number_eight}|
|9|{number_nine}|

## NumberListクラス

通常の数詞として使う場合にはNumberListクラスを使用する．
このクラスは基数詞のデータをリストに格納することができる．
数値の表現方法は，大きい桁から順に0番目から格納し，10進数の数値を表す．

NumberListクラスにはリスト型の関数として次の表のようなものが存在する．
ただしこれらの関数は，下記に記述する数値計算した後のNumberListには適用することができない．

|単語|説明|
|:-:|:-:|
|{NumberList}|NumberのリストNumberListを作成する|
|{NumberList_get} A B|NumberList(A)のB番目の値を取得する|
|{NumberList_append} A B|NumberListに1つのNumberを末尾に加える|
|{NumberList_slice} A B C|AというNumberListに対して，B番目からC番目までのリストを取得する|
|{NumberList_add} A B|2つのNumberListを結合する|
|{NumberList_len} A|NumberList(A)の長さを取得する|

また，1~5桁の整数を作るためには，以下の表のような専用の関数が用意されている．

|単語|説明|
|:-:|:-:|
|{NumberList_digit1}|10進数1桁からなるNumberListを作成する|
|{NumberList_digit2}|10進数2桁からなるNumberListを作成する|
|{NumberList_digit3}|10進数3桁からなるNumberListを作成する|
|{NumberList_digit4}|10進数4桁からなるNumberListを作成する|
|{NumberList_digit5}|10進数5桁からなるNumberListを作成する|

SFGPLで，"I have five apples."を表すには次のようにする．

```SFGPL
{I_have_five_apples}
```

また，"I have fifteen apples."を表すには次のようにする．

```SFGPL
{I_have_fifteen_apples}
```

さらに，10進数で5桁より大きな数値を表すためには，次のように```{NumberList_add}```を使い，2つのNumberListを結合することで実現できる．
次の文はSFGPLで"Japan has 125416877 people."を表している．

```SFGPL
{Japan_has_125416877_people}
```

### 四則演算

そして，次の表のようにNumberListでは四則演算を行う関数が存在する．

||SFGPL|
|:-:|:-:|
|Addition|{NumberList_calcAdd}|
|Subtraction|{NumberList_calcSub}|
|Multiplication|{NumberList_calcMul}|
|Division|{NumberList_calcDiv}|

### 実数の扱い方

実数を扱うには除算を利用する．
例えば3.14を表すには次のようにする．

```SFGPL
{real_number_3_14}
```

### BoolListとNumberListの相互変換

加えて，次の表のように整数のBoolListとNumberListを相互に変換する関数が存在する．

|SFGPL|from|to|
|:-:|:-:|:-:|
|{NumberList_IntNL2BL}|NumberList|BoolList|
|{BoolList_IntBL2NL}|BoolList|NumberList|

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|apple|{apple}|
|Japan|{Japan}|
|people|{people}|
