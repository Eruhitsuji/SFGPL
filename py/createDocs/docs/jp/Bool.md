{page_header}

SFGPLにはBoolに関連したクラス，Bool型と，BoolList型が存在する．
これらのクラスは，真偽値や，数値などを表すために使われる．

## Bool型について

Bool型は，真偽を表すためのクラスである．
Bool型のFalseとTrueは次のように表される．

||word|
|:-:|:-:|
|False|{Bool_false}|
|True|{Bool_true}|

また，```{Bool_B2N}```を使用して，Bool型と名詞を次のように接続することで，ある名詞に対する真偽を表すことができる．
次の文は"It is true that I am a student."という例を表す．
このような文では，全体がTrueとして継承される．

```SFGPL
{It_is_true_that_I_am_a_student}
```

そして，Bool型では，LangObjに備わっている，NOT ```{LangObj_NOT}```，OR ```{LangObj_OR}```，AND ```{LangObj_AND}```，NOR ```{LangObj_NOR}```とNAND ```{LangObj_NAND}```を使用することもできる．
そして，それら関数は論理演算をすることができる．

たとえば，```True OR False```を表すには次のようになる．

```SFGPL
{true_or_false}
```

LangObjには通常のIFELSE```{LangObj_IFELSE}```の他に，logicIFELSE```{LangObj_logicIFELSE}```が存在する．
この単語により，条件を満たすかどうかで内部的に実行する文章（単語）を変えることができる．
"If true, I am a student."を表すには次のようにする．

```SFGPL
{If_true_I_am_a_student}
```

## BoolList型について

BoolListでは，真偽値の配列を作成することができる．
BoolListには以下のような関数が存在している．

|単語|説明|
|:-:|:-:|
|{BoolList}|真偽のリスト（BoolList）を作成する|
|{BoolList_get} A B|BoolList(A)のB番目の値を取得する|
|{BoolList_append} A B|BoolList(A)に1つのBool(B)を末尾に加える|
|{BoolList_slice} A B C|AというBoolListに対して，B番目からC番目までのリストを取得する|
|{BoolList_add} A B|2つのBoolList(A,B)を結合する|
|{BoolList_len} A|BoolList(A)の長さを取得する|
|{BoolList_twoBit} A B|2つBoolの値(A,B)からなるBoolListを作成する|
|{BoolList_fourBit} X1~X4|4つBoolの値(x1~x4)からなるBoolListを作成する|
|{BoolList_byte} X1~X8|8つBoolの値(x1~x8)からなるBoolListを作成する|
|{BoolList_NaturalNum} A|BoolList(A)を2進数の自然数とみなす|
|{BoolList_Int} A|BoolList(A)を2進数の整数とみなす|
|{BoolList_Float} A|BoolList(A)を2進数の浮動小数とみなす|
|{BoolList_ASCII} A|BoolList(A)をASCII文字とみなす|

次のようにすることによって，4byteのデータを使用することができる．

```SFGPL
{bin_0100_0000_0100_1001_0000_1111_1101_1011}
```

これは，2進数で```0100 0000 0100 1001 0000 1111 1101 1011```を表している．
また，次のようにすることで，数値として使うことができる．
浮動小数点は，IEEE 754の半精度，単精度，倍精度，四倍精度に対応している．
そのため，それぞれ16bit，32bit，64bit，128bitで表す必要がある．

|Type|SFGPL|Value|
|:-:|:-:|:-:|
|自然数|{NN_b1}|{NN_b1_get}|
|整数|{INT_b1}|{INT_b1_get}|
|浮動小数点|{Float_b1}|{Float_b1_get}|

## BoolListの日時表現

BoolListを利用して，Unix時間に基づく日時表現をすることができる．
日時表現はその精度によって以下の3種類存在する．

|SFGPL|Type|Unit|
|:-:|:-:|:-:|
|{BoolList_UnixTimeD}|yyyy-mm-dd|Day|
|{BoolList_UnixTimeDT}|yyyy-mm-dd HH:MM:SS|Second|
|{BoolList_UnixTimeDTN}|yyyy-mm-dd HH:MM:SS.nnnnnnnnn|Nano Second|

これらの表現は```1970-01-01 00:00:00.000000000```が基準で，それぞれ日単位，秒単位，ナノ秒単位での差分によって日時を表す．
また，これらはUTC時間が基準となっている．

例えば，```2024-09-19 09:27:27```を```{BoolList_UnixTimeDT}```で表すには次のようにする．

まず，この時間のUnix時間は```1726738047```である．
これを2進数に変換すると，```0110 0110 1110 1011 1110 1110 0111 1111```となる．
そのためBoolListに変換すると次のようになる．

```SFGPL
{bin_0110_0110_1110_1011_1110_1110_0111_1111}
```

さらに，```{BoolList_UnixTimeDT}```を使用して日時に変換すると次のようになる．

```SFGPL
{dt_bin_0110_0110_1110_1011_1110_1110_0111_1111}
```

これによって，```{dt_bin_0110_0110_1110_1011_1110_1110_0111_1111_str}```をSFGPLで表すことができる．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I am a student|{I_am_a_student}|
