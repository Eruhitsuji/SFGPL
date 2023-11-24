{page_header}

The LangFunc type exists as a basic function type in SFGPL.
The following functions exist in LangFunc.

|Word|Explanation|
|:-:|:-:|
|{LangFunc_setFunc} A B|Set up a function that returns B named A with a certain LangList as an argument|
|{LangFunc_arg}|Used for {LangFunc_setFunc} arguments|
|{LangFunc_runFunc} A B|Execute the configured LangFunc named A with argument B|

LangFunc sets the function by ```{LangFunc_setFunc}```.
Also, ```{LangFunc_arg}``` can be included in the second argument of ```{LangFunc_setFunc}``` statement.
This will cause the actual value to be assigned and processed when the function is executed.
The first argument of ```{LangFunc_setFunc}``` is a function name.
And the function name cannot be duplicated.
The following is an example of a function setup.

```SFGPL
{xor_set}
```

The function takes the XOR of the zeroth and first values of a LangList.
When (false,false) is given to the function, do the following.

```SFGPL
{xor_00}
```
