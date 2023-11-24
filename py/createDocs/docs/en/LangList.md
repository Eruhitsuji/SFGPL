{page_header}

The LangList type exists as a basic data structure type in SFGPL.
The following functions exist in LangList.

|Word|Explanation|
|:-:|:-:|
|{LangList}|Create a list of LangObj (LangList)|
|{LangList_get} A B|Gets the B-th value of LangList (A)|
|{LangList_append} A B|Add one LangObj (B) to the end of the LangList (A)|
|{LangList_slice} A B C|Get the B-th through C-th lists for a LangList (A)|
|{LangList_add} A B|Combine two LangLists|

LangList can store all classes that inherit from LangObj.
The following is an example of LangList creation.

```SFGPL
{lang_list_01}
```

To retrieve the first value from this LangList, do the following.
In this case ```{number_0}``` represents 0 in [BoolList]({docs_Bool}).

```SFGPL
{lang_list_01_get_0}
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|pen|{pen}|
|go|{go}|
|happy|{happy}|
|I am a student|{I_am_a_student}|
