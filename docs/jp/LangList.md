# 18. LangList

[TOP](../../readme.md)
/
[EN](../en/LangList.md)

SFGPLでは基本的なデータ構造型として，LangList型が存在する．
LangListには，以下の関数が存在している．

|単語|説明|
|:-:|:-:|
|fat|LangObjのリストLangListを作成する|
|fet A B|LangList(A)のB番目の値を取得する|
|fit A B|LangList(A)に1つのLangObj(B)を末尾に加える|
|fut A B C|AというLangListに対して，B番目からC番目までのリストを取得する|
|fot A B|2つのLangListを結合する|
|foat A|LangList(A)の長さを取得する|
|tat A B C|LangListを使用した繰り返し用の関数|
|tet A B|LangListの全要素に対して一定の処理を行う関数|

LangListは，LangObjを継承しているすべてのクラスを格納することができる．
次はLangListをappendを使用して作成する一例である．

```SFGPL
fit fit fit fit fit fat ga fa 'pen' sa 'go' la 'happy' ma ga so fa 'student'
```

また，このLangListから最初の値を取得するには次のようにする．
このとき```fis fas pas```は[BoolList](Bool.md)における0を表している．

```SFGPL
fet fit fit fit fit fit fat ga fa 'pen' sa 'go' la 'happy' ma ga so fa 'student' fis fas pas
```

## LangListでの繰り返し処理

LangListを繰り返し処理するための```tat```を使用することでLangListを使用した繰り返し処理を行うことができる．
以下に表す*x*はすべて同じLangListで，While関数内の処理で使用される変数となっている．

第一引数Aは，ループの初期値を設定する．
このAの値が，最初に*x*に代入される．

第二引数Bは，定義済みLangFuncの名前を設定する．
このBの名前の関数は，ループ上での条件文となり，この関数の引数には*x*が代入される．
また，この関数の戻り値のLangListの0番目の要素は，条件を満たすかを表すBool型とし，この値がTrueの場合はループを継続する．

第三引数Cは，定義済みLangFuncの名前を設定する．
このCの名前の関数は，繰り返し実行される処理内容となり，この関数の引数には*x*が代入される．
そして，この関数では更新された*x*を戻り値に設定する．

ループ終了時は最終的な*x*の結果が出力される．

次は，```tat```を使用した例である．

```SFGPL
pat fa 'condition_func' fit fat sal tel mal pol fet pit tol mal pal
pat fa 'process_func' fit fit fit fat tal fet pit tol mal pal mal pel tal fet pit tol mal pel mel pel pal til fet pit tol mal pil mal pil
tat fit fit fit fat mal pal mal pal mal pel fa 'condition_func' fa 'process_func'
```

まず1行目では，条件文の関数の設定を行っている．
この条件文の関数は"condition_func"とし，```4-x[0]>=0```がTrueの間は，ループを実行するように定義している．

2行目では，処理文の関数の設定を行っている．
この処理文の関数は"process_func"とし，それぞれの要素の更新を行う．
更新する内容は，```[x[0]+1,x[1]+10,x[2]*2]```としている．

3行目で，実際に繰り返しを実行している．
このとき初期値として，```[0,0,1]```を与えている．

## LangListのmap関数

LangListのすべての要素に対して，一定の処理を行う関数```tet```が存在する．
このとき，第一引数に適応するLangList A，第二引数に一定の処理を行うための関数名Bを指定する．

このとき，Bの関数には，LangList型で```[それぞれの要素のデータ，その要素のindex（NumberList），LangList A]```が引数として渡される．
また，Bの関数を実行した結果のLangList[0]の値が，新たな要素の値として使われる．

次に，```tet```を使用して，全要素に1を足すためには次のようにする．

```SFGPL
pat fa 'map_func' fit fat tal fet pit tol mal pal mal pel
tet fit fit fit fat mel pel pal mel pel pel mel pel pil fa 'map_func'
```

1行目で，処理用の関数を設定している．
この処理内容は，それぞれの要素のデータに対して，1を足す処理を行っている．

2行目で，実際に```[10,11,12]```を代入し，すべての要素に対して1を足す処理を実行している．
このとき，```[10,11,12]```を表すためには，```fit fit fit fat mel pel pal mel pel pel mel pel pil```とすることで表現できる．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|pen|fa 'pen'|
|go|sa 'go'|
|happy|la 'happy'|
|I am a student|ma ga so fa 'student'|
