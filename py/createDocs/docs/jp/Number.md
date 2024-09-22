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

### 数値計算

そして，次の表のようにNumberListでは四則演算等の数値計算を行う関数が存在する．

||Python|SFGPL|
|:-:|:-:|:-:|
|Addition|```A+B```|{NumberList_calcAdd} A B|
|Subtraction|```A-B```|{NumberList_calcSub} A B|
|Multiplication|```A*B```|{NumberList_calcMul} A B|
|Division|```A/B```|{NumberList_calcDiv} A B|
|Power|```A**B```|{NumberList_calcPow} A B|
|Int Division|```A//B```|{NumberList_calcIntDiv} A B|
|Remainder|```A%B```|{NumberList_calcMod} A B|
|Minus|```-A```|{NumberList_minus} A|
|Absolute value|```abs(A)```|{NumberList_abs} A|

### BoolListとNumberListの相互変換

次の表のようにBoolListとNumberListを相互に変換する関数が存在する．

|Type|SFGPL|from|to|
|:-:|:-:|:-:|:-:|
|Int|{NumberList_IntNL2BL}|NumberList|BoolList|
|Int|{BoolList_IntBL2NL}|BoolList|NumberList|
|Float|{NumberList_FloatNL2BL}|NumberList|BoolList|
|Float|{BoolList_FloatBL2NL}|BoolList|NumberList|

#### 整数型における相互変換

整数として相互変換する関数```{NumberList_IntNL2BL}```と```{BoolList_IntBL2NL}```が存在する．
これらの変換で扱われる数値は，BoolListを整数型(```{BoolList_Int}```)として見做される．
つまり，このときのBoolListの値は，2進数の2の補数表現方法と同等である．
これらの値は，NumberListによって，四則演算等の数値計算が行われた場合も適応できる．
ただし，NumberListが除算結果などにより実数となっている場合は，変換ができずエラーとなる．

#### 浮動小数点型（実数）における相互変換

浮動小数点（実数）として相互変換する関数```{NumberList_FloatNL2BL}```と```{BoolList_FloatBL2NL}```が存在する．
これらの変換で扱われる数値は，BoolListを浮動小数点型(```{BoolList_Float}```)として見做される．
つまり，このときのBoolListの値は，IEEE754における半精度，単精度，倍精度，四倍精度の浮動小数点表現方法が用いられる．
また，NumberListからBoolListに変換する際には，64bitの倍精度浮動小数点数として変換され，BoolListに格納される．

### 実数の扱い方

実数を扱うためには，NumberListの除算(```{NumberList_calcDiv}```)を使用する方法と，BoolListで浮動小数点数を表しそれをNumberListに変換する方法がある．

例えば3.14を除算によって表すには次のようにする．

```SFGPL
{real_number_3_14_div}
```

同様に，3.14を倍精度浮動小数点で表す場合は次のようにする．

```SFGPL
{real_number_3_14_bl}
```

### 正の数の判定

NumberListで正の数かを判定するには，```{NumberList_isPN}```を使用する．
これによって，SFGPLのBool型が出力され，0以上の数の場合が```{Bool_true}```と同値になる．
例えば，4と-4の2つの場合において正の整数か判定するには次のようにする．

```SFGPL
{isPN_4}
{isPN_-4}
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|apple|{apple}|
|Japan|{Japan}|
|people|{people}|
