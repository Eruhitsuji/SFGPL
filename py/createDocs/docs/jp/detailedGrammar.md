{page_header}

SFGPLは基本的に，[文型]({docs_sentence_pattern})に記されているような文法は厳守する必要があるが，その他はユーザ側である程度決めてよい．
しかし，模範的な文法を本章で記述しておく．

## 文章を修飾する方法

文章全体に対して修飾するためには，基本的にその文内の動詞を```{verb_add}```を使用することで修飾する．
例えば，"I go to Tokyo."という例文では，"to Tokyo"の部分が修飾語となる．
その際SFGPLでは次のように表現する．

```SFGPL
{I_go_to_Tokyo_1}
```

また，別の方法として，```{noun_havep}```を使う方法もある．

```SFGPL
{I_go_to_Tokyo_2}
```

### 英語における前置詞的な用法

特に，英語における前置詞のように動詞を修飾する場合，```{modifier_n2m}```と[DeterminerN]({docs_DeterminerN})を使用して表現する．
英語の前置詞とSFGPLの一例を次の表に示す．

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

## 比較表現の文法

SFGPLでは，英語における比較級を使った比較表現は，```{noun_gt}```によって定義されているが，最上級や同級による比較は定義されていない．
このような文は次のように表すことを推奨する．

### 比較級

"A is B(-er) than C"のような比較表現は，```{noun_gt}```によって表現する．
"My bag is bigger than yours."は，次のように表現する．

```SFGPL
{my_bag_is_bigger_than_yours}
```

### 最上級

"A is the B(-est) in/of C"のような比較表現は，次のような構文で表現する．

```SFGPL
{superlative_exp}
```

"My bag is the biggest in my class."は，次のように表現する．

```SFGPL
{my_bag_is_the_biggest_in_my_class}
```

また，「N番目にXな」を表現するとき，修飾語に数値を付与して```{superlative_number}```のように表す．
序数を使用した"My bag is the second biggest in my class."は次のように表現する．

```SFGPL
{my_bag_is_the_2nd_biggest_in_my_class}
```

### 同級

"A is as B as C"のような比較表現は，次のような構文で表現する．
このとき，"似ている"という意味の```{wordM_near}```を使って表現する．

```SFGPL
{equivalent_classes_exp}
```

"My bag is as big as his."は，次のように表現する．

```SFGPL
{my_bag_is_as_big_as_his}
```

## 通時的な文

習慣や周期的な事柄，不変の事実などの恒常的な事柄や事実を表すには，現在と同様に時制をつけないことで表現する．

SFGPLで"I cook every day."を表すには次のようにする．

```SFGPL
{I_cook_every_day}
```

また，SFGPLで"The Earth revolves around the Sun."を表すには次のようにする．

```SFGPL
{the_earth_revolves_around_the_sun}
```

そして，SFGPLで"English is spoken all over the world."を表すには次のようにする．

```SFGPL
{English_is_spoken_all_over_the_world}
```

## 主題優勢言語的な文法

日本語や中国語，朝鮮語，インドネシア語などの主に東アジアの言語によく見られる，主題優勢言語のような文を作成することができる．
主題優勢言語は，通常の主語の他に，文の主題を提示できるような文法が存在する言語である．
これにより，主題と主語の両方を含む文を容易に表現できる．
SFGPLでは，東アジア諸言語のような明確な方法ではないが，簡易的に主題を含む文を作成できる．

### 主題もしくは主語の片方を含む文

主題もしくは主語の片方を含む文は，[文型]({docs_sentence_pattern})と同様に文を構築する．

### 主題と主語の両方を含む文

主題と主語の両方を含む文は，次のように表現する．
このときの"T"は主題，"C"はコメント（主題を説明する文や単語等）で構成される．

```SFGPL
{include_topic_and_subject_exp}
```

例として，日本語の「象は鼻が長い」をSFGPLで表現するには次のようになる．

```SFGPL
{Elephants_have_long_noses}
{Elephants_have_long_noses_en}
```

## 単語集

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
|象|{象}|
|鼻|{鼻}|
|長い|{長い}|
|elephant|{elephant}|
|nose|{nose}|
|long|{long}|
