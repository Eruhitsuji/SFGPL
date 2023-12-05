# 15. Bool related classes

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
|False|pas|
|True|pos|

You can also use ```pis``` to connect a Bool type to a noun to indicate the truth or falsehood of a noun.
The following statement is an example.

```SFGPL
pis ma ga so fa 'student' pos
```

Bool types can also use NOT ```pa```, OR ```be```, AND ```ba```, NOR ```bo``` and NAND ```bu```, which are provided in LangObj. 
They can then perform logic operations.

## About BoolList class

BoolList can create an array of boolean values.
The following functions exist in BoolList.

|Word|Explanation|
|:-:|:-:|
|fas|Create a list of true/false (BoolList)|
|fes A B|Gets the B-th value of BoolList(A)|
|fis A B|Add one Bool (B) to the end of the BoolList (A)|
|fus A B C|Get the B-th through C-th lists for a BoolList (A)|
|fos A B|Combine two BoolLists (A,B)|
|mas A B|Create a BoolList consisting of 2 Bool values (A,B)|
|mis X1~X4|Create a BoolList consisting of 4 Bool values (x1~x4)|
|mos X1~X8|Create a BoolList consisting of 8 Bool values (x1~x8)|
|tas A|BoolList (A) is considered a binary natural number|
|tes A|BoolList (A) is considered a binary integer|
|tis A|BoolList (A) is considered a binary floating number|
|tus A|BoolList (A) is considered an ASCII character|

4-byte data can be used by doing the following.

```SFGPL
fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos
```

This represents ```0100 0000 0100 1001 0000 1111 1101 1011``` in binary.
It can also be used as a number by doing the following.

|Type|SFGPL|Value|
|:-:|:-:|:-:|
|Natural Number|tas fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|1078530011|
|Integer Number|tes fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|1078530011|
|Floating Point Number|tis fos fos mos pas pos pas pas pas pas pas pas mos pas pos pas pas pos pas pas pos fos mos pas pas pas pas pos pos pos pos mos pos pos pas pos pos pas pos pos|3.1415927410125732|

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I am a student|ma ga so fa 'student'|
