# 16. LangFunc

[TOP](../../readme.md)
/
[EN](../en/LangFunc.md)

SFGPLでは基本的な関数型として，LangFunc型が存在する．
LangFuncには，以下の関数が存在している．

|単語|説明|
|:-:|:-:|
|pat A B|あるLangListを引数とするAという名前のBを返す関数を設定する|
|pit|patの引数用に使用する|
|pot A B|設定したAという名前のLangFuncを引数Bとして実行する|

LangFuncは，```pat```によって関数を設定する．
また，```pit```を```pat```の第二引数内の文内に含ませることができる．
それによって，関数実行時に実際の値が代入されて処理される．
また，```pat```の第一引数は関数名を表す．
そして，関数名は重複して付けることはできない．
以下は，関数設定の例を示す．

```SFGPL
pat fa 'xor' fit fat bu bu fet pit mas pas pas bu fet pit mas pas pas fet pit mas pas pos bu bu fet pit mas pas pas fet pit mas pas pos fet pit mas pas pos
```

この関数は，あるLangListに対して，0番目と1番目のXORを取る関数である．
この関数に(false,false)を与えるときは，次のようにする．

```SFGPL
pot fa 'xor' fit fit fat pas pas
```
