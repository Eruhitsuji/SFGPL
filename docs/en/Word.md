# 8. Word

[TOP](../../readme.md)
/
[JP](../jp/Word.md)

The SFGPL words have a basic set of usages.
For example, the way in which loan words are used is defined.
This chapter describes the types of these words and how they are used.
The details of the words are also available in [dict.csv](../../dict.csv).

In general, SFGPL words are not transformed by articles, number, gender or case.
If you want to indicate number or gender, use [noun determiner](DeterminerN.md).

## Borrowed Words

The SFGPL uses loan words for all but the basic words.
To use loan words for nouns, verbs, and modifiers, use the following table.

|Root Word|Part of Speech|SFGPL|
|:-:|:-:|:-:|
|apple|Noun|fa 'apple'|
|open|Verb|sa 'open'|
|tall|Modifier|la 'tall'|

Examples using these words are shown below.

|English|SFGPL|
|:-:|:-:|
|I have an apple.|mi ga so fa 'apple'|
|I open a door.|te ga sa 'open' fa 'door'|
|I am tall.|me ga so la 'tall'|

### Borrowed words and the language from which they are borrowed

Borrowing words can be from any language.
However, it is preferable to choose words that are understood by both speakers.

For example, the word 'language' from any language can be borrowed into the SFGPL as shown in the table below.

|Language|Raw Word|SFGPL|
|:-:|:-:|:-:|
|English|language|fa 'language'|
|Japanese|言語|fa '言語'|
|Spanish|idioma|fa 'idioma'|
|French|langue|fa 'langue'|
|Russian|язык|fa 'язык'|
|Portuguese|linguagem|fa 'linguagem'|
|Esperanto|lingvo|fa 'lingvo'|

Thus, it can borrow from a variety of languages.
In addition, the borrowed words in this material are basically borrowed from the English language.

## About unique words

The SFGPL provides several unique words for verbs and modifiers.
In the WordV and WordM classes, these are word groups that are unique to the SFGPL.

These word groups are highly versatile because their parts of speech have already been determined and they have a broad meaning, but it is difficult to specify the details of their meaning.

The following table gives examples of unique words.

|English|SFGPL|
|:-:|:-:|
|create|kan|
|big|wan|

Examples using these words are shown below.

|English|SFGPL|
|:-:|:-:|
|I create a door.|te ga kan fa 'door'|
|The apple is big.|me fa 'apple' so wan|

### Unique word rules

There is uniqueness with respect to the SFGPL's unique words: words with different meanings have different pronunciations.
The syllable structure is one word and one syllable (CV or CVC).

## About the determiners

As a grammatical function, there are determiners, which are words that simply modify a word.
There are two types of determiners: noun determiners, which limit nouns, and verb determiners, which limit verbs.

### DeterminerN

The SFGPL has a [noun determiner](DeterminerN.md).
This is a special word that originally modifies a noun.
However, they can also be used as nouns in the same sense as the determiners themselves.
To do so, use ```fo```.
Examples are given in the following table.

|English|SFGPL|
|:-:|:-:|
|human|ben fo|

Examples using these words are shown below.

|English|SFGPL|
|:-:|:-:|
|I am human.|ma ga so ben fo|

### DeterminerV

There is a [verb determiner](DeterminerV.md) in the SFGPL.
These are special words that modify verbs.
These include words used as verb tenses and phases, and words that add meaning to the verb in an auxiliary verb-like manner.

## About meaningless words

There are words in the SFGPL that do not add meaning.
These words exist for each part of speech and are used when grammatically necessary.

First, ```fo``` of meaningless noun is often used to express [noun determiners](DeterminerN.md) as they are.
Also, ```so``` of meaningless verb is used when a verb is not needed, especially in [sentence pattern](sentence_pattern.md).
On the other hand, ```lo``` of meaningless modifier is rarely used.
Examples of these are given below.

|English|SFGPL|
|:-:|:-:|
|I am human.|ma ga so ben fo|
|I have an apple.|mi ga so fa 'apple'|

||SFGPL|
|:-:|:-:|
|Noun|fo|
|Verb|so|
|Modifier|lo|

## About pronouns

[Pronouns](pronoun.md) exist in SFGPL.
Pronouns are listed in the following table.

||English|SFGPL|
|:-:|:-:|:-:|
|First Person Pronoun|I|ga|
|Second Person Pronoun|you|ge|
|Third Person Pronoun|he/she/it|gi|
|Proximate Pronoun|this|gu|
|Distant Pronoun|that|go|
|Interrogative Pronoun|what|wa|
|Indefinite Pronoun|something|we|

## Words used numerically and logically

There are [numerical words](Number.md), [words for boolean values](Bool.md), [words for lists](LangList.md) and [words for functions](LangFunc.md) in the SFGPL.
These words are not often used in general sentences, but are used to indicate logic.
