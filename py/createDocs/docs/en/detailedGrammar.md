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

## Grammar of comparative expressions

In the SFGPL, comparative expressions using comparative classes in English are defined by ```{noun_gt}```, but not comparisons using superlative or equivalent classes.
It is recommended that such sentences be expressed as follows.

### Comparative degree

Comparative expressions such as "A is B(-er) than C" are expressed by ```{noun_gt}```.
"My bag is bigger than yours." is expressed as follows.

```SFGPL
{my_bag_is_bigger_than_yours}
```

### Superlative

Comparative expressions such as "A is the B(-est) in/of C" are expressed with the following syntax.

```SFGPL
{superlative_exp}
```

"My bag is the biggest in my class." is expressed as follows.

```SFGPL
{my_bag_is_the_biggest_in_my_class}
```

When expressing "the N-th X(-est)", a numerical value is added to the modifier, as in ```{superlative_number}```.
"My bag is the second biggest in my class." using ordinal numbers is expressed as follows.

```SFGPL
{my_bag_is_the_2nd_biggest_in_my_class}
```

### Equivalent classes

Comparative expressions such as "A is as B as C" are expressed with the following syntax.
In this case, use ```{wordM_near}``` to mean "similar".

```SFGPL
{equivalent_classes_exp}
```

"My bag is as big as his." is expressed as follows.

```SFGPL
{my_bag_is_as_big_as_his}
```

## Diachronic sentences

Constant matters and facts, such as customs, periodic matters and unchanging facts, are expressed by not adding a tense, as is the case with the present.

To express "I cook every day." in SFGPL, use the following.

```SFGPL
{I_cook_every_day}
```

"The Earth revolves around the Sun." in the SFGPL can be expressed as follows.

```SFGPL
{the_earth_revolves_around_the_sun}
```

And to express "English is spoken all over the world." in the SFGPL as follows.

```SFGPL
{English_is_spoken_all_over_the_world}
```

## Topic-prominent linguistic grammar

It is possible to produce sentences like those in topic-prominent languages, which are common in East Asian languages such as Japanese, Chinese, Korean, and Indonesian.
A topic-prominent language is a language in which, in addition to the usual subject, there is a grammar that allows the subject of the sentence to be presented.
This makes it easy to produce sentences that contain both a topic and a subject.
The SFGPL allows for the production of sentences containing topics in a simplified manner, though not in the explicit manner of the East Asian languages.

### Sentences containing a subject or one of the topic or subject

Sentences containing a topic or subject fragment are constructed in the same way as [sentence type]({docs_sentence_pattern}).

### Sentences containing both a topic and a subject

A sentence containing both a topic and a subject is expressed as follows.
In this case, “T” is the topic, and “C” consists of comments (sentences, words, etc. that explain the topic).

```SFGPL
{include_topic_and_subject_exp}
```

As an example, the Japanese phrase "象は鼻が長い"(“Elephants have long noses” [topic: elephant, subject: nose]) can be expressed in SFGPL as follows.

```SFGPL
{Elephants_have_long_noses}
{Elephants_have_long_noses_en}
```

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|go|{go}|
|to Tokyo|{to_tokyo}|
|bag|{bag}|
|big|{big}|
|yours(possessive)|{yours_possessive}|
|my class|{my_class}|
|his(possessive)|{his_possessive}|
|cook|{cook}|
|every day|{every_day}|
|the Earth|{the_earth}|
|revolve|{revolve}|
|the Sun|{the_sun}|
|English|{English}|
|speak|{speak}|
|all over the world|{all_over_the_world}|
|象(elephant)|{象}|
|鼻(nose)|{鼻}|
|長い(long)|{長い}|
|elephant|{elephant}|
|nose|{nose}|
|long|{long}|
