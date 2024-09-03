# 5. Interrogative Sentence

[TOP](../../readme.md)
/
[JP](../jp/interrogativeSentence.md)

## Yes–no question

Use ```da``` to create interrogative sentences.
When this word is added to a sentence, it becomes a interrogative sentence.
"You have a table." is ```mi ge so fa 'table'``` under the SFGPL.
To make it mean "Do you have a table?", it can be expressed as follows in the SFGPL.

```SFGPL
da mi ge so fa 'table'
```

Such a question reply is expressed by using Bool.B2N```pis``` to indicate whether the proposition is true or false, as follows.

```SFGPL
pis mi ga so pen gi pos
pis mi ga so pen gi pas
```

## wh-questions

In the case of interrogative sentences containing interrogatives, the indefinite is expressed by replacing the indefinite with an interrogative.
Interrogatives are represented by a combination of the interrogative pronoun ```wa``` and [noun determiner](DeterminerN.md).

"Who has a table?" is expressed as follows.

```SFGPL
da mi ben wa so fa 'table'
```

"What do you have?" is expressed as follows.

```SFGPL
da mi ge so pen wa
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|you|ge|
|table|fa 'table'|
|who|ben wa|
|what|pen wa|
