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
|foal A|Get the length of the NumberList (A)|

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

### Numeric calculation

As shown in the following table, NumberList has functions that perform numerical calculations such as four arithmetic operations.

||Python|SFGPL|
|:-:|:-:|:-:|
|Addition|```A+B```|tal A B|
|Subtraction|```A-B```|tel A B|
|Multiplication|```A*B```|til A B|
|Division|```A/B```|tul A B|
|Power|```A**B```|dal A B|
|Int Division|```A//B```|del A B|
|Remainder|```A%B```|dil A B|
|Minus|```-A```|sel A|
|Absolute value|```abs(A)```|sil A|

### Interconversion between BoolList and NumberList

As shown in the following table, there are functions that convert BoolList and NumberList into each other.

|Type|SFGPL|from|to|
|:-:|:-:|:-:|:-:|
|Int|tol|NumberList|BoolList|
|Int|tos|BoolList|NumberList|
|Float|dol|NumberList|BoolList|
|Float|dos|BoolList|NumberList|

#### Mutual Conversion in Integer Types

There are ```tol``` and ```tos``` functions that convert each other as integers.
The numeric values handled by these conversions consider the BoolList as an integer type (```tes```).
In other words, the value of the BoolList is equivalent to the two's complement representation of a binary number.
These values can also be adapted if numerical calculations, such as four arithmetic operations, are performed by NumberList.
However, if NumberList is a real number due to the result of division, etc., the conversion cannot be performed and an error occurs.

#### Mutual Conversion in Floating-Point Type (Real Number)

There are ```dol``` and ```dos``` that convert each other as floating-point (real) numbers.
The numbers handled by these conversions consider BoolList as a floating-point type (```tis```).
In other words, the BoolList values in this case use the half-precision, single-precision, double-precision, and quadruple-precision floating-point representation methods in IEEE754.
When converting from NumberList to BoolList, it is converted as a 64-bit double-precision floating-point number and stored in BoolList.

### How to handle real numbers

To handle real numbers, you can use NumberList division (```tul```), or you can represent floating-point numbers in a BoolList and convert it to a NumberList.

For example, 3.14 can be expressed by division as follows.

```SFGPL
tul mil pul pel pol mil pel pal pal
```

Similarly, to express 3.14 in double-precision floating point, do the following.

```SFGPL
dos fos fos fos mos pas pos pas pas pas pas pas pas mos pas pas pas pas pos pas pas pos fos mos pas pas pas pos pos pos pos pas mos pos pas pos pos pos pas pas pas fos fos mos pas pos pas pos pas pas pas pos mos pos pos pos pas pos pas pos pos fos mos pos pas pas pas pas pos pas pos mos pas pas pas pos pos pos pos pos
```

### Determination of positive numbers

To determine whether a NumberList is a positive number, use ```sal```.
This will output the SFGPL Bool type, which is equivalent to ```pos``` if the number is greater than or equal to zero.
For example, to determine whether an integer is positive in the two cases of 4 and -4, do the following.

```SFGPL
sal mal pol
sal sel mal pol
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|ga|
|apple|fa 'apple'|
|Japan|fa 'Japan'|
|people|fa 'people'|
