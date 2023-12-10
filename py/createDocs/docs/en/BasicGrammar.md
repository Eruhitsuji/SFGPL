{page_header}

This chapter explains the basic knowledge and grammar for learning the SFGPL.
In particular, it describes the basic sentences in the affirmative form of the present tense.

It is also recommended to read [aboutSFGPL]({docs_aboutSFGPL}) as a prerequisite.
Furthermore, as a whole this material is based on English, e.g. example sentences, so it is desirable to know a little English.

## About the features of the SFGPL sentence structure

Like English, SFGPL is an SOV-type language in which the role of a word is determined by its position.
One of the most important features of the SFGPL is its emphasis on [sentence pattern]({docs_sentence_pattern}).
Each of these sentence patterns defines what arguments (words of what part of speech) and how many to take.
The meaning of the sentence is therefore uniquely determined.
The function word that determines this sentence type is attached to the beginning of the sentence (clause).
The whole sentence (clause) is considered as a noun and can be nested ([Compound Sentences]({docs_CompoundSentences})).

## Specific examples of SFGPL sentence patterns

### Syntax with {noun_do}

First, we present an example using ```{noun_do}```.
This ```{noun_do}``` has two arguments, where the first argument is the subject of the sentence and the second argument is the verb of the sentence.
In other words, ```{noun_do}``` can produce sentences equivalent to the English first sentence type SV.

For example, to express "I run." in SFGPL, use the following.

```SFGPL
{I_run}
```

In this case, ```{noun_do}``` is the word to be added when the sentence type is "SV".

The ```{I}``` denotes the first person pronoun "I".

And ```{run}``` denotes the verb "run".
This ```{run}``` consists of two words.
In loan words such as these, a part-of-speech indicator (in this case, ```{verb_init}```) is attached to the word.
There are three words that represent such parts of speech.

||SFGPL|
|:-:|:-:|
|Noun|{noun_init}|
|Verb|{verb_init}|
|Modifier|{modifier_init}|

### Syntax with {noun_eq}

Next, we present an example using ```{noun_eq}```.
This ```{noun_eq}``` has three arguments: the first is the subject of the sentence, the second is the verb of the sentence and the third is the complement of the subject.
Also, the complement of the third argument must be a noun.
In other words, ```{noun_eq}``` can produce sentences equivalent to the English second sentence type SVC.

As an example, to express "I am a student." in the SFGPL, use the following.

```SFGPL
{I_am_a_student}
```

In this case, ```{noun_eq}``` is the word to be added when the sentence type is "SVC".

The ```{I}``` denotes the first person pronoun "I".

Next, ```{verb_none}``` is a word indicating that the verb is nonsense.
In ```{verb_none}```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to that of the English verb "be".

And ```{student}``` denotes the noun "student".
In this case, the article that exists in English and other languages does not exist in the SFGPL, so there is no need to add any article.

### Syntax with {noun_haveP}

Next, we present an example using ```{noun_haveP}```.
This ```{noun_haveP}``` has three arguments: the first is the subject of the sentence, the second is the verb of the sentence and the third is the complement of the subject.
Also, the complement of the third argument must be a modifier.
In other words, ```{noun_haveP}``` can produce sentences equivalent to the English second sentence type SVC.

As an example, to express "I am happy." in the SFGPL, do the following.

```SFGPL
{I_am_happy}
```

In this case, ```{noun_haveP}``` is the word to be added when the sentence type is "SVC".

The ```{I}``` denotes the first person pronoun "I".

Next, ```{verb_none}``` is a word indicating that the verb is nonsense.
In ```{verb_none}```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to that of the English verb "be".

And ```{happy}``` denotes the modifier "happy".

### Syntax with {noun_doT}

We then present an example using ```{noun_doT}```.
This ```{noun_doT}``` has three arguments, the first representing the subject of the sentence, the second the verb of the sentence and the third the object.
In other words, ```{noun_doT}``` can produce sentences equivalent to SVO, the third sentence type in English.

For example, to express "I open the door." in SFGPL, use the following.

```SFGPL
{I_open_the_door}
```

In this case, ```{noun_doT}``` is the word to be added when the sentence type is "SVO".

The ```{I}``` denotes the first person pronoun "I".

Next, ```{open}``` denotes the verb "open".

Next, ```{door}``` denotes the noun "door".

### Syntax with {noun_give}

Next, we present an example using ```{noun_give}```.
This ```{noun_give}``` has four arguments, the first representing the subject of the sentence, the second the verb of the sentence, the third the indirect object and the fourth the direct object.
In other words, ```{noun_give}``` can produce sentences equivalent to SVOO, the fourth sentence type in English.

For example, to express "I give you a box." in SFGPL, you can do the following.

```SFGPL
{I_give_you_a_box}
```

In this case, ```{noun_give}``` is a word that is added when the sentence type is "SVOO".

The ```{I}``` denotes the first person pronoun "I".

Next, ```{verb_none}``` is a word indicating that the verb is nonsense.
In ```{verb_none}```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to the English word give.

And ```{you}``` denotes the second person pronoun "you".

Furthermore, ```{box}``` denotes the noun "box".

### Syntax with {noun_makeN}

Next, we present an example using ```{noun_makeN}```.
This ```{noun_makeN}``` has four arguments: the first is the subject of the sentence, the second the verb of the sentence, the third the object and the fourth the complement of the object.
The complement of the fourth argument must be a noun.
In other words, ```{noun_makeN}``` can produce sentences equivalent to the English fourth sentence type SVOC.

For example, to express "I make you a teacher." in SFGPL, use the following.

```SFGPL
{I_make_you_a_teacher}
```

In this case, ```{noun_makeN}``` is the word to be added when the sentence type is "SVOC".

The ```{I}``` denotes the first person pronoun "I".

Next, ```{verb_none}``` is a word indicating that the verb is nonsense.
In ````{verb_none}```, the meaning changes depending on the location.
In this case, in the example sentence, the meaning is equivalent to the English causative verb make.

And ```{you}``` denotes the second person pronoun "you".

Furthermore, ```{teacher}``` represents the noun "teacher".

### Syntax with {noun_makeM}

Next, we present an example using ```{noun_makeM}```.
This ```{noun_makeM}``` has four arguments: the first is the subject of the sentence, the second the verb of the sentence, the third the object and the fourth the complement of the object.
The complement of the fourth argument must be a modifier.
In other words, ```{noun_makeM}``` can produce sentences equivalent to the English fourth sentence type SVOC.

As an example, to express "I make you happy." in the SFGPL, use the following.

```SFGPL
{I_make_you_happy}
```

In this case, ```{noun_makeM}``` is the word to be added when the sentence type is "SVOC".

The ```{I}``` denotes the first person pronoun "I".

Next, ```{verb_none}``` is a word indicating that the verb is nonsense.
In ````{verb_none}```, the meaning changes depending on the location.
In this case, in the example sentence, the meaning is equivalent to the English causative verb make.

And ```{you}``` denotes the second person pronoun "you".

Furthermore, ```{happy}``` represents the modifier "happy".

### Syntax with {noun_have}

Next, we present an example using ```{noun_have}```.
This ```{noun_have}``` has three arguments, the first representing the subject of the sentence (the owner), the second the verb of the sentence and the third the object (the possession).
Therefore, ```{noun_have}``` can represent the sentence "S has O".

As an example, to express "I have a box." in SFGPL, use the following.

```SFGPL
{I_have_a_box}
```

In this case, ```{noun_have}``` is the word used to make a sentence expressing possession.

The ```{I}``` is the first person pronoun "I".

Next, ```{verb_none}``` is a word that indicates that the verb is meaningless.
In ```{verb_none}```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to the English word have.

Furthermore, ```{box}``` denotes the noun "box".

### Syntax with {noun_belong}

Next, we present an example using ```{noun_belong}```.
This ```{noun_belong}``` has three arguments, the first representing the subject of the sentence (the person or thing to which it belongs), the second the verb of the sentence and the third the object (place of affiliation).
Therefore, ```{noun_belong}``` can represent the sentence "S belongs to O".

As an example, to express "I belong to a school." in SFGPL, use the following.

```SFGPL
{I_belong_to_a_school}
```

In this case, ```{noun_belong}``` is a word that is added to make a statement of belonging.

The ```{I}``` denotes the first person pronoun "I".

Next, ```{verb_none}``` is a word that indicates that the verb is meaningless.
In ```{verb_none}```, the meaning changes depending on the location.
In the example sentence, the meaning is equivalent to "belong to" in English.

Furthermore, ```{school}``` denotes the noun "school".

### Other syntaxes

Other syntaxes are indicated by [sentence pattern]({docs_sentence_pattern}).

## Modification methods

### How to modify nouns

There are two main ways of modifying nouns: with modifiers and with nouns.

#### How to modify a noun with a modifier

For example, to express that a certain box is big, in English we say "The box is big.".
Similarly, the SFGPL uses ```{noun_haveP}``` to express an SVC as follows:.

```SFGPL
{the_box_is_big}
```

In this case, ```{big}``` means big.

#### How to modify a noun with a noun for a noun

This method is used in situations where the English preposition "of" or the Japanese particle "の" is used.
However, the SFGPL does not allow for concise notation, and even in such cases it is qualified by sentences like English relative pronouns ([compound sentences]({docs_CompoundSentences})).

For example, "My box is big." can be expressed by the following sentence.

```SFGPL
{my_box_is_big}
```

In this sentence, the sentence ```{I_have_a___box_}``` is nested in the subject of the main sentence.
This ```{I_have_a___box_}``` means "I have a box.
In addition, the use of ```{determinerN_stressed}``` can be used to emphasise words that are particularly important in the sentence.
Thus, in this sentence, ```{stressed_box}``` is used to emphasise the word "box".

Overall, the literal translation means "[I have a **box**] is big.", which is equivalent to "My box is big.".

### How to modify verbs

#### Simple verb modification methods

Verbs can be modified using ```{verb_add}```.
In ```{verb_add}```, the first argument is the verb and the second argument is the modifier.

For example, to express "I quickly run.".

```SFGPL
{I_quickly_run}
```

In this case, ```{quickly}``` means "quickly".
In ```{run_quickly}```, the verb "run" is modified by the modifier "quickly", meaning "quickly run".

#### How to convert a noun phrase into a modifier and modify a verb

The SFGPL allows you to convert a noun phrase into a modifier, which then modifies a verb.
This is similar to adverbialisation using prepositions in English.

First, the SFGPL has [words that can be converted between parts of speech]({docs_partOfSpeechConversion}), which in this case uses ```{modifier_N2M}``` to convert a noun to a modifier.
In this usage, a [noun determiner]({docs_DeterminerN}) is used in parallel with ```{modifier_N2M}``` to limit the meaning of the noun phrase.

For example, to express "I go to Tokyo." in SFGPL.

```SFGPL
{I_go_to_Tokyo}
```

Firstly, ```{go}``` expresses the English word "go", and the destination is expressed by modifying the verb.
In particular, the four words ```{to_Tokyo}``` represent "to Tokyo".
The three words ```{modifier_N2M}``` are noun-to-modifier words, and ```{determinerN_place}``` is a nominal determiner of place.
Combining these two words with ```{Tokyo}``` (Tokyo) to express the meaning "to Tokyo".

### How to modify modifiers

The modifier modification is expressed using ````{modifier_add}```.
In this ```{modifier_add}```, the modifier of the second argument modifies the modifier of the first argument.

For example, to express "Your box is a little big." in the SFGPL, use the following.

```SFGPL
{Your_box_is_a_little_big}
```

In this case, ```{a_little}``` (= "a little") modifies ```{big}``` (= "big"), so that ```{a_little_big}``` means "a little big".

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|run|{run}|
|student|{student}|
|happy|{happy}|
|open|{open}|
|door|{door}|
|you|{you}|
|box|{box}|
|teacher|{teacher}|
|school|{school}|
|big|{big}|
|quickly|{quickly}|
|go|{go}|
|Tokyo|{Tokyo}|
|a little|{a_little}|
