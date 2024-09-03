{page_header}

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
In such a statement, the whole is inherited as True.

```SFGPL
{It_is_true_that_I_am_a_student}
```

Bool types can also use NOT ```{LangObj_NOT}```, OR ```{LangObj_OR}```, AND ```{LangObj_AND}```, NOR ```{LangObj_NOR}``` and NAND ```{LangObj_NAND}```, which are provided in LangObj. 
They can then perform logic operations.

For example, to represent ```True OR False```, the following is used.

```SFGPL
{true_or_false}
```

Besides the usual IFELSE ```{LangObj_IFELSE}```, LangObj has a logicIFELSE ```{LangObj_logicIFELSE}```.
This word allows you to change the sentence (word) to be executed internally depending on whether or not the condition is met.
"If true, I am a student." can be expressed as follows.

```SFGPL
{If_true_I_am_a_student}
```

## About BoolList class

BoolList can create an array of boolean values.
The following functions exist in BoolList.

|Word|Explanation|
|:-:|:-:|
|{BoolList}|Create a list of true/false (BoolList)|
|{BoolList_get} A B|Gets the B-th value of BoolList(A)|
|{BoolList_append} A B|Add one Bool (B) to the end of the BoolList (A)|
|{BoolList_slice} A B C|Get the B-th through C-th lists for a BoolList (A)|
|{BoolList_add} A B|Combine two BoolLists (A,B)|
|{BoolList_twoBit} A B|Create a BoolList consisting of 2 Bool values (A,B)|
|{BoolList_fourBit} X1~X4|Create a BoolList consisting of 4 Bool values (x1~x4)|
|{BoolList_byte} X1~X8|Create a BoolList consisting of 8 Bool values (x1~x8)|
|{BoolList_NaturalNum} A|BoolList (A) is considered a binary natural number|
|{BoolList_Int} A|BoolList (A) is considered a binary integer|
|{BoolList_Float} A|BoolList (A) is considered a binary floating number|
|{BoolList_ASCII} A|BoolList (A) is considered an ASCII character|

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
