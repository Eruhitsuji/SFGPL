# LangList

[TOP](../../readme.md)
/
[EN](../en/LangList.md)

SFGPLでは基本的なデータ構造型として，LangList型が存在する．
LangListには，以下の関数が存在している．

|単語|説明|
|:-:|:-:|
|{LangList}|LangObjのリストLangListを作成する|
|{LangList_get} A B|LangList(A)のB番目の値を取得する|
|{LangList_append} A B|LangList(A)に1つのLangObj(B)を末尾に加える|
|{LangList_slice} A B C|AというLangListに対して，B番目からC番目までのリストを取得する|
|{LangList_add} A B|2つのLangListを結合する|

LangListは，LangObjを継承しているすべてのクラスを格納することができる．
次はLangListを作成する一例である．

```SFGPL
{lang_list_01}
```

また，このLangListから最初の値を取得するには次のようにする．
このとき```{number_0}```は[BoolList](Bool.md)における0を表している．

```SFGPL
{lang_list_01_get_0}
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|pen|{pen}|
|go|{go}|
|happy|{happy}|
|I am a student|{I_am_a_student}|
