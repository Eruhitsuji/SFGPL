# 20. LangVar

[TOP](../../readme.md)
/
[JP](../jp/LangVar.md)

In SFGPL, a variable that stores [LangList](LangList.md) can be created.

|Word|Explanation|
|:-:|:-:|
|bat A B|Assign LangList B to the variable named A|
|bot A|Get a variable named A|

To store LangList```["apple","banana"]``` in a variable named var1, do the following.

```SFGPL
bat fa 'var1' fit fit fat fa 'apple' fa 'banana'
```

To obtain var1, do the following.

```SFGPL
bot fa 'var1'
```
