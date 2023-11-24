# 17. 例文

[TOP](../../readme.md)
/
[EN](../en/exampleSentence.md)

以下の表は，SFGPLの例文を示す．

|SFGPL|Python|Translation|
|:-:|:-:|:-:|
|ma ga so me fa 'worker' so li pun fa 'office'|Noun.eq( Pronoun.I(  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  ) |I am an office worker.|
|ma ge so me fa 'worker' so li pun fa 'office'|Noun.eq( Pronoun.you(  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  ) |You are an office worker.|
|ma lan gi so me fa 'worker' so li pun fa 'office'|Noun.eq( DeterminerN.male( Pronoun.he(  )  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  ) |He is an office worker.|
|ma len gi so me fa 'worker' so li pun fa 'office'|Noun.eq( DeterminerN.female( Pronoun.he(  )  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  ) |She is an office worker.|
|ma don ga so me fa 'worker' so li pun fa 'office'|Noun.eq( DeterminerN.plural( Pronoun.I(  )  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  ) |We are an office worker.|
|ma don ge so me fa 'worker' so li pun fa 'office'|Noun.eq( DeterminerN.plural( Pronoun.you(  )  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  ) |You are an office worker.|
|ma don gi so me fa 'worker' so li pun fa 'office'|Noun.eq( DeterminerN.plural( Pronoun.he(  )  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  ) |They are an office worker.|
|di ma ga so me fa 'worker' so li pun fa 'office'|Phrase.past( Noun.eq( Pronoun.I(  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  )  ) |I was an office worker.|
|du ma ga so me fa 'worker' so li pun fa 'office'|Phrase.future( Noun.eq( Pronoun.I(  ) , Verb.none(  ) , Noun.haveP( Noun( "'worker'" ) , Verb.none(  ) , Modifier.N2M( DeterminerN.place( Noun( "'office'" )  )  )  )  )  ) |I will be an office worker.|
|ta ga na sa 'go' li pun mu ga so san fa 'school'|Noun.do( Pronoun.I(  ) , Verb.add( Verb( "'go'" ) , Modifier.N2M( DeterminerN.place( Noun.belong( Pronoun.I(  ) , Verb.none(  ) , DeterminerN.stressed( Noun( "'school'" )  )  )  )  )  )  ) |I go to my school.|
|di ta ga na sa 'go' li pun mu ga so san fa 'school'|Phrase.past( Noun.do( Pronoun.I(  ) , Verb.add( Verb( "'go'" ) , Modifier.N2M( DeterminerN.place( Noun.belong( Pronoun.I(  ) , Verb.none(  ) , DeterminerN.stressed( Noun( "'school'" )  )  )  )  )  )  )  ) |I went to my school.|
|du ta ga na sa 'go' li pun mu ga so san fa 'school'|Phrase.future( Noun.do( Pronoun.I(  ) , Verb.add( Verb( "'go'" ) , Modifier.N2M( DeterminerN.place( Noun.belong( Pronoun.I(  ) , Verb.none(  ) , DeterminerN.stressed( Noun( "'school'" )  )  )  )  )  )  )  ) |I will go to my school.|
|te ga sa 'read' fa 'book'|Noun.doT( Pronoun.I(  ) , Verb( "'read'" ) , Noun( "'book'" )  ) |I read a book.|
|di ti ga na sa 'send' li pin fa 'yesterday' lan gi fa 'letter'|Phrase.past( Noun.give( Pronoun.I(  ) , Verb.add( Verb( "'send'" ) , Modifier.N2M( DeterminerN.time( Noun( "'yesterday'" )  )  )  ) , DeterminerN.male( Pronoun.he(  )  ) , Noun( "'letter'" )  )  ) |I sent him a letter yesterday.|
|di tu ga so lan gi fa 'teacher'|Phrase.past( Noun.makeN( Pronoun.I(  ) , Verb.none(  ) , DeterminerN.male( Pronoun.he(  )  ) , Noun( "'teacher'" )  )  ) |I made him a teacher.|
|di to ga so lan gi la 'happy'|Phrase.past( Noun.makeM( Pronoun.I(  ) , Verb.none(  ) , DeterminerN.male( Pronoun.he(  )  ) , Modifier( "'happy'" )  )  ) |I made her happy.|
|mo lan gi so la 'tall' ga|Noun.gt( DeterminerN.male( Pronoun.he(  )  ) , Verb.none(  ) , Modifier( "'tall'" ) , Pronoun.I(  )  ) |He is taller than me.|
|di te ga na sa 'put' li pun min fa 'table' ba fa 'apple' fa 'peach'|Phrase.past( Noun.doT( Pronoun.I(  ) , Verb.add( Verb( "'put'" ) , Modifier.N2M( DeterminerN.place( DeterminerN.on( Noun( "'table'" )  )  )  )  ) , LangObj.AND( Noun( "'apple'" ) , Noun( "'peach'" )  )  )  ) |I put an apple and a peach on the table.|
|ta ga na sa 'go' li pun fa 'Osaka'|Noun.do( Pronoun.I(  ) , Verb.add( Verb( "'go'" ) , Modifier.N2M( DeterminerN.place( Noun( "'Osaka'" )  )  )  )  ) |I go to Osaka.|
|di ta ga na sa 'go' li pun fa 'Osaka'|Phrase.past( Noun.do( Pronoun.I(  ) , Verb.add( Verb( "'go'" ) , Modifier.N2M( DeterminerN.place( Noun( "'Osaka'" )  )  )  )  )  ) |I went to Osaka.|
|du ta ga na sa 'go' li pun fa 'Osaka'|Phrase.future( Noun.do( Pronoun.I(  ) , Verb.add( Verb( "'go'" ) , Modifier.N2M( DeterminerN.place( Noun( "'Osaka'" )  )  )  )  )  ) |I will go to Osaka.|
|te ga sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , Verb( "'create'" ) , Noun( "'table'" )  ) |I create a table.|
|te ga sa 'create' ma gu so san fa 'table'|Noun.doT( Pronoun.I(  ) , Verb( "'create'" ) , Noun.eq( Pronoun.proximal(  ) , Verb.none(  ) , DeterminerN.stressed( Noun( "'table'" )  )  )  ) |I create this table.|
|pa te ga sa 'create' fa 'table'|LangObj.NOT( Noun.doT( Pronoun.I(  ) , Verb( "'create'" ) , Noun( "'table'" )  )  ) |I don't create a table.|
|te ge sa 'create' fa 'table'|Noun.doT( Pronoun.you(  ) , Verb( "'create'" ) , Noun( "'table'" )  ) |You create a table.|
|da te ge sa 'create' fa 'table'|Phrase.interrogative( Noun.doT( Pronoun.you(  ) , Verb( "'create'" ) , Noun( "'table'" )  )  ) |Do you create a table?|
|da di te ge sa 'create' fa 'table'|Phrase.interrogative( Phrase.past( Noun.doT( Pronoun.you(  ) , Verb( "'create'" ) , Noun( "'table'" )  )  )  ) |Did you create a table?|
|da te ben wa sa 'create' fa 'table'|Phrase.interrogative( Noun.doT( DeterminerN.human( Pronoun.interrogative(  )  ) , Verb( "'create'" ) , Noun( "'table'" )  )  ) |Who create the table?|
|da te ge sa 'create' pen wa|Phrase.interrogative( Noun.doT( Pronoun.you(  ) , Verb( "'create'" ) , DeterminerN.thing( Pronoun.interrogative(  )  )  )  ) |What do you create?|
|da te ge na sa 'create' li pin wa fa 'table'|Phrase.interrogative( Noun.doT( Pronoun.you(  ) , Verb.add( Verb( "'create'" ) , Modifier.N2M( DeterminerN.time( Pronoun.interrogative(  )  )  )  ) , Noun( "'table'" )  )  ) |When do you create the table?|
|da te ge na sa 'create' li pon wa fa 'table'|Phrase.interrogative( Noun.doT( Pronoun.you(  ) , Verb.add( Verb( "'create'" ) , Modifier.N2M( DeterminerN.reason( Pronoun.interrogative(  )  )  )  ) , Noun( "'table'" )  )  ) |Why do you create the table?|
|de te we sa 'create' fa 'table'|Phrase.imperative( Noun.doT( Pronoun.indefinite(  ) , Verb( "'create'" ) , Noun( "'table'" )  )  ) |Create a table!|
|di te ga sa 'create' fa 'table'|Phrase.past( Noun.doT( Pronoun.I(  ) , Verb( "'create'" ) , Noun( "'table'" )  )  ) |I created a table.|
|du te ga sa 'create' fa 'table'|Phrase.future( Noun.doT( Pronoun.I(  ) , Verb( "'create'" ) , Noun( "'table'" )  )  ) |I will create a table.|
|ta fa 'table' na ne sa 'create' li tan tin ga|Noun.do( Noun( "'table'" ) , Verb.add( Verb.passive( Verb( "'create'" )  ) , Modifier.N2M( DeterminerN.affect( DeterminerN.near( Pronoun.I(  )  )  )  )  )  ) |The table is created by me.|
|te ga ni sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , Verb.progressive( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I am creating a table.|
|te ga nu sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , Verb.perfective( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I have created a table.|
|du te ga pak sa 'create' fa 'table'|Phrase.future( Noun.doT( Pronoun.I(  ) , DeterminerV.Estimation100( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I 100% probability will create a table.|
|du te ga pek sa 'create' fa 'table'|Phrase.future( Noun.doT( Pronoun.I(  ) , DeterminerV.Estimation75( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I 75% probability will create a table.|
|du te ga pik sa 'create' fa 'table'|Phrase.future( Noun.doT( Pronoun.I(  ) , DeterminerV.Estimation50( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I 50% probability will create a table.|
|du te ga puk sa 'create' fa 'table'|Phrase.future( Noun.doT( Pronoun.I(  ) , DeterminerV.Estimation25( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I 25% probability will create a table.|
|du te ga pok sa 'create' fa 'table'|Phrase.future( Noun.doT( Pronoun.I(  ) , DeterminerV.Estimation0( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I 0% probability will create a table.|
|te ga fak sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Frequency100( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I 100% frequently create a table.|
|te ga fek sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Frequency75( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I 75% frequently create a table.|
|te ga fik sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Frequency50( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I 50% frequently create a table.|
|te ga fuk sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Frequency25( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I 25% frequently create a table.|
|te ga fok sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Frequency0( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I 0% frequently create a table.|
|te ga bik sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.present( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I create a table.|
|te ga bak sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.past( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I created a table.|
|te ga bok sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.future( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I will create a table.|
|di te ga bak sa 'create' fa 'table'|Phrase.past( Noun.doT( Pronoun.I(  ) , DeterminerV.past( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I created a table.(Past in the past at a point in time)|
|di te ga bik sa 'create' fa 'table'|Phrase.past( Noun.doT( Pronoun.I(  ) , DeterminerV.present( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I created a table.(Present in the past at a point in time)|
|di te ga bok sa 'create' fa 'table'|Phrase.past( Noun.doT( Pronoun.I(  ) , DeterminerV.future( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I would create a table.(Future in the past at a point in time)|
|di te ga bak sa 'create' fa 'table'|Phrase.past( Noun.doT( Pronoun.I(  ) , DeterminerV.past( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I will have created a table.(Past in the future at a point in time)|
|di te ga bik sa 'create' fa 'table'|Phrase.past( Noun.doT( Pronoun.I(  ) , DeterminerV.present( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I will create a table.(Present in the future at a point in time)|
|di te ga bok sa 'create' fa 'table'|Phrase.past( Noun.doT( Pronoun.I(  ) , DeterminerV.future( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |I will create a table.(Future in the future at a point in time)|
|te ga nak sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Possible( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I can create a table.|
|te ga nek sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Ability( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I can create a table.|
|te ga nik sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Will( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I will create a table.|
|te ga nuk sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Obligation( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I should create a table.|
|te ga nok sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Necessary( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I need to create a table.|
|te ga lak sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Duty( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I must create a table.|
|te ga lek sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.forced( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I am forced to create a table.|
|te ga lik sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.want( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I want to create a table.|
|te ga luk sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.dare( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I dare create a table.|
|te ga lok sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.allow( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I allow to create a table.|
|te ga kak sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.easy( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I am easy to create a table.|
|te ga kek sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.hard( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I am hard to create a table.|
|te ga kik sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.habit( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I habitually create a table.|
|te ga kuk sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.Polite( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I create a table.(polite expression)|
|te lan gi kok sa 'create' fa 'table'|Noun.doT( DeterminerN.male( Pronoun.he(  )  ) , DeterminerV.Respect( Verb( "'create'" )  ) , Noun( "'table'" )  ) |He creates a table.(respectful expression)|
|te ga gak sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.volitional( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I consciously create a table.|
|te ga gek sa 'create' fa 'table'|Noun.doT( Pronoun.I(  ) , DeterminerV.nonVolitional( Verb( "'create'" )  ) , Noun( "'table'" )  ) |I unconsciously create a table.|
|da te ge gik sa 'create' fa 'table'|Phrase.interrogative( Noun.doT( Pronoun.you(  ) , DeterminerV.Requests( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |Can you create a table?|
|da te ga guk sa 'create' fa 'table'|Phrase.interrogative( Noun.doT( Pronoun.I(  ) , DeterminerV.Permission( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |May I create a table?|
|da te ga gok sa 'create' fa 'table'|Phrase.interrogative( Noun.doT( Pronoun.I(  ) , DeterminerV.Suggestion( Verb( "'create'" )  ) , Noun( "'table'" )  )  ) |Shall I create a table?|

