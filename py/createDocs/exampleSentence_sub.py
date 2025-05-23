from SFGPL import *

void_func=lambda a:a

sc=SFGPLCorpus()

sentence_01_func=lambda x:Noun.eq(x,Verb.none(),Noun.haveP(Noun("worker"),Verb.none(),Modifier.N2M(DeterminerN.place(Noun("office")))))

sc.setCorpus(
    sentence_01_func(Pronoun.I()),
    "I am an office worker.",
)

sc.setCorpus(
    sentence_01_func(Pronoun.you()),
    "You are an office worker.",
)

sc.setCorpus(
    sentence_01_func(DeterminerN.male(Pronoun.he())),
    "He is an office worker.",
)

sc.setCorpus(
    sentence_01_func(DeterminerN.female(Pronoun.he())),
    "She is an office worker.",
)

sc.setCorpus(
    sentence_01_func(DeterminerN.plural(Pronoun.I())),
    "We are office workers.",
)

sc.setCorpus(
    sentence_01_func(DeterminerN.plural(Pronoun.you())),
    "You are office workers.",
)

sc.setCorpus(
    sentence_01_func(DeterminerN.plural(Pronoun.he())),
    "They are office workers.",
)

sc.setCorpus(
    Phrase.past(sentence_01_func(Pronoun.I())),
    "I was an office worker.",
)

sc.setCorpus(
    Phrase.future(sentence_01_func(Pronoun.I())),
    "I will be an office worker.",
)

sentence_02=Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school")))))))

sc.setCorpus(
    sentence_02,
    "I go to my school.",
)

sc.setCorpus(
    Phrase.past(sentence_02),
    "I went to my school.",
)

sc.setCorpus(
    Phrase.future(sentence_02),
    "I will go to my school.",
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("read"),Noun("book")),
    "I read a book.",
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb.add(Verb("send"),Modifier.N2M(DeterminerN.time(Noun("yesterday")))),DeterminerN.male(Pronoun.he()),Noun("letter"))),
    "I sent him a letter yesterday.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.I(),Verb.none(),DeterminerN.male(Pronoun.he()),Noun("teacher"))),
    "I made him a teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.I(),Verb.none(),DeterminerN.male(Pronoun.he()),Modifier("happy"))),
    "I made her happy.",
)

sc.setCorpus(
    Noun.gt(DeterminerN.male(Pronoun.he()),Verb.none(),Modifier("tall"),Pronoun.I()),
    "He is taller than me.",
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.add(Verb("put"),Modifier.N2M(DeterminerN.place(DeterminerN.on(Noun("table"))))),Noun.AND(Noun("apple"),Noun("peach")))),
    "I put an apple and a peach on the table.",
)

sentence_03=lambda ph=void_func,dv=void_func,vf=void_func:ph(Noun.do(Pronoun.I(),Verb.add(dv(vf(Verb("go"))),Modifier.N2M(DeterminerN.place(Noun("Osaka"))))))

sc.setCorpus(
    sentence_03(),
    "I go to Osaka.",
)

sc.setCorpus(
    sentence_03(ph=Phrase.past),
    "I went to Osaka.",
)

sc.setCorpus(
    sentence_03(ph=Phrase.future),
    "I will go to Osaka.",
)

sentence_04=lambda subject=Pronoun.I(),tense_base=void_func,determinerV=void_func,tableD=void_func:(tense_base(Noun.doT(subject,determinerV(Verb("create")),tableD(Noun("table")))))

sc.setCorpus(
    sentence_04(),
    "I create a table."
)

sc.setCorpus(
    sentence_04(tableD=lambda x:Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(x))),
    "I create this table."
)

sc.setCorpus(
    Phrase.NOT(sentence_04()),
    "I don't create a table."
)

sc.setCorpus(
    sentence_04(subject=Pronoun.you()),
    "You create a table."
)

sc.setCorpus(
    Phrase.interrogative(sentence_04(subject=Pronoun.you())),
    "Do you create a table?"
)

sc.setCorpus(
    Phrase.interrogative(Phrase.past(sentence_04(subject=Pronoun.you()))),
    "Did you create a table?"
)

sc.setCorpus(
    Phrase.interrogative(sentence_04(subject=DeterminerN.human(Pronoun.interrogative()))),
    "Who create the table?"
)

sc.setCorpus(
    Phrase.interrogative(Noun.doT(Pronoun.you(),Verb("create"),DeterminerN.thing(Pronoun.interrogative()))),
    "What do you create?"
)

sc.setCorpus(
    Phrase.interrogative(Noun.doT(Pronoun.you(),Verb.add(Verb("create"),Modifier.N2M(DeterminerN.time(Pronoun.interrogative()))),Noun("table"))),
    "When do you create the table?"
)

sc.setCorpus(
    Phrase.interrogative(Noun.doT(Pronoun.you(),Verb.add(Verb("create"),Modifier.N2M(DeterminerN.reason(Pronoun.interrogative()))),Noun("table"))),
    "Why do you create the table?"
)

sc.setCorpus(
    Phrase.imperative(sentence_04(subject=Pronoun.indefinite())),
    "Create a table!"
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.past),
    "I created a table."
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.future),
    "I will create a table."
)

sc.setCorpus(
    Noun.do(Noun("table"),Verb.add(Verb.passive(Verb("create")),Modifier.N2M(DeterminerN.affect(DeterminerN.near(Pronoun.I()))))),
    "The table is created by me."
)

sc.setCorpus(
    sentence_04(determinerV=Verb.progressive),
    "I am creating a table."
)

sc.setCorpus(
    sentence_04(determinerV=Verb.perfective),
    "I have created a table."
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.future,determinerV=DeterminerV.Estimation100),
    "I 100% probability will create a table."
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.future,determinerV=DeterminerV.Estimation75),
    "I 75% probability will create a table."
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.future,determinerV=DeterminerV.Estimation50),
    "I 50% probability will create a table."
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.future,determinerV=DeterminerV.Estimation25),
    "I 25% probability will create a table."
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.future,determinerV=DeterminerV.Estimation0),
    "I 0% probability will create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Frequency100),
    "I 100% frequently create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Frequency75),
    "I 75% frequently create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Frequency50),
    "I 50% frequently create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Frequency25),
    "I 25% frequently create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Frequency0),
    "I 0% frequently create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.present),
    "I create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.past),
    "I created a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.future),
    "I will create a table."
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.past,determinerV=DeterminerV.past),
    "I created a table.(Past in the past at a point in time)"
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.past,determinerV=DeterminerV.present),
    "I created a table.(Present in the past at a point in time)"
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.past,determinerV=DeterminerV.future),
    "I would create a table.(Future in the past at a point in time)"
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.past,determinerV=DeterminerV.past),
    "I will have created a table.(Past in the future at a point in time)"
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.past,determinerV=DeterminerV.present),
    "I will create a table.(Present in the future at a point in time)"
)

sc.setCorpus(
    sentence_04(tense_base=Phrase.past,determinerV=DeterminerV.future),
    "I will create a table.(Future in the future at a point in time)"
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Possible),
    "I can create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Ability),
    "I can create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Will),
    "I will create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Obligation),
    "I should create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Necessary),
    "I need to create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Duty),
    "I must create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.forced),
    "I am forced to create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.want),
    "I want to create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.dare),
    "I dare create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.allow),
    "I allow to create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.easy),
    "I am easy to create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.hard),
    "I am hard to create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.habit),
    "I habitually create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.Polite),
    "I create a table.(polite expression)"
)

sc.setCorpus(
    sentence_04(subject=DeterminerN.male(Pronoun.he()),determinerV=DeterminerV.Respect),
    "He creates a table.(respectful expression)"
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.volitional),
    "I consciously create a table."
)

sc.setCorpus(
    sentence_04(determinerV=DeterminerV.nonVolitional),
    "I unconsciously create a table."
)

sc.setCorpus(
    Phrase.interrogative(sentence_04(subject=Pronoun.you(),determinerV=DeterminerV.Requests)),
    "Can you create a table?"
)

sc.setCorpus(
    Phrase.interrogative(sentence_04(determinerV=DeterminerV.Permission)),
    "May I create a table?"
)

sc.setCorpus(
    Phrase.interrogative(sentence_04(determinerV=DeterminerV.Suggestion)),
    "Shall I create a table?"
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("get"),Noun.eq(Noun("information"),Verb.none(),Noun.doT(DeterminerN.male(Pronoun.he()),Verb.perfective(Verb("create")),Noun("table")))),
    "I get the information that he has create a table."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("get"),Noun.eq(Noun("information"),Verb.none(),Noun.doT(DeterminerN.male(Pronoun.he()),Verb.perfective(Verb("create")),Noun("table"))))),
    "I got the information that he has create a table."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("get"),Noun.eq(Noun("information"),Verb.none(),Noun.doT(DeterminerN.male(Pronoun.he()),Verb.perfective(Verb("create")),Noun.eq(DeterminerN.plural(Noun("table")),Verb.none(),NumberList.digit1(Number.three())))))),
    "I got the information that he has create three tables."
)

sc.setCorpus(
    Phrase.past(Noun.hearSay(Pronoun.I(),Verb.none(),Noun.doT(DeterminerN.male(Pronoun.he()),Verb("create"),Noun("table")),Noun("John"))),
    "According to John, I heard that he create a table."
)

sc.setCorpus(
    Phrase.past(Noun.hearSay(Pronoun.you(),Verb.none(),Noun.doT(DeterminerN.male(Pronoun.he()),Verb("create"),Noun("table")),Noun("John"))),
    "According to John, you heard that he create a table."
)

sc.setCorpus(
    Phrase.past(Phrase.NOT(Noun.doT(Pronoun.I(),Verb("know"),Phrase.past(Noun.doT(DeterminerN.human(Pronoun.indefinite()),Verb.progressive(Verb("call")),Pronoun.I()))))),
    "I didn't know that someone was calling me."
)

sc.setCorpus(
    Phrase.Because(Phrase.past(Phrase.NOT(Noun.do(Pronoun.I(),Verb.add(DeterminerV.Possible(Verb("go")),Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.distal(),Verb.none(),DeterminerN.stressed(Noun("event"))))))))),Phrase.NOT(Noun.have(Pronoun.I(),Verb.none(),Noun("car")))),
    "I could not go to that event because I do not have a car."
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.you(),Verb.add(Verb.none(),Modifier.N2M(DeterminerN.reason(Phrase.past(Noun.doT(Pronoun.you(),Verb.borrowed("eat","English"),Noun.doT(Pronoun.I(),Verb.borrowed("make","English"),DeterminerN.stressed(Noun.borrowed("cake","English")))))))),Noun("Mary"),Modifier.borrowed("sad","English"))),
    "You made Mary sad, for you ate the cake I made."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.add(Verb.borrowed("meet","English"),Modifier.N2M(DeterminerN.time(Phrase.past(Noun.doT(Pronoun.I(),Verb.borrowed("go","English"),Noun.V2N(Verb.borrowed("shop","English"))))))),Noun("Mary"))),
    "I met Mary when I went shopping."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.add(Verb.borrowed("meet","English"),Modifier.N2M(DeterminerN.time(Phrase.past(Noun.doT(Pronoun.I(),Verb.borrowed("go","English"),Noun.V2N(Verb.borrowed("shop","English"))))))),Noun("Mary"))),
    "I met Mary when I went shopping."
)

sc.setCorpus(
    Noun.do(Noun("apple"),Verb.add(WordV.exist(),Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("table")))))),
    "There is an apple on this table."
)

sc.setCorpus(
    Noun.do(DeterminerN.plural(Noun("apple")),Verb.add(WordV.exist(),Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("table")))))),
    "There are apples on this table."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb.none(),Noun.have(Pronoun.I(),Verb.none(),DeterminerN.plural(Noun("student"))),DeterminerN.plural(Noun("apple")))),
    "I gave my students apples."
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.human(Pronoun.indefinite()),Verb("eat"),Noun("apple"))),
    "Someone ate an apple."
)

sc.setCorpus(
    Noun.do(DeterminerN.female(Pronoun.he()),Verb.add(Verb("sing"),Modifier("beautifully"))),
    "She sings beautifully."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.he()),Verb.add(Verb("arrive"),Modifier("late")))),
    "They arrived late."
)

sc.setCorpus(
    Noun.do(DeterminerN.male(Pronoun.he()),Verb.add(Verb("work"),Modifier("hard"))),
    "He works hard."
)

sc.setCorpus(
    Noun.do(Noun.eq(DeterminerN.animal(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("cat"))),Verb.progressive(Verb("sleep"))),
    "The cat is sleeping."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),Noun("coffee")),
    "I like coffee."
)

sc.setCorpus(
    Noun.do(DeterminerN.female(Pronoun.he()),Verb.add(Verb("run"),Modifier("fast"))),
    "She runs fast."
)

sc.setCorpus(
    Noun.have(DeterminerN.plural(Pronoun.I()),Verb.none(),Noun("plan")),
    "We have a plan."
)

sc.setCorpus(
    Noun.doT(DeterminerN.male(Pronoun.he()),Verb("play"),Noun("guitar")),
    "He plays the guitar."
)

sc.setCorpus(
    Noun.doT(DeterminerN.female(Pronoun.he()),Verb("play"),Noun("guitar")),
    "She plays the guitar."
)

sc.setCorpus(
    Noun.do(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("phone"))),Verb.progressive(Verb("ring"))),
    "The phone is ringing."
)

sc.setCorpus(
    Noun.do(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("phone"))),Verb.progressive(Verb("ring"))),
    "My phone is ringing."
)

sc.setCorpus(
    Noun.do(Noun.eq(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("phone"))),Verb.progressive(Verb("ring"))),
    "His phone is ringing."
)

sc.setCorpus(
    Noun.do(Noun.eq(DeterminerN.female(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("phone"))),Verb.progressive(Verb("ring"))),
    "Her phone is ringing."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.progressive(Verb("watch")),Noun("movie")),
    "They are watching a movie."
)
