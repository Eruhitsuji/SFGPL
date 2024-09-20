# 17. Bool related classes

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
In such a statement, the whole is inherited as True.

```SFGPL
pis ma ga so fa 'student' pos
```

Bool types can also use NOT ```pa```, OR ```be```, AND ```ba```, NOR ```bo``` and NAND ```bu```, which are provided in LangObj. 
They can then perform logic operations.

For example, to represent ```True OR False```, the following is used.

```SFGPL
be pos pas
```

Besides the usual IFELSE ```bi```, LangObj has a logicIFELSE ```ja```.
This word allows you to change the sentence (word) to be executed internally depending on whether or not the condition is met.
"If true, I am a student." can be expressed as follows.

```SFGPL
ja pos ma ga so fa 'student' pa ma ga so fa 'student'
```

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
|foas A|Get the length of the BoolList (A)|
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

Floating point corresponds to half, single, double and quadruple precision in IEEE 754.
Therefore, they must be expressed in 16-bit, 32-bit, 64-bit and 128-bit respectively.

To express 1/3 in each precision is as follows.
First, the hexadecimal representation is as follows.

|Type|HEX|
|:-:|:-:|
|Half|```3555```|
|Single|```3eaa aaab```|
|Double|```3FD5 5555 5555 5555```|
|Quadruple|```3ffd 5555 5555 5555 5555 5555 5555 5555```|

This is converted into the SFGPL as follows.

|Type|SFGPL|
|:-:|:-:|
|Half|```tis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fas pas pas pos pos pas pos pas pos pas pos pas pos pas pos pas pos```|
|Single|```tis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fas pas pas pos pos pos pos pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pos```|
|Double|```tis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fas pas pas pos pos pos pos pos pos pos pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos```|
|Quadruple|```tis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fis fas pas pas pos pos pos pos pos pos pos pos pos pos pos pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos pas pos```|

## BoolList date/time representation

BoolList can be used to represent dates and times based on Unix time.
There are three types of date/time expressions, depending on their accuracy.

|SFGPL|Type|Unit|
|:-:|:-:|:-:|
|das|yyyy-mm-dd|Day|
|des|yyyy-mm-dd HH:MM:SS|Second|
|dis|yyyy-mm-dd HH:MM:SS.nnnnnnnnn|Nano Second|

These expressions are based on ```1970-01-01 00:00:00.00000000000``` and represent the date and time by the difference in days, seconds and nanoseconds respectively.
They are also based on UTC time.

For example, to represent ```2024-09-19 09:27:27``` by ```des``` as follows.

First, the Unix time for this hour is ```1726738047```.
Converting this to a binary number gives ```0110 0110 1110 1011 1110 1110 0111 1111```.
Therefore, converting it to a BoolList gives the following.

```SFGPL
fos fos mos pas pos pos pas pas pos pos pas mos pos pos pos pas pos pas pos pos fos mos pos pos pos pas pos pos pos pas mos pas pos pos pos pos pos pos pos
```

Furthermore, the conversion to date and time using ```des``` gives the following.

```SFGPL
des fos fos mos pas pos pos pas pas pos pos pas mos pos pos pos pas pos pas pos pos fos mos pos pos pos pas pos pos pos pas mos pas pos pos pos pos pos pos pos
```

This allows ```2024-09-19 09:27:27``` to be represented by the SFGPL.

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I am a student|ma ga so fa 'student'|
