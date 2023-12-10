# 2. Basic Grammar

[TOP](../../readme.md)
/
[JP](../jp/BasicGrammar.md)

This document describes the basic knowledge and grammar for learning the SFGPL.
In particular, this chapter describes the basic sentences of the affirmative form of the present tense.

It is also recommended to read [aboutSFGPL](aboutSFGPL.md) as a prerequisite.
Furthermore, it is desirable to know a little English, as the example sentences etc. are based on English.

## About the features of the SFGPL sentence structure

Like English, SFGPL is an SOV-type language in which the role of a word is determined by its position.
One of the most important features of the SFGPL is its emphasis on [sentence pattern](sentence_pattern.md).
Each of these sentence patterns defines what arguments (words of what part of speech) and how many to take.
The meaning of the sentence is therefore uniquely determined.
The function word that determines this sentence type is attached to the beginning of the sentence (clause).
The whole sentence (clause) is considered as a noun and can be nested ([Compound Sentences](CompoundSentences.md)).

## Specific examples of SFGPL sentence patterns

### Syntax with ta

First, we present an example using ```ta```.
This ```ta``` has two arguments, where the first argument is the subject of the sentence and the second argument is the verb of the sentence.
In other words, ```ta``` can produce sentences equivalent to the English first sentence type SV.

For example, to express "I run." in SFGPL, use the following.

```SFGPL
ta ga sa 'run'
```

In this case, ```ta``` is the word to be added when the sentence type is "SV".

The ```ga``` denotes the first person pronoun "I".

And ```sa 'run'``` denotes the verb "run".
This ```sa 'run'``` consists of two words.
In loan words such as these, a part-of-speech indicator (in this case, ```sa```) is attached to the word.
There are three words that represent such parts of speech.

||SFGPL|
|:-:|:-:|
|Noun|fa|
|Verb|sa|
|Modifier|la|

### Syntax with ma

Next, we present an example using ```ma```.
This ```ma``` has three arguments: the first is the subject of the sentence, the second is the verb of the sentence and the third is the complement of the subject.
Also, the complement of the third argument must be a noun.
In other words, ```ma``` can produce sentences equivalent to the English second sentence type SVC.

As an example, to express "I am a student." in the SFGPL, use the following.

```SFGPL
ma ga so fa 'student'
```

In this case, ```ma``` is the word to be added when the sentence type is "SVC".

The ```ga``` denotes the first person pronoun "I".

Next, ```so``` is a word indicating that the verb is nonsense.
In ```so```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to that of the English verb "be".

And ```fa 'student'``` denotes the noun "student".
In this case, the article that exists in English and other languages does not exist in the SFGPL, so there is no need to add any article.

### Syntax with me

Next, we present an example using ```me```.
This ```me``` has three arguments: the first is the subject of the sentence, the second is the verb of the sentence and the third is the complement of the subject.
Also, the complement of the third argument must be a modifier.
In other words, ```me``` can produce sentences equivalent to the English second sentence type SVC.

As an example, to express "I am happy." in the SFGPL, do the following.

```SFGPL
me ga so la 'happy'
```

In this case, ```me``` is the word to be added when the sentence type is "SVC".

The ```ga``` denotes the first person pronoun "I".

Next, ```so``` is a word indicating that the verb is nonsense.
In ```so```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to that of the English verb "be".

And ```la 'happy'``` denotes the modifier "happy".

### Syntax with te

We then present an example using ```te```.
This ```te``` has three arguments, the first representing the subject of the sentence, the second the verb of the sentence and the third the object.
In other words, ```te``` can produce sentences equivalent to SVO, the third sentence type in English.

For example, to express "I open the door." in SFGPL, use the following.

```SFGPL
te ga sa 'open' fa 'door'
```

In this case, ```te``` is the word to be added when the sentence type is "SVO".

The ```ga``` denotes the first person pronoun "I".

Next, ```sa 'open'``` denotes the verb "open".

Next, ```fa 'door'``` denotes the noun "door".

### Syntax with ti

Next, we present an example using ```ti```.
This ```ti``` has four arguments, the first representing the subject of the sentence, the second the verb of the sentence, the third the indirect object and the fourth the direct object.
In other words, ```ti``` can produce sentences equivalent to SVOO, the fourth sentence type in English.

For example, to express "I give you a box." in SFGPL, you can do the following.

```SFGPL
ti ga so ge fa 'box'
```

In this case, ```ti``` is a word that is added when the sentence type is "SVOO".

The ```ga``` denotes the first person pronoun "I".

Next, ```so``` is a word indicating that the verb is nonsense.
In ```so```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to the English word give.

And ```ge``` denotes the second person pronoun "you".

Furthermore, ```fa 'box'``` denotes the noun "box".

### Syntax with tu

Next, we present an example using ```tu```.
This ```tu``` has four arguments: the first is the subject of the sentence, the second the verb of the sentence, the third the object and the fourth the complement of the object.
The complement of the fourth argument must be a noun.
In other words, ```tu``` can produce sentences equivalent to the English fourth sentence type SVOC.

For example, to express "I make you a teacher." in SFGPL, use the following.

```SFGPL
tu ga so ge fa 'teacher'
```

In this case, ```tu``` is the word to be added when the sentence type is "SVOC".

The ```ga``` denotes the first person pronoun "I".

Next, ```so``` is a word indicating that the verb is nonsense.
In ````so```, the meaning changes depending on the location.
In this case, in the example sentence, the meaning is equivalent to the English causative verb make.

And ```ge``` denotes the second person pronoun "you".

Furthermore, ```fa 'teacher'``` represents the noun "teacher".

### Syntax with to

Next, we present an example using ```to```.
This ```to``` has four arguments: the first is the subject of the sentence, the second the verb of the sentence, the third the object and the fourth the complement of the object.
The complement of the fourth argument must be a modifier.
In other words, ```to``` can produce sentences equivalent to the English fourth sentence type SVOC.

As an example, to express "I make you happy." in the SFGPL, use the following.

```SFGPL
to ga so ge la 'happy'
```

In this case, ```to``` is the word to be added when the sentence type is "SVOC".

The ```ga``` denotes the first person pronoun "I".

Next, ```so``` is a word indicating that the verb is nonsense.
In ````so```, the meaning changes depending on the location.
In this case, in the example sentence, the meaning is equivalent to the English causative verb make.

And ```ge``` denotes the second person pronoun "you".

Furthermore, ```la 'happy'``` represents the modifier "happy".

### Syntax with mi

Next, we present an example using ```mi```.
This ```mi``` has three arguments, the first representing the subject of the sentence (the owner), the second the verb of the sentence and the third the object (the possession).
Therefore, ```mi``` can represent the sentence "S has O".

As an example, to express "I have a box." in SFGPL, use the following.

```SFGPL
mi ga so fa 'box'
```

In this case, ```mi``` is the word used to make a sentence expressing possession.

The ```ga``` is the first person pronoun "I".

Next, ```so``` is a word that indicates that the verb is meaningless.
In ```so```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to the English word have.

Furthermore, ```fa 'box'``` denotes the noun "box".

### Syntax with mu

Next, we present an example using ```mu```.
This ```mu``` has three arguments, the first representing the subject of the sentence (the person or thing to which it belongs), the second the verb of the sentence and the third the object (place of affiliation).
Therefore, ```mu``` can represent the sentence "S belongs to O".

As an example, to express "I belong to a school." in SFGPL, use the following.

```SFGPL
mu ga so fa 'school'
```

In this case, ```mu``` is a word that is added to make a statement of belonging.

The ```ga``` denotes the first person pronoun "I".

Next, ```so``` is a word that indicates that the verb is meaningless.
In ```so```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to "belong to" in English.

Furthermore, ```fa 'school'``` denotes the noun "school".

### Other syntaxes

Other syntaxes are indicated by [sentence pattern](sentence_pattern.md).

## Modification methods

### How to modify nouns

There are two main ways of modifying nouns: with modifiers and with nouns.

#### How to modify a noun with a modifier

For example, to express that a certain box is big, in English we say "The box is big.".
Similarly, the SFGPL uses ```me``` to express an SVC as follows:.

```SFGPL
me fa 'box' so wan
```

In this case, ```wan``` means big.

#### How to modify a noun with a noun for a noun

This method is used in situations where the English preposition "of" or the Japanese particle "の" is used.
However, the SFGPL does not allow for concise notation, and even in such cases it is qualified by sentences like English relative pronouns ([compound sentences](CompoundSentences.md)).

For example, "My box is big." can be expressed by the following sentence.

```SFGPL
me mi ga so san fa 'box' so wan
```

In this sentence, the sentence ```mi ga so san fa 'box'``` is nested in the subject of the main sentence.
This ```mi ga so san fa 'box'``` means "I have a box.
In addition, the use of ```san``` can be used to emphasise words that are particularly important in the sentence.
Thus, in this sentence, ```san fa 'box'``` is used to emphasise the word "box".

Overall, the literal translation means "[I have a **box**] is big.", which is equivalent to "My box is big.".

### How to modify verbs

#### Simple verb modification methods

Verbs can be modified using ```na```.
In ```na```, the first argument is the verb and the second argument is the modifier.

For example, to express "I quickly run.".

```SFGPL
ta ga na sa 'run' la 'quickly'
```

In this case, ```la 'quickly'``` means "quickly".
In ```na sa 'run' la 'quickly'```, the verb "run" is modified by the modifier "quickly", meaning "quickly run".

#### How to convert a noun phrase into a modifier and modify a verb

The SFGPL allows you to convert a noun phrase into a modifier, which then modifies a verb.
This is similar to adverbialisation using prepositions in English.

First, the SFGPL has [words that can be converted between parts of speech](partOfSpeechConversion.md), which in this case uses ```li``` to convert a noun to a modifier.
In this usage, a [noun determiner](DeterminerN.md) is used in parallel with ```li``` to limit the meaning of the noun phrase.

For example, to express "I go to Tokyo." in SFGPL.

```SFGPL
ta ga na sa 'go' li pun fa 'Tokyo'
```

Firstly, ```sa 'go'``` expresses the English word "go", and the destination is expressed by modifying the verb.
In particular, the four words ```li pun fa 'Tokyo'``` represent "to Tokyo".
The three words ```li``` are noun-to-modifier words, and ```pun``` is a nominal determiner of place.
Combining these two words with ```fa 'Tokyo'``` (Tokyo) to express the meaning "to Tokyo".

### How to modify modifiers

The modifier modification is expressed using ````ka```.
In this ```ka```, the modifier of the second argument modifies the modifier of the first argument.

For example, to express "Your box is a little big." in the SFGPL, use the following.

```SFGPL
me mi ge so san fa 'box' so ka wan la 'little'
```

In this case, ```la 'little'``` (= "a little") modifies ```wan``` (= "big"), so that ```ka wan la 'little'``` means "a little big".

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|ga|
|run|sa 'run'|
|student|fa 'student'|
|happy|la 'happy'|
|open|sa 'open'|
|door|fa 'door'|
|you|ge|
|box|fa 'box'|
|teacher|fa 'teacher'|
|school|fa 'school'|
|big|wan|
|quickly|la 'quickly'|
|go|sa 'go'|
|Tokyo|fa 'Tokyo'|
|a little|la 'little'|
