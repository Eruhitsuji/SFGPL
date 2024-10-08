{page_header}

The SFGPL words have a basic set of usages.
For example, the way in which loan words are used is defined.
This chapter describes the types of these words and how they are used.
The details of the words are also available in [dict.csv](../../dict.csv).

In general, SFGPL words are not transformed by articles, number, gender or case.
If you want to indicate number or gender, use [noun determiner]({docs_DeterminerN}).

## Borrowed Words

The SFGPL uses loan words for all but the basic words.
However, half-width double quotation marks (") and half-width spaces ( ) cannot be used.
The single quotation mark (') is a symbol to indicate a loanword, so care must be taken if you wish to add it to the beginning or end of a word.

To use loan words for nouns, verbs, and modifiers, use the following table.

|Root Word|Part of Speech|SFGPL|
|:-:|:-:|:-:|
|apple|Noun|{noun_apple}|
|open|Verb|{verb_open}|
|tall|Modifier|{modifier_tall}|

Examples using these words are shown below.

|English|SFGPL|
|:-:|:-:|
|I have an apple.|{I_have_an_apple}|
|I open a door.|{I_open_a_door}|
|I am tall.|{I_am_tall}|

### Borrowed words and the language from which they are borrowed

Borrowing words can be from any language.
However, it is preferable to choose words that are understood by both speakers.

For example, the word 'language' from any language can be borrowed into the SFGPL as shown in the table below.

|Language|Raw Word|SFGPL|
|:-:|:-:|:-:|
|English|language|{language_en}|
|Japanese|言語|{language_ja}|
|Spanish|idioma|{language_es}|
|French|langue|{language_fr}|
|Russian|язык|{language_ru}|
|Portuguese|linguagem|{language_pt}|
|Esperanto|lingvo|{language_eo}|

Thus, it can borrow from a variety of languages.
In addition, the borrowed words in this material are basically borrowed from the English language.

### How to make borrowed words explicit

The following words exist to make it clear from which language a loanword has been borrowed.

|Type|Word|
|:-:|:-:|
|Noun|{Noun_borrowed}|
|Verb|{Verb_borrowed}|
|Modifier|{Modifier_borrowed}|

#### Noun

To borrow the English noun word "language", do the following.

```SFGPL
{language_English_borrowed}
```

#### Verb

To borrow the English verb word "go", do the following.

```SFGPL
{go_English_borrowed}
```

#### Modifier

To borrow the English modifier word "big", do the following.

```SFGPL
{big_English_borrowed}
```

## About unique words

The SFGPL provides several unique words for verbs and modifiers.
In the WordV and WordM classes, these are word groups that are unique to the SFGPL.

These word groups are highly versatile because their parts of speech have already been determined and they have a broad meaning, but it is difficult to specify the details of their meaning.

The following table gives examples of unique words.

|English|SFGPL|
|:-:|:-:|
|create|{create}|
|big|{big}|

Examples using these words are shown below.

|English|SFGPL|
|:-:|:-:|
|I create a door.|{I_create_a_door}|
|The apple is big.|{the_apple_is_big}|

### Unique word rules

There is uniqueness with respect to the SFGPL's unique words: words with different meanings have different pronunciations.
The syllable structure is one word and one syllable (CV or CVC).

## About the determiners

As a grammatical function, there are determiners, which are words that simply modify a word.
There are two types of determiners: noun determiners, which limit nouns, and verb determiners, which limit verbs.

### DeterminerN

The SFGPL has a [noun determiner]({docs_DeterminerN}).
This is a special word that originally modifies a noun.
However, they can also be used as nouns in the same sense as the determiners themselves.
To do so, use ```{noun_none}```.
Examples are given in the following table.

|English|SFGPL|
|:-:|:-:|
|human|{human}|

Examples using these words are shown below.

|English|SFGPL|
|:-:|:-:|
|I am human.|{I_am_human}|

### DeterminerV

There is a [verb determiner]({docs_DeterminerV}) in the SFGPL.
These are special words that modify verbs.
These include words used as verb tenses and aspects, and words that add meaning to the verb in an auxiliary verb-like manner.

## About meaningless words

There are words in the SFGPL that do not add meaning.
These words exist for each part of speech and are used when grammatically necessary.

First, ```{noun_none}``` of meaningless noun is often used to express [noun determiners]({docs_DeterminerN}) as they are.
Also, ```{verb_none}``` of meaningless verb is used when a verb is not needed, especially in [sentence pattern]({docs_sentence_pattern}).
On the other hand, ```{modifier_none}``` of meaningless modifier is rarely used.
Examples of these are given below.

|English|SFGPL|
|:-:|:-:|
|I am human.|{I_am_human}|
|I have an apple.|{I_have_an_apple}|

||SFGPL|
|:-:|:-:|
|Noun|{noun_none}|
|Verb|{verb_none}|
|Modifier|{modifier_none}|

## About pronouns

[Pronouns]({docs_pronoun}) exist in SFGPL.
Pronouns are listed in the following table.

||English|SFGPL|
|:-:|:-:|:-:|
|First Person Pronoun|I|{pronoun_I}|
|Second Person Pronoun|you|{pronoun_you}|
|Third Person Pronoun|he/she/it|{pronoun_he}|
|Proximate Pronoun|this|{pronoun_proximal}|
|Distant Pronoun|that|{pronoun_distal}|
|Interrogative Pronoun|what|{pronoun_interrogative}|
|Indefinite Pronoun|something|{pronoun_indefinite}|

## Words used numerically and logically

There are [numerical words]({docs_Number}), [words for boolean values]({docs_Bool}), [words for lists]({docs_LangList}), [words for functions]({docs_LangFunc}) and [words for variable]({docs_LangVar}) in the SFGPL.
These words are not often used in general sentences, but are used to indicate logic.
