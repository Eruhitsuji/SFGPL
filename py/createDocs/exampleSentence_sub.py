from SFGPL import *

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
    "We are an office worker.",
)

sc.setCorpus(
    sentence_01_func(DeterminerN.plural(Pronoun.you())),
    "You are an office worker.",
)

sc.setCorpus(
    sentence_01_func(DeterminerN.plural(Pronoun.he())),
    "They are an office worker.",
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

