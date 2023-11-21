# Verb Conjugation

[TOP](../../readme.md)
/
[JP](../jp/verbConjugation.md)

## Verb tenses

Verb tenses exist in the SFGPL as shown in the figure below.

![BasingPoint](../img/BasingPoint.jpg)

Thus, there are three tenses in the SFGPL: ① past tense, ② present tense, and ③ future tense.
These tenses are fundamental to verb conjugation and serve as reference points for sentence time.
Example sentences using the tenses are shown in the following table.

|Tense|English|SFGPL|
|:-:|:-:|:-:|
|①Past Tense|I lived in Tokyo.|{I_lived_in_Tokyo}|
|②Present Tense|I live in Tokyo.|{I_live_in_Tokyo}|
|③Future Tense|I will live in Tokyo.|{I_will_live_in_Tokyo}|

In particular, ```{phrase_past}``` and ```{phrase_future}``` are attached to the sentence itself.

### Extended verb tenses

The verbs described in the previous section are the most basic way of expressing verb tenses.
However, in the SFGPL, there are words that are mainly used to combine tenses, depending on the DetermineV class.
The extended tense by the DeterminerV class has a lower priority than the base tense by the Phrase class, and the base tense basically represents the tense of the entire sentence.
The following table shows the words that represent the extended tense.

|Tense|Word|
|:-:|:-:|
|①Past Tense|{determinerV_past}|
|②Present Tense|{determinerV_present}|
|③Future Tense|{determinerV_future}|

These tenses can be combined to form compound tenses such as future past tense and past future tense.
The following is an example of the future past tense, which expresses the past at a future point in time.

```SFGPL
{I_would_live_in_Tokyo}
```

In summary, the tenses in the SFGPL are as shown in the table below.
The column names in the table below indicate the types of the base tense by Phrase, and the row names indicate the types of the extended tense by DeterminerV.
In ```A/B```, A denotes the base tense and B the extended tense.

||Past Tense|-|Future Tense|
|:-:|:-:|:-:|:-:|
|**-**|{phrase_past}/-|-/-|{phrase_future}/-|
|**Past Tense**|{phrase_past}/{determinerV_past}|-/{determinerV_past}|{phrase_future}/{determinerV_past}|
|**Present Tense**|{phrase_past}/{determinerV_present}|-/{determinerV_present}|{phrase_future}/{determinerV_present}|
|**Future Tense**|{phrase_past}/{determinerV_future}|-/{determinerV_future}|{phrase_future}/{determinerV_future}|

## Phases

In SFGPL, there are six phases as shown in the figure below: ①start phase, ②transitional phase, ③completion phase, ④continuation phase, ⑤finish phase, and ⑥progression phase.

![ProgressiveForm](../img/ProgressiveForm.jpg)

The following table shows example sentences in each phase for ```{I_wear_a_dress}``` meaning "I wear dress".

|Phase|Word|English|SFGPL|
|:-:|:-:|:-:|:-:|
|①Start Phase|{verb_start}|I begin wear a dress.|{I_begin_wear_a_dress}|
|②Transitional Phase|{verb_condition}|I am (in the process of) wearing a dress.|{I_am_in_the_process_of_wearing_a_dress}|
|③Completion Phase|{verb_complete}|I wear a dress. (I just finished wearing it.)|{I_wear_a_dress_complete}|
|④Continuation Phase|{verb_continue}|I am wearing a dress. (The state in which it is worn.)|{I_am_wearing_a_dress_continue}|
|⑤Finish Phase|{verb_end}|I finish wear a dress. (I stopped wearing it.)|{I_finish_wear_a_dress}|
|⑥Progression Phase|{verb_progressive}|I am wearing a dress.|{I_am_wearing_a_dress}|

These phases can be in the past or future tense in addition to the present tense.
⑥ Progressive phase includes ② transitional phase and ④ continuation phase.
There are also cases where ③ the completion phase and ⑤ the finish phase are the same.
"I begin wear a dress." in the past and future tenses is as follows.

```SFGPL
{I_began_wear_a_dress}
{I_began_will_begin_a_dress}
```

As a rule, a phase alone does not indicate a range of time, but only the moment in which it occurs.
When expressing a range of time, the perfect tense is added.
The progressive form plus the perfect form to express "I have been wearing a dress.".

```SFGPL
{I_have_been_wearing_a_dress}
```

### General progressive form

In SFGPL, we can make a simple progressive form as in ⑥ without considering the phases ① to ⑤ in the previous section.
The SFGPL can be expressed in the progressive form meaning "I am wearing the dress." as follows.

```{I_am_wearing_the_dress}```

Progressive forms ```{verb_progressive}``` are attached to verbs.
They can be past or future tense as well as present tense.
"I am wearing the dress." in the past and future tenses is as follows.

```SFGPL
{I_was_wearing_the_dress}
{I_will_be_wearing_the_dress}
```

## Perfect tense

In the SFGPL, there is a perfect tense equivalent to English, as shown in the figure below.

![PerfectForm](../img/PerfectForm.jpg)

This perfect tense is used to indicate that something that has happened in the past is continuing.
Examples of the perfect tense for the three tenses are as follows.

|Tense|English|SFGPL|
|:-:|:-:|:-:|
|①Past Perfect Tense|I had lived in Tokyo.|{I_had_lived_in_Tokyo}|
|②Present Perfect Tense|I have lived in Tokyo.|{I_have_lived_in_Tokyo}|
|③Future Perfect Tense|I will have lived in Tokyo.|{I_will_have_lived_in_Tokyo}|

In ```{verb_perfective}```, the perfective form is attached to and modifies the verb itself.

## Passive voice

SFGPL can express the passive voice with the meaning "The dress is worn.".

```{the_dress_is_worn}```

The ```{verb_passive}```, which indicates the passive form, is attached to the verb.
These can be in the past or future tense as well as the present tense.
"The dress is worn." in the past and future tenses is as follows.

```SFGPL
{the_dress_was_worn}
{the_dress_will_be_worn}
```

## Other verb modifiers

Functions in the [DeterminerV](DeterminerV.md) class can modify other verbs.
They are similar to English auxiliary verbs.

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|live|{live}|
|in Tokyo|{in_Tokyo}|
|wear|{wear}|
|dress|{dress}|
