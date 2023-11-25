{page_header}

The SFGPL words have a basic set of usages.
For example, the way in which loan words are used is defined.
This chapter describes the types of these words and how they are used.

In general, SFGPL words are not transformed by articles, number, gender or case.
If you want to indicate number or gender, use [noun determiner]({docs_DeterminerN}).

## Borrowed Words

The SFGPL uses loan words for all but the basic words.
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

## About the determiners

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

## About meaningless words

There are words in the SFGPL that do not add meaning.
These words exist for each part of speech and are used when grammatically necessary.

```{noun_none}``` is often used to express [noun determiners]({docs_DeterminerN}) as they are.
Also, ```{verb_none}``` is used when a verb is not needed, especially in [sentence pattern]({docs_sentence_pattern}).
On the other hand, ```{modifier_none}``` is rarely used.
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
