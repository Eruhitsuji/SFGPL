# Bool関連クラス

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
|False|{Bool_false}|
|True|{Bool_true}|

また，```{Bool_B2N}```を使用して，Bool型と名詞を次のように接続することで，ある名詞に対する真偽を表すことができる．
次の文は"It is true that I am a student."という例を表す．

```SFGPL
{It_is_true_that_I_am_a_student}
```

そして，Bool型では，LangObjに備わっている，NOT ```{LangObj_NOT}```，OR ```{LangObj_OR}```，AND ```{LangObj_AND}```，NOR ```{LangObj_NOR}```とNAND ```{LangObj_NAND}```を使用することもできる．
そして，それら関数は論理演算をすることができる．

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

|Type|SFGPL|Value|
|:-:|:-:|:-:|
|自然数|{NN_b1}|{NN_b1_get}|
|整数|{INT_b1}|{INT_b1_get}|
|浮動小数点|{Float_b1}|{Float_b1_get}|

## 単語集

|English|SFGPL|
|:-:|:-:|
|I am a student|{I_am_a_student}|
