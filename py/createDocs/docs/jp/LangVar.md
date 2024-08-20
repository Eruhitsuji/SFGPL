{page_header}

SFGPLでは[LangList]({docs_LangList})を格納する変数を作成できる．

|単語|説明|
|:-:|:-:|
|{LangVar_set} A B|Aという名前の変数にLangList Bを代入する|
|{LangVar_get} A|Aという名前の変数を取得する|

var1という名前の変数にLangList```["apple","banana"]```を格納するには次のようにする．

```SFGPL
{var1_set_lang_list}
```

また，var1を取得するには次のようにする．

```SFGPL
{var1_get_lang_list}
```
