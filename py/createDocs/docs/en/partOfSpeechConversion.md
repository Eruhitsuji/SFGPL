{page_header}

The SFGPL can convert nouns, verbs, and modifiers into each other's parts of speech.
The following table lists the words converted to parts-of-speech by the SFGPL.

||Before|After|Word|
|:-:|:-:|:-:|:-:|
|V2N|Verb|Noun|{V2N}|
|M2N|Modifier|Noun|{M2N}|
|M2V|Modifier|Verb|{M2V}|
|N2V|Noun|Verb|{N2V}|
|N2M|Noun|Modifier|{N2M}|
|V2M|Verb|Modifier|{V2M}|

Verb to noun and noun to modifier are especially common.

## Verb to Noun

Verb to noun is used as in "This is building.".

```SFGPL
{this_is_building}
```

The verb of the original word can also be pre-conjugated according to [verb conjugation]({docs_verbConjugation}).

## Noun to Modifier

Noun to modifier is used to create the equivalent meaning of a phrase that combines an English preposition and a noun.
In such cases, ```{N2M}``` and [DeterminerN]({docs_DeterminerN}) are used in combination.
"I live in Tokyo." in SFGPL becomes the following.
In this case, ```{determinerN_place}``` is a determiner of location.

```SFGPL
{I_live_in_Tokyo}
```

It can also be combined with the word ```{determinerN_abstract}```, which abstracts the noun, to mean "-like".
"My daughter has a cat-like stuffed toy." can be expressed in SFGPL as follows.

```SFGPL
{my_daughter_has_a_cat_like_stuffed_toy}
```

## Verb to Modifier

Verb to modifier conversion allows for the use of the participle equivalent, which is common in the Indo-European language family.
The verb of the original word can also be pre-conjugated according to [verb conjugation]({docs_verbConjugation}).

"There is a sleeping boy." can be expressed in the SFGPL as follows.

```SFGPL
{there_is_a_sleeping_boy}
```

The phrase "I lived in that destroyed building." can be expressed as follows.

```SFGPL
{I_lived_in_that_destroyed_building}
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|this|{this}|
|build|{build}|
|I|{I}|
|live|{live}|
|in Tokyo|{in_Tokyo}|
|daughter|{daughter}|
|cat|{cat}|
|stuffed|{stuffed}|
|toy|{toy}|
|there|{there}|
|sleep|{sleep}|
|boy|{boy}|
|that|{that}|
|destroy|{destroy}|
