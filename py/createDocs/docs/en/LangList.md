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
|{LangList_While} A B C|Function for iteration using LangList|

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

## Iteration in LangList

LangList can be iterated using ```{LangList_While}``` to iterate through LangList.
The *x*s below are all the same LangList variables used in the While function.

The first argument A sets the initial value of the loop.
The value of A is first assigned to *x*.

The second argument B sets the name of the predefined LangFunc.
The function named B is a conditional statement on the loop, and *x* is assigned to the argument of this function.
The zeroth element of the function's return value, LangList, is of type Bool, indicating whether the condition is satisfied, and if this value is True, the loop continues.

The third argument C is set to the name of a predefined LangFunc.
The function named C is the content of the iterative process, and *x* is assigned to the argument of this function.
The function then sets the updated *x* as the return value.

At the end of the loop, the final *x* result is output.

The following is an example using ````{LangList_While}`` .

```SFGPL
{langlist_while_example_1}
{langlist_while_example_2}
{langlist_while_example_3}
```

The first line sets up the function of the conditional statement.
The function of the conditional statement is defined as “condition_func”, which executes a loop while ```4-x[0]>=0``` is True.

In the second line, the function of the processing statement is set.
The function of this processing statement is “process_func” and updates each element.
The contents to be updated are set to ```[x[0]+1,x[1]+10,x[2]*2]```.

The third line actually executes the iteration.
In this case, ```[0,0,1]``` is given as the initial value.

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|pen|{pen}|
|go|{go}|
|happy|{happy}|
|I am a student|{I_am_a_student}|
