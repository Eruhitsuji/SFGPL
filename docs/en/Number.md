# 21. How numbers are expressed

[TOP](../../readme.md)
/
[JP](../jp/Number.md)

The Number and NumberList classes exist in SFGPL to represent decimal numbers.

## Number class

The Number class is a class for cardinal numerals and is not used by itself.
In this class, values from 0 to 9 are defined, as shown in the table below.

|Meaning|SFGPL|
|:-:|:-:|
|0|pal|
|1|pel|
|2|pil|
|3|pul|
|4|pol|
|5|bal|
|6|bel|
|7|bil|
|8|bul|
|9|bol|

## NumberList class

Use the NumberList class when used as a normal numeral.
This class can store radix data in a list.
Numbers are represented as decimal numbers, with the largest digit stored first, starting with the 0th digit.

The NumberList class has the following list-type functions.
However, these functions cannot be applied to NumberList after numerical calculation as described below.

|Word|Explanation|
|:-:|:-:|
|fal|Create a list of Number(NumberList)|
|fel A B|Gets the B-th value of NumberList(A)|
|fil A B|Add one Number to the end of the NumberList|
|ful A B C|Get the B-th through C-th lists for a NumberList (A)|
|fol A B|Combine two NumberLists|

In addition, dedicated functions are available to create 1~5-digit integers, as shown in the table below.

|Word|Explanation|
|:-:|:-:|
|mal|Create a NumberList consisting of one decimal digit
|mel|Create a NumberList consisting of two decimal digit|
|mil|Create a NumberList consisting of three decimal digit|
|mul|Create a NumberList consisting of four decimal digit|
|mol|Create a NumberList consisting of five decimal digit|

In the SFGPL, "I have five apples." can be expressed as follows.

```SFGPL
mi ga so ma fa 'apple' so mal bal
```

The expression "I have fifteen apples." can be expressed as follows.

```SFGPL
mi ga so ma fa 'apple' so mel pel bal
```

Furthermore, the representation of numbers with more than five digits in decimal can be achieved by using ```fol``` and concatenating NumberList.
The following sentence represents "Japan has 125416877 people." in the SFGPL.

```SFGPL
mi fa 'Japan' so ma fa 'people' so fol mul pel pil bal pol mol pel bel bul bil bil
```

Then, as shown in the following table, there are functions in NumberList that perform the four arithmetic operations.

||SFGPL|
|:-:|:-:|
|Addition|tal|
|Subtraction|tel|
|Multiplication|til|
|Division|tul|

In addition, there are functions that convert integer BoolList and NumberList into each other, as shown in the table below.

|SFGPL|from|to|
|:-:|:-:|:-:|
|tol|NumberList|BoolList|
|tos|BoolList|NumberList|

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|ga|
|apple|fa 'apple'|
|Japan|fa 'Japan'|
|people|fa 'people'|
