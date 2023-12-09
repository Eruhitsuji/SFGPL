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

LangListは，LangObjを継承しているすべてのクラスを格納することができる．
次はLangListを作成する一例である．

```SFGPL
fit fit fit fit fit fat ga fa 'pen' sa 'go' la 'happy' ma ga so fa 'student'
```

また，このLangListから最初の値を取得するには次のようにする．
このとき```fis fas pas```は[BoolList](Bool.md)における0を表している．

```SFGPL
fet fit fit fit fit fit fat ga fa 'pen' sa 'go' la 'happy' ma ga so fa 'student' fis fas pas
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|pen|fa 'pen'|
|go|sa 'go'|
|happy|la 'happy'|
|I am a student|ma ga so fa 'student'|
