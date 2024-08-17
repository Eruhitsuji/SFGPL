# 9. 詳細な文法

[TOP](../../readme.md)
/
[EN](../en/detailedGrammar.md)

SFGPLは基本的に，[文型](sentence_pattern.md)に記されているような文法は厳守する必要があるが，その他はユーザ側である程度決めてよい．
しかし，模範的な文法を本章で記述しておく．

## 文章を修飾する方法

文章全体に対して修飾するためには，基本的にその文内の動詞を```na```を使用することで修飾する．
例えば，"I go to Tokyo."という例文では，"to Tokyo"の部分が修飾語となる．
その際SFGPLでは次のように表現する．

```SFGPL
ta ga na sa 'go' li pun fa 'Tokyo'
```

また，別の方法として，```me```を使う方法もある．

```SFGPL
me ta ga sa 'go' so li pun fa 'Tokyo'
```

### 英語における前置詞的な用法

特に，英語における前置詞のように動詞を修飾する場合，```li```と[DeterminerN](DeterminerN.md)を使用して表現する．
英語の前置詞とSFGPLの一例を次の表に示す．

|English|Meaning|SFGPL|
|:-:|:-:|:-:|
|at/in/on/to/from|Time|li pin|
|at/in/on/to/from|Place|li pun|
|for|Reason|li pon|
|for|Way/Means|li ban|
|from|Start|li fan|
|to|End|li fen|
|between/among|Section|li fin|
|in|In|li fun|
|into|Into|li tun fun|
|out|Out|li fon|
|up/over|Move&Above|li tun man|
|above|Above|li man|
|down|Move&Below|li tun men|
|under|On&Below|li min men|
|below|Below|li men|
|on|On|li min|
|right|Right|li mun|
|left|Left|li mon|
|near|Near|li tin|
|by/about|By/About|li tan tin|
|with|With|li ten tin|

## 比較表現の文法

SFGPLでは，英語における比較級を使った比較表現は，```mo```によって定義されているが，最上級や同級による比較は定義されていない．
このような文は次のように表すことを推奨する．

### 比較級

"A is B(-er) than C"のような比較表現は，```mo```によって表現する．
"My bag is bigger than yours."は，次のように表現する．

```SFGPL
mo mi ga so san fa 'big' so wan sen ge
```

### 最上級

"A is the B(-est) in/of C"のような比較表現は，次のような構文で表現する．

```SFGPL
me A V ka ki B li fun C
```

"My bag is the biggest in my class."は，次のように表現する．

```SFGPL
me mi ga so san fa 'bag' so ka ki wan li fun mu ga so san fa 'class'
```

また，「N番目にXな」を表現するとき，修飾語に数値を付与して```ka X li N```のように表す．
序数を使用した"My bag is the second biggest in my class."は次のように表現する．

```SFGPL
me mi ga so san fa 'bag' so ka ki ka wan li mal pil li fun mu ga so san fa 'class'
```

### 同級

"A is as B as C"のような比較表現は，次のような構文で表現する．
このとき，"似ている"という意味の```wen```を使って表現する．

```SFGPL
me ba A C V ka B wen
```

"My bag is as big as his."は，次のように表現する．

```SFGPL
me ba mi ga so san fa 'bag' sen lan gi so ka wan wen
```

## 通時的な文

習慣や周期的な事柄，不変の事実などの恒常的な事柄や事実を表すには，現在と同様に時制をつけないことで表現する．

SFGPLで"I cook every day."を表すには次のようにする．

```SFGPL
ta ga na sa 'cook' li pin me fa 'day' so la 'every'
```

また，SFGPLで"The Earth revolves around the Sun."を表すには次のようにする．

```SFGPL
ta fa 'Earth' na sa 'revolve' li tun tin fa 'Sun'
```

そして，SFGPLで"English is spoken all over the world."を表すには次のようにする．

```SFGPL
ta fa 'English' na ne sa 'speak' li fun dan fa 'world'
```

## 主題優勢言語的な文法

日本語や中国語，朝鮮語，インドネシア語などの主に東アジアの言語によく見られる，主題優勢言語のような文を作成することができる．
主題優勢言語は，通常の主語の他に，文の主題を提示できるような文法が存在する言語である．
これにより，主題と主語の両方を含む文を容易に表現できる．
SFGPLでは，東アジア諸言語のような明確な方法ではないが，簡易的に主題を含む文を作成できる．

### 主題もしくは主語の片方を含む文

主題もしくは主語の片方を含む文は，[文型](sentence_pattern.md)と同様に文を構築する．

### 主題と主語の両方を含む文

主題と主語の両方を含む文は，次のように表現する．
このときの"T"は主題，"C"はコメント（主題を説明する文や単語等）で構成される．

```SFGPL
ma T so C
```

例として，日本語の「象は鼻が長い」をSFGPLで表現するには次のようになる．

```SFGPL
ma fa '象' so me fa '鼻' so la '長い'
ma fa 'elephant' so me fa 'nose' so la 'long'
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|ga|
|go|sa 'go'|
|to Tokyo|li pun fa 'Tokyo'|
|bag|fa 'bag'|
|big|wan|
|yours(possessive)|sen ge|
|my class|mu ga so san fa 'class'|
|his(possessive)|sen lan gi|
|cook|sa 'cook'|
|every day|me fa 'day' so la 'every'|
|the Earth|fa 'Earth'|
|revolve|sa 'revolve'|
|the Sun|fa 'Sun'|
|English|fa 'English'|
|speak|sa 'speak'|
|all over the world|li fun dan fa 'world'|
|象|fa '象'|
|鼻|fa '鼻'|
|長い|fa '長い'|
|elephant|fa 'elephant'|
|nose|fa 'nose'|
|long|la 'long'|
