# 10. Part of Speech Conversion

[TOP](../../readme.md)
/
[JP](../jp/partOfSpeechConversion.md)

The SFGPL can convert nouns, verbs, and modifiers into each other's parts of speech.
The following table lists the words converted to parts-of-speech by the SFGPL.

||Before|After|Word|
|:-:|:-:|:-:|:-:|
|V2N|Verb|Noun|fi|
|M2N|Modifier|Noun|fu|
|M2V|Modifier|Verb|si|
|N2V|Noun|Verb|su|
|N2M|Noun|Modifier|li|
|V2M|Verb|Modifier|lu|

Verb to noun and noun to modifier are especially common.

## Verb to Noun

Verb to noun is used as in "This is building.".

```SFGPL
ma gu so fi sa 'build'
```

The verb of the original word can also be pre-conjugated according to [verb conjugation](verbConjugation.md).

## Noun to Modifier

Noun to modifier is used to create the equivalent meaning of a phrase that combines an English preposition and a noun.
In such cases, ```li``` and [DeterminerN](DeterminerN.md) are used in combination.
"I live in Tokyo." in SFGPL becomes the following.
In this case, ```pun``` is a determiner of location.

```SFGPL
ta ga na sa 'live' li pun fa 'Tokyo'
```

It can also be combined with the word ```son```, which abstracts the noun, to mean "-like".
"My daughter has a cat-like stuffed toy." can be expressed in SFGPL as follows.

```SFGPL
mi mi ga so san fa 'daughter' so me me fa 'toy' so lu ne sa 'stuff' so li son fa 'cat'
```

## Verb to Modifier

Verb to modifier conversion allows for the use of the participle equivalent, which is common in the Indo-European language family.
The verb of the original word can also be pre-conjugated according to [verb conjugation](verbConjugation.md).

"There is a sleeping boy." can be expressed in the SFGPL as follows.

```SFGPL
ma pun go so me fa 'boy' so lu ni sa 'sleep'
```

The phrase "I lived in that destroyed building." can be expressed as follows.

```SFGPL
di ta ga na sa 'live' li pun ma go so san me fi sa 'build' so lu ne sa 'destroy'
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|this|gu|
|build|sa 'build'|
|I|ga|
|live|sa 'live'|
|in Tokyo|li pun fa 'Tokyo'|
|daughter|fa 'daughter'|
|cat|fa 'cat'|
|stuffed|lu ne sa 'stuff'|
|toy|fa 'toy'|
|there|pun go|
|sleep|sa 'sleep'|
|boy|fa 'boy'|
|that|go|
|destroy|sa 'destroy'|
