# 17. Bool関連クラス

[TOP](../../readme.md)
/
[EN](../en/Bool.md)

SFGPLにはBoolに関連したクラス，Bool型と，BoolList型が存在する．
これらのクラスは，真偽値や，数値などを表すために使われる．

## Bool型について

Bool型は，真偽を表すためのクラスである．
Bool型のFalseとTrueは次のように表される．

||word|
|:-:|:-:|
|False|pas|
|True|pos|

また，```pis```を使用して，Bool型と名詞を次のように接続することで，ある名詞に対する真偽を表すことができる．
次の文は"It is true that I am a student."という例を表す．
このような文では，全体がTrueとして継承される．

```SFGPL
pis ma ga so fa 'student' pos
```

そして，Bool型では，LangObjに備わっている，NOT ```pa```，OR ```be```，AND ```ba```，NOR ```bo```とNAND ```bu```を使用することもできる．
そして，それら関数は論理演算をすることができる．

たとえば，```True OR False```を表すには次のようになる．

```SFGPL
be pos pas
```

LangObjには通常のIFELSE```bi```の他に，logicIFELSE```ja```が存在する．
この単語により，条件を満たすかどうかで内部的に実行する文章（単語）を変えることができる．
"If true, I am a student."を表すには次のようにする．

```SFGPL
ja pos ma ga so fa 'student' pa ma ga so fa 'student'
```

## BoolList型について

BoolListでは，真偽値の配列を作成することができる．
BoolListには以下のような関数が存在している．

|単語|説明|
|:-:|:-:|
|fas|真偽のリスト（BoolList）を作成する|
|fes A B|BoolList(A)のB番目の値を取得する|
|fis A B|BoolList(A)に1つのBool(B)を末尾に加える|
|fus A B C|AというBoolListに対して，B番目からC番目までのリストを取得する|
|fos A B|2つのBoolList(A,B)を結合する|
|foas A|BoolList(A)の長さを取得する|
|mas A B|2つBoolの値(A,B)からなるBoolListを作成する|
|mis X1~X4|4つBoolの値(x1~x4)からなるBoolListを作成する|
|mos X1~X8|8つBoolの値(x1~x8)からなるBoolListを作成する|
|tas A|BoolList(A)を2進数の自然数とみなす|
|tes A|BoolList(A)を2進数の整数とみなす|
|tis A|BoolList(A)を2進数の浮動小数とみなす|
|tus A|BoolList(A)をASCII文字とみなす|

次のようにすることによって，4byteのデータを使用することができる．

```SFGPL
fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos
```

これは，2進数で```0100 0000 0100 1001 0000 1111 1101 1011```を表している．
また，次のようにすることで，数値として使うことができる．

|Type|SFGPL|Value|
|:-:|:-:|:-:|
|自然数|tas fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|1078530011|
|整数|tes fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|1078530011|
|浮動小数点|tis fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|3.1415927410125732|

## BoolListの日時表現

BoolListを利用して，Unix時間に基づく日時表現をすることができる．
日時表現はその精度によって以下の3種類存在する．

|SFGPL|Type|Unit|
|:-:|:-:|:-:|
|das|yyyy-mm-dd|Day|
|des|yyyy-mm-dd HH:MM:SS|Second|
|dis|yyyy-mm-dd HH:MM:SS.nnnnnnnnn|Nano Second|

これらの表現は```1970-01-01 00:00:00.000000000```が基準で，それぞれ日単位，秒単位，ナノ秒単位での差分によって日時を表す．

例えば，```2024-09-19 18:27:27```を```des```で表すには次のようにする．

まず，この時間のUnix時間は```1726738047```である．
これを2進数に変換すると，```0110 0110 1110 1011 1110 1110 0111 1111```となる．
そのためBoolListに変換すると次のようになる．

```SFGPL
fos fos mos pas pos pos pas pas pos pos pas mos pos pos pos pas pos pas pos pos fos mos pos pos pos pas pos pos pos pas mos pas pos pos pos pos pos pos pos
```

さらに，```des```を使用して日時に変換すると次のようになる．

```SFGPL
des fos fos mos pas pos pos pas pas pos pos pas mos pos pos pos pas pos pas pos pos fos mos pos pos pos pas pos pos pos pas mos pas pos pos pos pos pos pos pos
```

これによって，```2024-09-19 09:27:27```をSFGPLで表すことができる．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I am a student|ma ga so fa 'student'|
