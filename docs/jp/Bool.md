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
|False|pas|
|True|pos|

また，```pis```を使用して，Bool型と名詞を次のように接続することで，ある名詞に対する真偽を表すことができる．
次の文は"It is true that I am a student."という例を表す．

```SFGPL
pis ma ga so fa 'student' pos
```

そして，Bool型では，LangObjに備わっている，```pa```，```be```，```ba```，```bo```と```bu```を使用することもできる．
そして，それらは，論理演算をすることができる．

## BoolList型について

BoolListでは，真偽値の配列を作成することができる．
BoolListには以下のような関数が存在している．

|単語|説明|
|:-:|:-:|
|fas|真偽のリスト（BoolList）を作成する|
|fis A B|BoolListに1つのBoolを末尾に加える|
|fos A B|2つのBoolListを結合する|
|mas A B|2つBoolの値からなるBoolListを作成する|
|mis X1~X4|4つBoolの値からなるBoolListを作成する|
|mos X1~X8|8つBoolの値からなるBoolListを作成する|
|tas A|BoolListを2進数の自然数とみなす|
|tes A|BoolListを2進数の整数とみなす|
|tis A|BoolListを2進数の浮動小数とみなす|
|tus A|BoolListをアスキー文字とみなす|

次のようにすることによって，4byteのデータを使用することができる．

```SFGPL
fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos
```

また，次のようにすることで，数値として使うことができる．

|Type|SFGPL|Value|
|:-:|:-:|:-:|
|自然数|tas fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|1078530011|
|整数|tes fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|1078530011|
|浮動小数点|tis fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|3.1415927410125732|

## 単語集

|English|SFGPL|
|:-:|:-:|
|I am a student|ma ga so fa 'student'|
