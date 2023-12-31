{page_header}

SFGPLでは，時制や相，助動詞などの動詞を修飾する語が備わっている．
これらの語は，主に，動詞に直接付属し修飾するものと，文全体に修飾するものが存在する．

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

また，②の現在形は，何も付属しないことで，通常は現在のことを表す．
しかし，本来は不定時制であり，特に時制を必要としない場合にも使われる．

### 動詞の拡張時制

前項で説明した動詞は，一番基本的な動詞の時制の表し方である．
しかし，SFGPLではDeterminVクラスにによって，主に時制を組み合わせるための単語が存在する．
また，このDeterminerVクラスによる拡張時制は，Phraseクラスによる基礎時制より優先度が低く，基本的には基礎時制で文全体の時制を表す．
以下の表は拡張時制を表す単語である．

|時制|単語|
|:-:|:-:|
|①過去形|{determinerV_past}|
|②現在形|{determinerV_present}|
|③未来形|{determinerV_future}|

これらの時制を組み合わせることで，未来過去形や過去未来形などの複合時制を作ることができる．
次の例は，未来の時点で過去を表す未来過去形の例である．  

```SFGPL
{I_would_live_in_Tokyo}
```

まとめるとSFGPLにおける時制は以下の表のようなものが存在する．
以下の表の列名はPhraseによる基礎時制の種類，行名はDeterminerVによる拡張時制の種類を表している．
また，```A/B```でAは基礎時制，B拡張時制を表す，

||Past Tense|-|Future Tense|
|:-:|:-:|:-:|:-:|
|**-**|{phrase_past}/-|-/-|{phrase_future}/-|
|**Past Tense**|{phrase_past}/{determinerV_past}|-/{determinerV_past}|{phrase_future}/{determinerV_past}|
|**Present Tense**|{phrase_past}/{determinerV_present}|-/{determinerV_present}|{phrase_future}/{determinerV_present}|
|**Future Tense**|{phrase_past}/{determinerV_future}|-/{determinerV_future}|{phrase_future}/{determinerV_future}|

## 動作の時間軸に関する相

SFGPLでは下の図のように，①起動相，②経過相，③完結相，④継続相，⑤終了相，⑥進行相の6つが存在する．

![ProgressiveForm](../img/ProgressiveForm.jpg)

"I wear dress"という意味の```{I_wear_a_dress}```について，それぞれの相での例文を次の表に示す．

|相|単語|English|SFGPL|
|:-:|:-:|:-:|:-:|
|①起動相|{verb_start}|I begin wear a dress.|{I_begin_wear_a_dress}|
|②経過相|{verb_condition}|I am (in the process of) wearing a dress.|{I_am_in_the_process_of_wearing_a_dress}|
|③完結相|{verb_complete}|I wear a dress. (I just finished wearing it.)|{I_wear_a_dress_complete}|
|④継続相|{verb_continue}|I am wearing a dress. (The state in which it is worn.)|{I_am_wearing_a_dress_continue}|
|⑤終了相|{verb_end}|I finish wear a dress. (I stopped wearing it.)|{I_finish_wear_a_dress}|
|⑥進行相|{verb_progressive}|I am wearing a dress.|{I_am_wearing_a_dress}|

①起動相，③完結相，⑤終了相では，ある動作に対しての瞬間の一点だけを表す．

②経過相，④継続相，⑥進行相は，ある動作に対しての期間を表す．
⑥進行相は②経過相と④継続相が含まれた，不明瞭な期間を表す．
また，一部の動詞では，それぞれとの相との間が一瞬であり，ほとんど区別できない場合がある．

これらの相は，現在形以外にも，過去形，未来形にできる．
"I begin wear a dress."を過去形，未来形にすると次のようになる．

```SFGPL
{I_began_wear_a_dress}
{I_began_will_begin_a_dress}
```

また，原則としてこれらの相単体では，ある時点にフォーカスをした動作を表している．
特に，その時点より過去からその動作が続いている場合を強調して示すためには，それらの相に加えて完了形を使用し表現する．
進行形に完了形を加えた"I have been wearing a dress."を表すには，次のようになる．

```SFGPL
{I_have_been_wearing_a_dress}
```

### 一般的な進行形

SFGPLでは前節の①～⑤のような相を考えずに，⑥のように単純な進行形にすることができる．
SFGPLは次のように，"I am wearing the dress."という意味の進行形を表すことができる．

```SFGPL
{I_am_wearing_the_dress}
```

進行形を表す```{verb_progressive}```は動詞に付属する．
これらは，現在形以外にも，過去形，未来形にできる．
"I am wearing the dress."を過去形，未来形にすると次のようになる．

```SFGPL
{I_was_wearing_the_dress}
{I_will_be_wearing_the_dress}
```

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

## SFGPLの時間表現のまとめ

SFGPLの時間表現に関しては，次の表のようなものが存在する．

|基本時制|拡張時制|完了相|完結相|
|:-:|:-:|:-:|:-:|
|-|-|-|-|
|{phrase_past}|{determinerV_past}|{verb_perfective}|{verb_start}|
|{phrase_future}|{determinerV_present}||{verb_condition}|
||{determinerV_future}||{verb_complete}|
||||{verb_continue}|
||||{verb_end}|
||||{verb_progressive}|

このように，SFGPLでは3×4×2×7=168通りの時間表現が存在し，あらゆる場面に対して表現することが可能である．

## 受動態

SFGPLは次のように，"The dress is worn."という意味の受動態を表すことができる．

```SFGPL
{the_dress_is_worn}
```

受動態を表す```{verb_passive}```は動詞に付属する．
これらは，現在形以外にも，過去形，未来形にできる．
"The dress is worn."を過去形，未来形にすると次のようになる．

```SFGPL
{the_dress_was_worn}
{the_dress_will_be_worn}
```

## その他の動詞の修飾

[DeterminerV]({docs_DeterminerV})クラス内の関数では，その他の動詞の修飾をすることができる．
また，それらは，英語の助動詞と似ている．

## 単語集

|English|SFGPL|
|:-:|:-:|
|I|{I}|
|live|{live}|
|in Tokyo|{in_Tokyo}|
|wear|{wear}|
|dress|{dress}|
