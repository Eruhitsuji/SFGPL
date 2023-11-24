# 2. Sentence Pattern

[TOP](../../readme.md)
/
[JP](../jp/sentence_pattern.md)

## List of SFGPL sentence patterns

In the SFGPL, there are sentence types as shown in the table below, and the sentences themselves are composed by the combination of these sentence types. In addition, modification of words is also performed.

|||word|function|arguments|supplement|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|S V|ta|Noun.do|S,V||
|2|S V C|ma|Noun.eq|S,V,C|C is the noun|
|2|S V C|me|Noun.haveP|S,V,C|C is the modifier|
|3|S V O|te|Noun.doT|S,V,O||
|4|S V O1 O2|ti|Noun.give|S,V,O1,O2||
|5|S V O C|tu|Noun.makeN|S,V,O,C|C is the noun|
|5|S V O C|to|Noun.makeM|S,V,O,C|C is the modifier|
|-|A has B|mi|Noun.have|A,V,B||
|-|A belongs to B|mu|Noun.belong|A,V,B||
|-|A is more B than C|mo|Noun.gt|A,V,B,C||

## Noun.do

In Noun.do ```ta```, in particular, S is the subject and V is the verb in the same form as the English first sentence form, and the subject is said to perform some action. It can express simple sentences.
"I run." can be expressed in SFGPL as follows.

```SFGPL
ta ga sa 'run'
```

## Noun.eq

Noun.eq ```ma``` corresponds to the English second sentence pattern "S is C", in which the complement C is a noun.
This construction also shows that S and C are equivalent.
If V corresponds to a be verb in English, use ```so``` as the verb.
To express "This is a table." in SFGPL, it is as follows.

```SFGPL
ma gu so fa 'table'
```

"You become a teacher." can be expressed in SFGPL as follows.

```SFGPL
ma ge sa 'become' fa 'teacher'
```

## Noun.haveP

Noun.haveP ```me``` corresponds to the English second sentence pattern "S is C", in which the complement C can be used as a modifier.
In this construction, S is the property or state of C.
If V corresponds to a be verb in English, use ```so``` as the verb.
To express "The table is red." in SFGPL, it is as follows.

```SFGPL
me fa 'table' so la 'red'
```

"You look sad." can be expressed in SFGPL as follows.

```SFGPL
me ge sa 'look' la 'sad'
```

## Noun.doT

Noun.doT ```te```, in particular, corresponds to the third sentence pattern in English, where S is the subject, V is the verb, and O is the object.
"I study English." can be expressed in SFGPL as follows.

```SFGPL
te ga sa 'study' fa 'English'
```

## Noun.give

In Noun.give ```ti```, in particular, it corresponds to the English fourth sentence pattern, where S is the subject, V is the verb, and O1 and O2 are the objects. In particular, this construction means "S gives O1 O2".
If V corresponds to "give" in English, use ```so``` as the verb.
"I give you a table." can be expressed in SFGPL as follows.

```SFGPL
ti ga so ge fa 'table'
```

## Noun.makeN and Noun.makeM

Noun.makeN ```tu``` and Noun.makeM ```to```, in particular, correspond to the English fifth sentence pattern, where S is the subject, V is the verb, O is the object and C is the complement.
Noun.makeN is used when C is a noun and Noun.makeM when C is a modifier.
In this construction, it means "S makes O C".
If V corresponds to "make" in English, use ```so``` as the verb.

"I make you a teacher." can be expressed in SFGPL as follows.

```SFGPL
tu ga so ge fa 'teacher'
```

"I make you sad." can be expressed in SFGPL as follows.

```SFGPL
to ga so ge la 'sad'
```

## Noun.have

Noun.have ```mi``` means "A owns B".
If V corresponds to "have" in English, use ```so``` as the verb.
"I have a table." can be expressed in SFGPL as follows.

```SFGPL
mi ga so fa 'table'
```

## Noun.belong

Noun.belong ```mu``` means "A belongs to B".
If V corresponds to "belong to" in English, use ```so``` as the verb.
"I belong to a school." can be expressed in SFGPL as follows.

```SFGPL
mu ga so fa 'school'
```

## Noun.gt

Noun.gt ```mo``` means "A is more B than C".
In this case, A and B are the nouns being compared and C is a modifier.
If V corresponds to a be verb in English, use ```so``` as the verb.
"The bed is bigger than yours." can be expressed in the SFGPL as follows.

```SFGPL
mo fa 'bed' so wan sen ge
```

## How to modify nouns using sentence structures

SFGPL uses these sentence structures to modify nouns.
When a sentence is generated, the entire sentence becomes a noun, which can be embedded in another sentence.

"Your table is red." can be expressed in SFGPL as follows.

```SFGPL
me mi ge so fa 'table' so la 'red'
```

Thus, ```mi ge so fa 'table'```, which is "You have table", becomes the subject, and it can be explained that the table is red ```la 'red'```.
The equivalent "You have red table." can be expressed as follows.

```SFGPL
mi ge so me fa 'table' so la 'red'
```

### Stressed Form

Emphasis ```san``` can also be used, especially when you want to emphasize a word other than the subject in a sentence.
To stress the word "table" in "Your table is red.".

```SFGPL
me mi ge so san fa 'table' so la 'red'
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|ga|
|run|sa 'run'|
|this|gu|
|table|fa 'table'|
|red|la 'red'|
|you|ge|
|become|sa 'become'|
|teacher|fa 'teacher'|
|look|sa 'look'|
|sad|la 'sad'|
|study|sa 'study'|
|English|fa 'English'|
|school|fa 'school'|
|bed|fa 'bed'|
|big|wan|
|yours|sen ge|
