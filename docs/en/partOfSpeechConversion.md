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
Verb to noun is used as in "This is building.".

```SFGPL
ma gu so fi sa 'build'
```

Noun-to-Modifier is also used to create the equivalent meaning of a phrase that combines an English preposition and a noun.
In such cases, ```li``` and [DeterminerN](DeterminerN.md) are used in combination.
"I live in Tokyo." in SFGPL becomes the following.
In this case, ```pun``` is a determiner of location.

```SFGPL
ta ga na sa 'live' li pun fa 'Tokyo'
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|this|gu|
|building|fi sa 'build'|
|I|ga|
|live|sa 'live'|
|in Tokyo|li pun fa 'Tokyo'|
