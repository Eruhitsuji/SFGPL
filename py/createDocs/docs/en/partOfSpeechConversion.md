# Part of Speech Conversion

[TOP](../../readme.md)
/
[JP](../jp/partOfSpeechConversion.md)

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
Verb to noun is used as in "This is building.".

```SFGPL
{this_is_building}
```

Noun-to-Modifier is also used to create the equivalent meaning of a phrase that combines an English preposition and a noun.
In such cases, ```{N2M}``` and [DeterminerN](DeterminerN.md) are used in combination.
"I live in Tokyo." in SFGPL becomes the following.
In this case, ```{determinerN_place}``` is a determiner of location.

```SFGPL
{I_live_in_Tokyo}
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|this|{this}|
|building|{building}|
|I|{I}|
|live|{live}|
|in Tokyo|{in_Tokyo}|
