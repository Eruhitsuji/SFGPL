# 21. 数字の表現方法

[TOP](../../readme.md)
/
[EN](../en/Number.md)

SFGPLでは10進数の数値を表すために，NumberとNumberListクラスが存在する．

## Numberクラス

Numberクラスは，基数詞用のクラスであり，単体では使用されない．
このクラスでは以下の表のように，0~9までの値が定義されている．

|Meaning|SFGPL|
|:-:|:-:|
|0|pal|
|1|pel|
|2|pil|
|3|pul|
|4|pol|
|5|bal|
|6|bel|
|7|bil|
|8|bul|
|9|bol|

## NumberListクラス

通常の数詞として使う場合にはNumberListクラスを使用する．
このクラスは基数詞のデータをリストに格納することができる．
数値の表現方法は，大きい桁から順に0番目から格納し，10進数の数値を表す．

NumberListクラスにはリスト型の関数として次の表のようなものが存在する．
ただしこれらの関数は，下記に記述する数値計算した後のNumberListには適用することができない．

|単語|説明|
|:-:|:-:|
|fal|NumberのリストNumberListを作成する|
|fel A B|NumberList(A)のB番目の値を取得する|
|fil A B|NumberListに1つのNumberを末尾に加える|
|ful A B C|AというNumberListに対して，B番目からC番目までのリストを取得する|
|fol A B|2つのNumberListを結合する|
|foal A|NumberList(A)の長さを取得する|

また，1~5桁の整数を作るためには，以下の表のような専用の関数が用意されている．

|単語|説明|
|:-:|:-:|
|mal|10進数1桁からなるNumberListを作成する|
|mel|10進数2桁からなるNumberListを作成する|
|mil|10進数3桁からなるNumberListを作成する|
|mul|10進数4桁からなるNumberListを作成する|
|mol|10進数5桁からなるNumberListを作成する|

SFGPLで，"I have five apples."を表すには次のようにする．

```SFGPL
mi ga so ma fa 'apple' so mal bal
```

また，"I have fifteen apples."を表すには次のようにする．

```SFGPL
mi ga so ma fa 'apple' so mel pel bal
```

さらに，10進数で5桁より大きな数値を表すためには，次のように```fol```を使い，2つのNumberListを結合することで実現できる．
次の文はSFGPLで"Japan has 125416877 people."を表している．

```SFGPL
mi fa 'Japan' so ma fa 'people' so fol mul pel pil bal pol mol pel bel bul bil bil
```

### 数値計算

そして，次の表のようにNumberListでは四則演算等の数値計算を行う関数が存在する．

||SFGPL|
|:-:|:-:|
|Addition|tal|
|Subtraction|tel|
|Multiplication|til|
|Division|tul|
|Power|dal|
|Int Division|del|
|Remainder|dil|

### 実数の扱い方

実数を扱うには除算を利用する．
例えば3.14を表すには次のようにする．

```SFGPL
tul mil pul pel pol mil pel pal pal
```

### BoolListとNumberListの相互変換

次の表のようにBoolListとNumberListを相互に変換する関数が存在する．

|Type|SFGPL|from|to|
|:-:|:-:|:-:|:-:|
|Int|tol|NumberList|BoolList|
|Int|tos|BoolList|NumberList|
|Float|dol|NumberList|BoolList|
|Float|dos|BoolList|NumberList|

#### 整数型における相互変換

整数として相互変換する関数```tol```と```tos```が存在する．
これらの変換で扱われる数値は，BoolListを整数型(```tes```)として見做される．
つまり，このときのBoolListの値は，2進数の2の補数表現方法と同等である．
これらの値は，NumberListによって，四則演算等の数値計算が行われた場合も適応できる．
ただし，NumberListが除算結果などにより実数となっている場合は，変換ができずエラーとなる．

#### 浮動小数点型（実数）における相互変換

浮動小数点（実数）として相互変換する関数```dol```と```dos```が存在する．
これらの変換で扱われる数値は，BoolListを浮動小数点型(```tis```)として見做される．
つまり，このときのBoolListの値は，IEEE754における半精度，単精度，倍精度，四倍精度の浮動小数点表現方法が用いられる．
また，NumberListからBoolListに変換する際には，64bitの倍精度浮動小数点数として変換され，BoolListに格納される．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|apple|fa 'apple'|
|Japan|fa 'Japan'|
|people|fa 'people'|
