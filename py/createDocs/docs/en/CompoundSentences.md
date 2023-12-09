{page_header}

The SFGPL allows you to create sentences that combine several within a single sentence.

## Parallel clauses

A [conjunction]({docs_Conjunction}) is used to connect two or more sentences in parallel.

In the SFGPL, "I went to Tokyo and I was shopping there." can be expressed as follows.

```SFGPL
{I_went_to_Tokyo_and_I_was_shopping_there_01}
```

And while English-like tense agreement requires clause-by-clause utilisation in this way, the SFGPL allows the basic tense to be utilised throughout the sentence.

```SFGPL
{I_went_to_Tokyo_and_I_was_shopping_there_02}
```

## Dependent clauses

A subordinate modification of a noun in the main clause can be achieved by inserting a sentence describing the noun instead of the noun.
In addition, the SFGPL generally uses subordinate clauses to modify nouns.

### General subordinate clauses

In the SFGPL, "My bag is big." can be expressed as follows.
In this case, "My bag" is expressed as "I have a bag".
The noun is then marked with ```{DeterminerN_stressed}``` because "bag" is the noun being modified.

```SFGPL
{my_bag_is_big}
```

The meaning of "I have a bag is big." is almost the same as "I have a bag is big.
In this case, the "bag" in "a bag is big" is the subject of the subordinate clause, so ```{DeterminerN_stressed}``` need not be added.

```SFGPL
{I_have_a_bag_is_big}
```

Then, to express "I give you the desk I built.", do the following.

```SFGPL
{I_give_you_the_desk_I_built}
```

The tense of only the subordinate clause can be changed in this way.

### Adverbial clauses

Adverbial clauses can be used to modify predicates and whole sentences.
In the SFGPL, "I ate sushi, when I went to Tokyo." can be expressed as follows.

```SFGPL
{I_ate_sushi_when_I_went_to_Tokyo}
```

Or, to express "I went grocery shopping while my kids were sleeping." in the SFGPL.

```SFGPL
{I_went_grocery_shopping_while_my_kids_were_sleeping}
```

## Modification of nouns by nouns

When Y modifies X in a noun X and Y, it is expressed as "YのX" in Japanese and "Y X" or "X of Y" in English, but the SFGPL uses three main types of usage.
In the SFGPL, as mentioned earlier, modifications are often made in subordinate clauses, and the case of nouns modifying nouns with nouns is no exception.
Therefore, nouns can be modified in different ways: ```{noun_eq}```, ```{noun_have}``` and ```{noun_belong}```.

### Noun.eq

First, ```{noun_eq}``` is mainly used when the modifier and the moderated are equivalent.
For example, to express "This pen is big." in SFGPL as follows.

```SFGPL
{this_pen_is_big}
```

In this case, "this" and "pen" are equivalent.
Therefore, ```{noun_eq}``` is used.

### Noun.have

Next, ```{noun_have}``` is mainly used when something has something.
To express "My pen is big." in the SFGPL, use the following.

```SFGPL
{my_pen_is_big}
```

### Noun.belong

Also, ```{noun_belong}``` is mainly used when something belongs to something.
To express "My school is big." in the SFGPL, use the following.

```SFGPL
{my_school_is_big}
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|go|{go}|
|to Tokyo|{to_Tokyo}|
|shop (Verb)|{shop_verb}|
|there|{there}|
|bag|{bag}|
|big|{big}|
|you|{you}|
|build|{build}|
|desk|{desk}|
|eat|{eat}|
|sushi|{sushi}|
|grocery|{grocery}|
|kid|{kid}|
|sleep|{sleep}|
|this|{this}|
|pen|{pen}|
|school|{school}|
