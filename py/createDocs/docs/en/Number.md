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
|{NumberList_len} A|Get the length of the NumberList (A)|

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

### Numeric calculation

As shown in the following table, NumberList has functions that perform numerical calculations such as four arithmetic operations.

||SFGPL|
|:-:|:-:|
|Addition|{NumberList_calcAdd}|
|Subtraction|{NumberList_calcSub}|
|Multiplication|{NumberList_calcMul}|
|Division|{NumberList_calcDiv}|
|Power|{NumberList_calcPow}|
|Int Division|{NumberList_calcIntDiv}|
|Remainder|{NumberList_calcMod}|

### How to handle real numbers

When you want to deal with real numbers, use division.
For example, 3.14 can be expressed as follows.

```SFGPL
{real_number_3_14}
```

### Interconversion between BoolList and NumberList

As shown in the following table, there are functions that convert BoolList and NumberList into each other.

|Type|SFGPL|from|to|
|:-:|:-:|:-:|:-:|
|Int|{NumberList_IntNL2BL}|NumberList|BoolList|
|Int|{BoolList_IntBL2NL}|BoolList|NumberList|
|Float|{NumberList_FloatNL2BL}|NumberList|BoolList|
|Float|{BoolList_FloatBL2NL}|BoolList|NumberList|

#### Mutual Conversion in Integer Types

There are ```{NumberList_IntNL2BL}``` and ```{BoolList_IntBL2NL}``` functions that convert each other as integers.
The numeric values handled by these conversions consider the BoolList as an integer type (```{BoolList_Int}```).
In other words, the value of the BoolList is equivalent to the two's complement representation of a binary number.
These values can also be adapted if numerical calculations, such as four arithmetic operations, are performed by NumberList.
However, if NumberList is a real number due to the result of division, etc., the conversion cannot be performed and an error occurs.

#### Mutual Conversion in Floating-Point Type (Real Number)

There are ```{NumberList_FloatNL2BL}``` and ```{BoolList_FloatBL2NL}``` that convert each other as floating-point (real) numbers.
The numbers handled by these conversions consider BoolList as a floating-point type (```{BoolList_Float}```).
In other words, the BoolList values in this case use the half-precision, single-precision, double-precision, and quadruple-precision floating-point representation methods in IEEE754.
When converting from NumberList to BoolList, it is converted as a 64-bit double-precision floating-point number and stored in BoolList.

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|apple|{apple}|
|Japan|{Japan}|
|people|{people}|
