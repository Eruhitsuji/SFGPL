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

## Wordbook

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|go|{go}|
|to Tokyo|{to_tokyo}|
