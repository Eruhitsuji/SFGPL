{page_header}

Basically, the SFGPL must adhere strictly to the grammar as described in [sentence pattern]({docs_sentence_pattern}), but the rest may be decided to some extent by the user.
However, an exemplary grammar is described in this chapter.

## How to qualify a sentence

To modify a whole sentence, you basically modify the verbs in that sentence by using ```{verb_add}```.
For example, in the example sentence "I go to Tokyo.", the "to Tokyo" part is a modifier.
In this case, the SFGPL uses the following.

```SFGPL
{I_go_to_Tokyo_1}
```

Another alternative is to use ```{noun_havep}```.

```SFGPL
{I_go_to_Tokyo_2}
```

### Prepositional usage in English

In particular, when modifying verbs, like prepositions in English, they are expressed using ```{modifier_n2m}``` and [DeterminerN]({docs_DeterminerN}).
Examples of English prepositions and SFGPLs are given in the following table.

|English|Meaning|SFGPL|
|:-:|:-:|:-:|
|at/in/on/to/from|Time|{pre_time}|
|at/in/on/to/from|Place|{pre_place}|
|for|Reason|{pre_reason}|
|for|Way/Means|{pre_way}|
|from|Start|{pre_start}|
|to|End|{pre_end}|
|between/among|Section|{pre_section}|
|in|In|{pre_in}|
|into|Into|{pre_into}|
|out|Out|{pre_out}|
|up/over|Move&Above|{pre_up}|
|above|Above|{pre_above}|
|down|Move&Below|{pre_down}|
|under|On&Below|{pre_under}|
|below|Below|{pre_below}|
|on|On|{pre_on}|
|right|Right|{pre_right}|
|left|Left|{pre_left}|
|near|Near|{pre_near}|
|by/about|By/About|{pre_by}|
|with|With|{pre_with}|

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|go|{go}|
