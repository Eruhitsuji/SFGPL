# 20. LangVar

[TOP](../../readme.md)
/
[EN](../en/LangVar.md)

SFGPLでは[LangList](LangList.md)を格納する変数を作成できる．

|単語|説明|
|:-:|:-:|
|bat A B|Aという名前の変数にLangList Bを代入する|
|bot A|Aという名前の変数を取得する|

var1という名前の変数にLangList```["apple","banana"]```を格納するには次のようにする．

```SFGPL
bat fa 'var1' fit fit fat fa 'apple' fa 'banana'
```

また，var1を取得するには次のようにする．

```SFGPL
bot fa 'var1'
```
