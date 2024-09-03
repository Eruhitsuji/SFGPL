# 9. Detailed Grammar

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
me A V ka ki B li fun C
```

"My bag is the biggest in my class." is expressed as follows.

```SFGPL
me mi ga so san fa 'bag' so ka ki wan li fun mu ga so san fa 'class'
```

When expressing "the N-th X(-est)", a numerical value is added to the modifier, as in ```ka X li N```.
"My bag is the second biggest in my class." using ordinal numbers is expressed as follows.

```SFGPL
me mi ga so san fa 'bag' so ka ki ka wan li mal pil li fun mu ga so san fa 'class'
```

### Equivalent classes

Comparative expressions such as "A is as B as C" are expressed with the following syntax.
In this case, use ```wen``` to mean "similar".

```SFGPL
me ba A C V ka B wen
```

"My bag is as big as his." is expressed as follows.

```SFGPL
me ba mi ga so san fa 'bag' sen lan gi so ka wan wen
```

## Diachronic sentences

Constant matters and facts, such as customs, periodic matters and unchanging facts, are expressed by not adding a tense, as is the case with the present.

To express "I cook every day." in SFGPL, use the following.

```SFGPL
ta ga na sa 'cook' li pin me fa 'day' so la 'every'
```

"The Earth revolves around the Sun." in the SFGPL can be expressed as follows.

```SFGPL
ta fa 'Earth' na sa 'revolve' li tun tin fa 'Sun'
```

And to express "English is spoken all over the world." in the SFGPL as follows.

```SFGPL
ta fa 'English' na ne sa 'speak' li fun dan fa 'world'
```

## Syntax for expressing existence

When creating a sentence that simply states that something exists, use ```gen```.
This has the same meaning as the English There is/are construction.
For example, "There is a book on this table.".

```SFGPL
ta fa 'book' na gen li pun ma gu so fa 'table'
```

## Topic-prominent linguistic grammar

It is possible to produce sentences like those in topic-prominent languages, which are common in East Asian languages such as Japanese, Chinese, Korean, and Indonesian.
A topic-prominent language is a language in which, in addition to the usual subject, there is a grammar that allows the subject of the sentence to be presented.
This makes it easy to produce sentences that contain both a topic and a subject.
The SFGPL allows for the production of sentences containing topics in a simplified manner, though not in the explicit manner of the East Asian languages.

### Sentences containing a subject or one of the topic or subject

Sentences containing a topic or subject fragment are constructed in the same way as [sentence type](sentence_pattern.md).

### Sentences containing both a topic and a subject

A sentence containing both a topic and a subject is expressed as follows.
In this case, “T” is the topic, and “C” consists of comments (sentences, words, etc. that explain the topic).

```SFGPL
ma T so C
```

As an example, the Japanese phrase "象は鼻が長い"(“Elephants have long noses” [topic: elephant, subject: nose]) can be expressed in SFGPL as follows.

```SFGPL
ma fa '象' so me fa '鼻' so la '長い'
ma fa 'elephant' so me fa 'nose' so la 'long'
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
|cook|sa 'cook'|
|every day|me fa 'day' so la 'every'|
|the Earth|fa 'Earth'|
|revolve|sa 'revolve'|
|the Sun|fa 'Sun'|
|English|fa 'English'|
|speak|sa 'speak'|
|all over the world|li fun dan fa 'world'|
|book|fa 'book'|
|on this table|li pun ma gu so fa 'table'|
|象(elephant)|fa '象'|
|鼻(nose)|fa '鼻'|
|長い(long)|fa '長い'|
|elephant|fa 'elephant'|
|nose|fa 'nose'|
|long|la 'long'|
