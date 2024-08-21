{page_header}

SFGPLでは基本的なデータ構造型として，LangList型が存在する．
LangListには，以下の関数が存在している．

|単語|説明|
|:-:|:-:|
|{LangList}|LangObjのリストLangListを作成する|
|{LangList_get} A B|LangList(A)のB番目の値を取得する|
|{LangList_append} A B|LangList(A)に1つのLangObj(B)を末尾に加える|
|{LangList_slice} A B C|AというLangListに対して，B番目からC番目までのリストを取得する|
|{LangList_add} A B|2つのLangListを結合する|
|{LangList_While} A B C|LangListを使用した繰り返し用の関数|

LangListは，LangObjを継承しているすべてのクラスを格納することができる．
次はLangListをappendを使用して作成する一例である．

```SFGPL
{lang_list_01}
```

また，このLangListから最初の値を取得するには次のようにする．
このとき```{number_0}```は[BoolList]({docs_Bool})における0を表している．

```SFGPL
{lang_list_01_get_0}
```

## LangListでの繰り返し処理

LangListを繰り返し処理するための```{LangList_While}```を使用することでLangListを使用した繰り返し処理を行うことができる．
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

次は，```{LangList_While}```を使用した例である．

```SFGPL
{langlist_while_example_1}
{langlist_while_example_2}
{langlist_while_example_3}
```

まず1行目では，条件文の関数の設定を行っている．
この条件文の関数は"condition_func"とし，```4-x[0]>=0```がTrueの間は，ループを実行するように定義している．

2行目では，処理文の関数の設定を行っている．
この処理文の関数は"process_func"とし，それぞれの要素の更新を行う．
更新する内容は，```[x[0]+1,x[1]+10,x[2]*2]```としている．

3行目で，実際に繰り返しを実行している．
このとき初期値として，```[0,0,1]```を与えている．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|pen|{pen}|
|go|{go}|
|happy|{happy}|
|I am a student|{I_am_a_student}|
