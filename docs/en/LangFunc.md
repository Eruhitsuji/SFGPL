# 17. LangFunc

[TOP](../../readme.md)
/
[JP](../jp/LangFunc.md)

The LangFunc type exists as a basic function type in SFGPL.
The following functions exist in LangFunc.

|Word|Explanation|
|:-:|:-:|
|pat A B|Set up a function that returns B named A with a certain LangList as an argument|
|pit|Used for pat arguments|
|pot A B|Execute the configured LangFunc named A with argument B|

LangFunc sets the function by ```pat```.
Also, ```pit``` can be included in the second argument of ```pat``` statement.
This will cause the actual value to be assigned and processed when the function is executed.
The first argument of ```pat``` is a function name.
And the function name cannot be duplicated.
The following is an example of a function setup.

```SFGPL
pat fa 'xor' fit fat bu bu fet pit mas pas pas bu fet pit mas pas pas fet pit mas pas pos bu bu fet pit mas pas pas fet pit mas pas pos fet pit mas pas pos
```

The function takes the XOR of the zeroth and first values of a LangList.
When (false,false) is given to the function, do the following.

```SFGPL
pot fa 'xor' fit fit fat pas pas
```
