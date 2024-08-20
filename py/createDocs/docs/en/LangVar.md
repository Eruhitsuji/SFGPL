{page_header}

In SFGPL, a variable that stores [LangList]({docs_LangList}) can be created.

|Word|Explanation|
|:-:|:-:|
|{LangVar_set} A B|Assign LangList B to the variable named A|
|{LangVar_get} A|Get a variable named A|

To store LangList```["apple","banana"]``` in a variable named var1, do the following.

```SFGPL
{var1_set_lang_list}
```

To obtain var1, do the following.

```SFGPL
{var1_get_lang_list}
```
