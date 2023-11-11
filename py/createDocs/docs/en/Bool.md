# Bool related classes

[TOP](../../readme.md)
/
[JP](../jp/Bool.md)

SFGPL has classes related to Bool, Bool type and BoolList type.
These classes are used to represent boolean values, numerical values, and so on.

## About Bool class

The Bool type is a class for representing true or false.
False and True of type Bool are represented as follows.

||word|
|:-:|:-:|
|False|{Bool_false}|
|True|{Bool_true}|

You can also use ```{Bool_B2N}``` to connect a Bool type to a noun to indicate the truth or falsehood of a noun.
The following statement is an example.

```SFGPL
{It_is_true_that_I_am_a_student}
```

Bool types can also use NOT ```{LangObj_NOT}```, OR ```{LangObj_OR}```, AND ```{LangObj_AND}```, NOR ```{LangObj_NOR}``` and NAND ```{LangObj_NAND}```, which are provided in LangObj. 
They can then perform logic operations.

## About BoolList class

BoolList can create an array of boolean values.
The following functions exist in BoolList.

|Word|Explanation|
|:-:|:-:|
|{BoolList}|Create a list of true/false (BoolList)|
|{BoolList_append} A B|Add one Bool to the end of the BoolList|
|{BoolList_add} A B|Combine two BoolLists|
|{BoolList_twoBit} A B|Create a BoolList consisting of 2 Bool values|
|{BoolList_fourBit} X1~X4|Create a BoolList consisting of 4 Bool values|
|{BoolList_byte} X1~X8|Create a BoolList consisting of 8 Bool values|
|{BoolList_NaturalNum} A|BoolList is considered a binary natural number|
|{BoolList_Int} A|BoolList is considered a binary integer|
|{BoolList_Float} A|BoolList is considered a binary floating number|
|{BoolList_ASCII} A|BoolList is considered an ASCII character|

4-byte data can be used by doing the following.

```SFGPL
{bin_0100_0000_0100_1001_0000_1111_1101_1011}
```

This represents ```0100 0000 0100 1001 0000 1111 1101 1011``` in binary.
It can also be used as a number by doing the following.

|Type|SFGPL|Value|
|:-:|:-:|:-:|
|Natural Number|{NN_b1}|{NN_b1_get}|
|Integer Number|{INT_b1}|{INT_b1_get}|
|Floating Point Number|{Float_b1}|{Float_b1_get}|

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I am a student|{I_am_a_student}|
