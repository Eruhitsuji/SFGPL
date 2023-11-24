# 15. LangList

[TOP](../../readme.md)
/
[JP](../jp/LangList.md)

The LangList type exists as a basic data structure type in SFGPL.
The following functions exist in LangList.

|Word|Explanation|
|:-:|:-:|
|fat|Create a list of LangObj (LangList)|
|fet A B|Gets the B-th value of LangList (A)|
|fit A B|Add one LangObj (B) to the end of the LangList (A)|
|fut A B C|Get the B-th through C-th lists for a LangList (A)|
|fot A B|Combine two LangLists|

LangList can store all classes that inherit from LangObj.
The following is an example of LangList creation.

```SFGPL
fit fit fit fit fit fat ga fa 'pen' sa 'go' la 'happy' ma ga so fa 'student'
```

To retrieve the first value from this LangList, do the following.
In this case ```fis fas pas``` represents 0 in [BoolList](Bool.md).

```SFGPL
fet fit fit fit fit fit fat ga fa 'pen' sa 'go' la 'happy' ma ga so fa 'student' fis fas pas
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|ga|
|pen|fa 'pen'|
|go|sa 'go'|
|happy|la 'happy'|
|I am a student|ma ga so fa 'student'|
