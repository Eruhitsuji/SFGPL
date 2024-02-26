{page_header}

## Negative statement

Use ```{langobj_not}``` to create a normal negative sentence.
This word is attached to a sentence to make a negative sentence.
"I have a table." is ```{I_have_a_table}``` under the SFGPL.
To negate this whole sentence and make it mean "I don't have a table." in the negative sentence, the SFGPL can be expressed as follows.

```SFGPL
{I_don't_have_a_table}
```

## Negation of verbs

In SFGPL, besides negating whole sentences, it is also possible to negate verbs alone.
Negating an entire sentence and negating only the verb may have different meanings.
In satellite-framed languages such as English, in particular, the interpretation of their meanings may differ.

For example, in "I don't have a table.", the negation of the whole sentence and the negation of the verb alone are almost synonymous.

|||
|:-:|:-:|
|All Sentence|{a_I_don't_make_a_table}|
|Only Verb|{v_I_don't_make_a_table}|

In "I didn't run to my school.", the negation of the whole sentence and the negation of the verb alone have different meanings.

|||
|:-:|:-:|
|All Sentence|{a_I_didn't_ran_my_school}|
|Only Verb|{v_I_didn't_ran_my_school}|

In the case of the negation of the whole sentence, all events other than "I ran to my school." are represented.
In other words, it also implies "I walked to my school", "I didn't go to my school", etc.

However, in the case of verb-only negation, it implies an action other than "running" in the event "I went to my school.".
In other words, it implies other means, such as "I walked to my school.", but not "I didn't go to my school.".

On the other hand, in verb-framed languages such as Japanese, such differences in meaning tend to disappear because they are expressed by compound verbs such as "走って行く".
In this case, the compound verb "走って行く" contains both the method of action "走る(to run)" and the result of the action "行く(to go)", unlike in English.

## Negative forms of modifiers

In a modifier, the suffix ```{modifier_neg}``` can be used to indicate a synonym of the modifier.

For example, the synonym "small" for ```{big}```, which means "big", can be expressed by adding ```{neg_big}```.

"My table is small." can be expressed in SFGPL as follows.

```SFGPL
{my_table_is_small}
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|table|{table}|
|big|{big}|
