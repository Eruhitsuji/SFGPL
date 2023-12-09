# 8. Detailed Grammar

[TOP](../../readme.md)
/
[JP](../jp/detailedGrammar.md)

Basically, the SFGPL must adhere strictly to the grammar as described in [sentence pattern](sentence_pattern.md), but the rest may be decided to some extent by the user.
However, an exemplary grammar is described in this chapter.

## How to qualify a sentence

To modify a whole sentence, you basically modify the verbs in that sentence by using ```na```.
For example, in the example sentence "I go to Tokyo.", the "to Tokyo" part is a modifier.
In this case, the SFGPL uses the following.

```SFGPL
ta ga na sa 'go' li pun fa 'Tokyo'
```

Another alternative is to use ```me```.

```SFGPL
me ta ga sa 'go' so li pun fa 'Tokyo'
```

### Prepositional usage in English

In particular, when modifying verbs, like prepositions in English, they are expressed using ```li``` and [DeterminerN](DeterminerN.md).
Examples of English prepositions and SFGPLs are given in the following table.

|English|Meaning|SFGPL|
|:-:|:-:|:-:|
|at/in/on/to/from|Time|li pin|
|at/in/on/to/from|Place|li pun|
|for|Reason|li pon|
|for|Way/Means|li ban|
|from|Start|li fan|
|to|End|li fen|
|between/among|Section|li fin|
|in|In|li fun|
|into|Into|li tun fun|
|out|Out|li fon|
|up/over|Move&Above|li tun man|
|above|Above|li man|
|down|Move&Below|li tun men|
|under|On&Below|li min men|
|below|Below|li men|
|on|On|li min|
|right|Right|li mun|
|left|Left|li mon|
|near|Near|li tin|
|by/about|By/About|li tan tin|
|with|With|li ten tin|

## Grammar of comparative expressions

In the SFGPL, comparative expressions using comparative classes in English are defined by ```mo```, but not comparisons using superlative or equivalent classes.
It is recommended that such sentences be expressed as follows.

### Comparative degree

Comparative expressions such as "A is B(-er) than C" are expressed by ```mo```.
"My bag is bigger than yours." is expressed as follows.

```SFGPL
mo mi ga so san fa 'big' so wan sen ge
```

### Superlative

Comparative expressions such as "A is the B(-est) in/of C" are expressed with the following syntax.

```SFGPL
me A V ka B li fun C
```

"My bag is the biggest in my class." is expressed as follows.

```SFGPL
me mi ga so san fa 'big' so ka wan li fun mu ga so san fa 'class'
```

### Equivalent classes

Comparative expressions such as "A is as B as C" are expressed with the following syntax.
In this case, use ```wen``` to mean "similar".

```SFGPL
me ba A C V ka B wen
```

"My bag is as big as his." is expressed as follows.

```SFGPL
me ba mi ga so san fa 'big' sen lan gi so ka wan wen
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|ga|
|go|sa 'go'|
|to Tokyo|li pun fa 'Tokyo'|
|bag|fa 'bag'|
|big|wan|
|yours(possessive)|sen ge|
|my class|mu ga so san fa 'class'|
|his(possessive)|sen lan gi|
