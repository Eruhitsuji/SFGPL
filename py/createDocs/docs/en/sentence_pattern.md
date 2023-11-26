{page_header}

## List of SFGPL sentence patterns

In the SFGPL, there are sentence types as shown in the table below, and the sentences themselves are composed by the combination of these sentence types. In addition, modification of words is also performed.

|||word|function|arguments|supplement|
|:-:|:-:|:-:|:-:|:-:|:-:|
|1|S V|{noun_do}|Noun.do|S,V||
|2|S V C|{noun_eq}|Noun.eq|S,V,C|C is the noun|
|2|S V C|{noun_haveP}|Noun.haveP|S,V,C|C is the modifier|
|3|S V O|{noun_doT}|Noun.doT|S,V,O||
|4|S V O1 O2|{noun_give}|Noun.give|S,V,O1,O2||
|5|S V O C|{noun_makeN}|Noun.makeN|S,V,O,C|C is the noun|
|5|S V O C|{noun_makeM}|Noun.makeM|S,V,O,C|C is the modifier|
|-|A has B|{noun_have}|Noun.have|A,V,B||
|-|A belongs to B|{noun_belong}|Noun.belong|A,V,B||
|-|A is more B than C|{noun_gt}|Noun.gt|A,V,B,C||
|-|According to C, A V B|{noun_hearSay}|Noun.hearSay|A,V,B,C|A(Subject) V(Verb) that B(Content) according to C(Source)|

## Noun.do

In Noun.do ```{noun_do}```, in particular, S is the subject and V is the verb in the same form as the English first sentence form, and the subject is said to perform some action. It can express simple sentences.
"I run." can be expressed in SFGPL as follows.

```SFGPL
{I_run}
```

## Noun.eq

Noun.eq ```{noun_eq}``` corresponds to the English second sentence pattern "S is C", in which the complement C is a noun.
This construction also shows that S and C are equivalent.
If V corresponds to a be verb in English, use ```{verb_none}``` as the verb.
To express "This is a table." in SFGPL, it is as follows.

```SFGPL
{this_is_a_table}
```

"You become a teacher." can be expressed in SFGPL as follows.

```SFGPL
{you_become_a_teacher}
```

## Noun.haveP

Noun.haveP ```{noun_haveP}``` corresponds to the English second sentence pattern "S is C", in which the complement C can be used as a modifier.
In this construction, S is the property or state of C.
If V corresponds to a be verb in English, use ```{verb_none}``` as the verb.
To express "The table is red." in SFGPL, it is as follows.

```SFGPL
{the_table_is_red}
```

"You look sad." can be expressed in SFGPL as follows.

```SFGPL
{you_look_sad}
```

## Noun.doT

Noun.doT ```{noun_doT}```, in particular, corresponds to the third sentence pattern in English, where S is the subject, V is the verb, and O is the object.
"I study English." can be expressed in SFGPL as follows.

```SFGPL
{I_study_English}
```

## Noun.give

In Noun.give ```{noun_give}```, in particular, it corresponds to the English fourth sentence pattern, where S is the subject, V is the verb, and O1 and O2 are the objects. In particular, this construction means "S gives O1 O2".
If V corresponds to "give" in English, use ```{verb_none}``` as the verb.
"I give you a table." can be expressed in SFGPL as follows.

```SFGPL
{I_give_you_a_table}
```

## Noun.makeN and Noun.makeM

Noun.makeN ```{noun_makeN}``` and Noun.makeM ```{noun_makeM}```, in particular, correspond to the English fifth sentence pattern, where S is the subject, V is the verb, O is the object and C is the complement.
Noun.makeN is used when C is a noun and Noun.makeM when C is a modifier.
In this construction, it means "S makes O C".
If V corresponds to "make" in English, use ```{verb_none}``` as the verb.

"I make you a teacher." can be expressed in SFGPL as follows.

```SFGPL
{I_make_you_a_teacher}
```

"I make you sad." can be expressed in SFGPL as follows.

```SFGPL
{I_make_you_sad}
```

## Noun.have

Noun.have ```{noun_have}``` means "A owns B".
If V corresponds to "have" in English, use ```{verb_none}``` as the verb.
"I have a table." can be expressed in SFGPL as follows.

```SFGPL
{I_have_a_table}
```

## Noun.belong

Noun.belong ```{noun_belong}``` means "A belongs to B".
If V corresponds to "belong to" in English, use ```{verb_none}``` as the verb.
"I belong to a school." can be expressed in SFGPL as follows.

```SFGPL
{I_belong_to_a_school}
```

## Noun.gt

Noun.gt ```{noun_gt}``` means "A is more B than C".
In this case, A and B are the nouns being compared and C is a modifier.
If V corresponds to a be verb in English, use ```{verb_none}``` as the verb.
"The bed is bigger than yours." can be expressed in the SFGPL as follows.

```SFGPL
{The_bed_is_bigger_than_yours}
```

## Noun.hearSay

Noun.hearSay ```{noun_hearSay}``` means "A(Subject) V(Verb) that B(Content) according to C(Source)".
In this case, A is the person or thing receiving the information, V is the verb, B is the content of the information and C is the source person or thing.
If V corresponds to a verbs related to hearsay, such as hear and say in English, use ```{verb_none}``` as the verb.
"According to the book, I heard that Japan is located in East Asia." can be expressed in the SFGPL as.

```SFGPL
{According_to_the_book_I_heard_that_Japan_is_located_in_East_Asia}
```

## How to modify nouns using sentence structures

SFGPL uses these sentence structures to modify nouns.
When a sentence is generated, the entire sentence becomes a noun, which can be embedded in another sentence.

"Your table is red." can be expressed in SFGPL as follows.

```SFGPL
{your_table_is_red}
```

Thus, ```{you_have_table}```, which is "You have table", becomes the subject, and it can be explained that the table is red ```{red}```.
The equivalent "You have red table." can be expressed as follows.

```SFGPL
{you_have_red_table}
```

### Stressed Form

Emphasis ```{determinerN_stressed}``` can also be used, especially when you want to emphasize a word other than the subject in a sentence.
To stress the word "table" in "Your table is red.".

```SFGPL
{stressed_your_table_is_red}
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|run|{run}|
|this|{this}|
|table|{table}|
|red|{red}|
|you|{you}|
|become|{become}|
|teacher|{teacher}|
|look|{look}|
|sad|{sad}|
|study|{study}|
|English|{English}|
|school|{school}|
|bed|{bed}|
|big|{big}|
|yours|{yours_possessive}|
|book|{book}|
|Japan|{Japan}|
|in East Asia|{in_East_Asia}|
