{page_header}

The Number and NumberList classes exist in SFGPL to represent decimal numbers.

## Number class

The Number class is a class for cardinal numerals and is not used by itself.
In this class, values from 0 to 9 are defined, as shown in the table below.

|Meaning|SFGPL|
|:-:|:-:|
|0|{number_zero}|
|1|{number_one}|
|2|{number_two}|
|3|{number_three}|
|4|{number_four}|
|5|{number_five}|
|6|{number_six}|
|7|{number_seven}|
|8|{number_eight}|
|9|{number_nine}|

## NumberList class

Use the NumberList class when used as a normal numeral.
This class can store radix data in a list.
Numbers are represented as decimal numbers, with the largest digit stored first, starting with the 0th digit.

The NumberList class has the following list-type functions.
However, these functions cannot be applied to NumberList after numerical calculation as described below.

|Word|Explanation|
|:-:|:-:|
|{NumberList}|Create a list of Number(NumberList)|
|{NumberList_get} A B|Gets the B-th value of NumberList(A)|
|{NumberList_append} A B|Add one Number to the end of the NumberList|
|{NumberList_slice} A B C|Get the B-th through C-th lists for a NumberList (A)|
|{NumberList_add} A B|Combine two NumberLists|

In addition, dedicated functions are available to create 1~5-digit integers, as shown in the table below.

|Word|Explanation|
|:-:|:-:|
|{NumberList_digit1}|Create a NumberList consisting of one decimal digit
|{NumberList_digit2}|Create a NumberList consisting of two decimal digit|
|{NumberList_digit3}|Create a NumberList consisting of three decimal digit|
|{NumberList_digit4}|Create a NumberList consisting of four decimal digit|
|{NumberList_digit5}|Create a NumberList consisting of five decimal digit|

In the SFGPL, "I have five apples." can be expressed as follows.

```SFGPL
{I_have_five_apples}
```

The expression "I have fifteen apples." can be expressed as follows.

```SFGPL
{I_have_fifteen_apples}
```

Furthermore, the representation of numbers with more than five digits in decimal can be achieved by using ```{NumberList_add}``` and concatenating NumberList.
The following sentence represents "Japan has 125416877 people." in the SFGPL.

```SFGPL
{Japan_has_125416877_people}
```

### Four arithmetic operations

Then, as shown in the following table, there are functions in NumberList that perform the four arithmetic operations.

||SFGPL|
|:-:|:-:|
|Addition|{NumberList_calcAdd}|
|Subtraction|{NumberList_calcSub}|
|Multiplication|{NumberList_calcMul}|
|Division|{NumberList_calcDiv}|

### How to handle real numbers

When you want to deal with real numbers, use division.
For example, 3.14 can be expressed as follows.

```SFGPL
{real_number_3_14}
```

### Interconversion between BoolList and NumberList

In addition, there are functions that convert integer BoolList and NumberList into each other, as shown in the table below.

|SFGPL|from|to|
|:-:|:-:|:-:|
|{NumberList_IntNL2BL}|NumberList|BoolList|
|{BoolList_IntBL2NL}|BoolList|NumberList|

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|apple|{apple}|
|Japan|{Japan}|
|people|{people}|
