# 動詞の活用

[TOP](../../readme.md)
/
[EN](../en/verbConjugation.md)

## 動詞の時制

SFGPLでは以下の図のような動詞の時制が存在する．

![BasingPoint](../img/BasingPoint.jpg)

このように，SFGPLでは①過去形，②現在形，③未来形の3つの時制が存在する．
これら時制は動詞の活用として基礎的なもので，文の時間の基準点となる．
時制を使用した例文は次の表のようになる．

|時制|English|SFGPL|
|:-:|:-:|:-:|
|①過去形|I lived in Tokyo.|{I_lived_in_Tokyo}|
|②現在形|I live in Tokyo.|{I_live_in_Tokyo}|
|③未来形|I will live in Tokyo.|{I_will_live_in_Tokyo}|

特に```{phrase_past}```と```{phrase_future}```では，文章自体に付属し形容する．

## 完了形

SFGPLでは，以下の図のような，英語と同等な完了形が存在する．

![PerfectForm](../img/PerfectForm.jpg)

この完了形では過去に起こったことが続いていることを表す際に使用する．
3つの時制に対する完了形の例は次のようになる．

|時制|English|SFGPL|
|:-:|:-:|:-:|
|①過去完了形|I had lived in Tokyo.|{I_had_lived_in_Tokyo}|
|②現在完了形|I have lived in Tokyo.|{I_have_lived_in_Tokyo}|
|③未来完了形|I will have lived in Tokyo.|{I_will_have_lived_in_Tokyo}|

完了形を表す```{verb_perfective}```では，動詞自体に付属し，修飾する．

## 進行形

SFGPLは次のように，"I am wearing the dress."という意味の進行形を表すことができる．

```{I_am_wearing_the_dress}```

進行形を表す```{verb_progressive}```は動詞に付属する．
これらは，現在形以外にも，過去形，未来形にできる．
"I am wearing the dress."を過去形，未来形にすると次のようになる．

```SFGPL
{I_was_wearing_the_dress}
{I_will_be_wearing_the_dress}
```

## 受動態

SFGPLは次のように，"The dress is worn."という意味の受動態を表すことができる．

```{the_dress_is_worn}```

受動態を表す```{verb_passive}```は動詞に付属する．
これらは，現在形以外にも，過去形，未来形にできる．
"The dress is worn."を過去形，未来形にすると次のようになる．

```SFGPL
{the_dress_was_worn}
{the_dress_will_be_worn}
```

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|live|{live}|
|in Tokyo|{in_Tokyo}|
|wear|{wear}|
|dress|{dress}|
