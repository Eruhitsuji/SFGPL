import sys
sys.path.append("")

from SFGPL import *
import os
from datetime import datetime,timezone

OUT_DIR="out/"

void_func=lambda a:a

os.makedirs(OUT_DIR,exist_ok=True)

sc=SFGPLCorpus()

sc.setCorpus(
    Noun.eq(Pronoun.I(),Verb.none(),Noun("student")),
    "I am a student.",
)

sc.setCorpus(
    Noun.eq(Pronoun.you(),Verb.none(),Noun("student")),
    "You are a student.",
)

sc.setCorpus(
    Noun.eq(DeterminerN.male(Pronoun.he()),Verb.none(),Noun("student")),
    "He is a student.",
)

sc.setCorpus(
    Noun.eq(DeterminerN.female(Pronoun.he()),Verb.none(),Noun("student")),
    "She is a student.",
)

sc.setCorpus(
    Noun.eq(DeterminerN.plural(Pronoun.I()),Verb.none(),DeterminerN.plural(Noun("student"))),
    "We are students.",
)

sc.setCorpus(
    Noun.eq(DeterminerN.plural(Pronoun.you()),Verb.none(),DeterminerN.plural(Noun("student"))),
    "You are students.",
)

sc.setCorpus(
    Noun.eq(DeterminerN.plural(DeterminerN.male(Pronoun.he())),Verb.none(),DeterminerN.plural(Noun("student"))),
    "They are students.",
)

sc.setCorpus(
    Noun.eq(DeterminerN.plural(DeterminerN.female(Pronoun.he())),Verb.none(),DeterminerN.plural(Noun("student"))),
    "They are students.",
)

sc.setCorpus(
    Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),Noun.AND(Noun("pen"),Noun("notebook"))),
    "I have a pen and a notebook.",
)

sc.setCorpus(
    Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),Noun.OR(Noun("pen"),Noun("notebook"))),
    "I have a pen or a notebook.",
)

sc.setCorpus(
    Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),Noun.NAND(Noun("pen"),Noun("notebook"))),
    "I have a pen nand a notebook.",
)

sc.setCorpus(
    Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),Noun.NOR(Noun("pen"),Noun("notebook"))),
    "I have a pen nor a notebook.",
)

sub_sentence_01=Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),Noun("pen"))

sc.setCorpus(
    sub_sentence_01,
    "He has a pen.",
)

sc.setCorpus(
    Phrase.NOT(sub_sentence_01),
    "He doesn't a pen.",
)

sc.setCorpus(
    Phrase.past(sub_sentence_01),
    "He had a pen.",
)

sc.setCorpus(
    Phrase.NOT(Phrase.past(sub_sentence_01)),
    "He did't a pen.",
)

sc.setCorpus(
    Phrase.future(sub_sentence_01),
    "He will have a pen.",
)

sc.setCorpus(
    Phrase.NOT(Phrase.future(sub_sentence_01)),
    "He will not have a pen.",
)

sub_sentence_02=Noun.give(Pronoun.you(),Verb("tell"),Pronoun.I(),DeterminerN.thing(Pronoun.he()))

sc.setCorpus(
    sub_sentence_02,
    "You tell me it.",
)

sc.setCorpus(
    Phrase.NOT(sub_sentence_02),
    "You don't tell me it.",
)

sc.setCorpus(
    Phrase.past(sub_sentence_02),
    "You told me it.",
)

sc.setCorpus(
    Phrase.NOT(Phrase.past(sub_sentence_02)),
    "You didn't tell me it.",
)

sc.setCorpus(
    Phrase.future(sub_sentence_02),
    "You will tell me it.",
)

sc.setCorpus(
    Phrase.NOT(Phrase.future(sub_sentence_02)),
    "You will not tell me it.",
)

sub_sentence_03=Noun.doT(DeterminerN.male(Pronoun.he()),Verb("write"),Noun("book"))

sc.setCorpus(
    sub_sentence_03,
    "He writes a book.",
)

sc.setCorpus(
    Phrase.NOT(sub_sentence_03),
    "He don't write a book.",
)

sc.setCorpus(
    Phrase.past(sub_sentence_03),
    "He wrote a book.",
)

sc.setCorpus(
    Phrase.NOT(Phrase.past(sub_sentence_03)),
    "He didn't write a book.",
)

sc.setCorpus(
    Phrase.future(sub_sentence_03),
    "He will write a book.",
)

sc.setCorpus(
    Phrase.NOT(Phrase.future(sub_sentence_03)),
    "He will not write a book.",
)

sc.setCorpus(
    Phrase.Because(sub_sentence_01,sub_sentence_03),
    "He has a pen, because he writes a book.",
)

sc.setCorpus(
    Phrase.So(sub_sentence_01,sub_sentence_03),
    "He has a pen, so he writes a book.",
)

sc.setCorpus(
    Phrase.But(sub_sentence_01,Phrase.NOT(sub_sentence_03)),
    "He has a pen, but he don't write a book.",
)

sc.setCorpus(
    Phrase.AND(sub_sentence_01,sub_sentence_03),
    "He has a pen, and he writes a book.",
)

sc.setCorpus(
    Phrase.OR(sub_sentence_01,sub_sentence_03),
    "He has a pen, or he writes a book.",
)

sc.setCorpus(
    Phrase.NAND(sub_sentence_01,sub_sentence_03),
    "He has a pen, nand he writes a book.",
)

sc.setCorpus(
    Phrase.NOR(sub_sentence_01,sub_sentence_03),
    "He has a pen, nor he writes a book.",
)

sc.setCorpus(
    Phrase.IF(sub_sentence_01,sub_sentence_02),
    "If he has a pen, you tell me it.",
)

sub_sentence_04=Noun.give(Pronoun.you(),Verb("tell"),DeterminerN.male(Pronoun.he()),Phrase.imperative(Noun.doT(DeterminerN.male(Pronoun.he()),Verb("buy"),Noun("pen"))))

sc.setCorpus(
    sub_sentence_04,
    "You tell him buy a pen.",
)

sc.setCorpus(
    Phrase.IFELSE(sub_sentence_01,sub_sentence_02,Phrase.imperative(sub_sentence_04)),
    "If he has a pen, you tell me it, else tell him to buy a pen.",
)

sc.setCorpus(
    Noun.eq(Pronoun.I(),Verb.none(),Noun.belong(Noun("employee"),Verb.none(),Noun("company"))),
    "I am a company employee.",
)

sc.setCorpus(
    Noun.eq(Pronoun.you(),Verb.none(),Noun.belong(Noun("employee"),Verb.none(),Noun("company"))),
    "You are a company employee.",
)

sc.setCorpus(
    Noun.haveP(Pronoun.I(),Verb.none(),Modifier("sad")),
    "I am sad.",
)

sc.setCorpus(
    Noun.haveP(Pronoun.you(),Verb("seem"),Modifier("sad")),
    "you seem sad.",
)

red_table=Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("table"))),Verb.none(),Modifier("red"))
blue_table=Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("table"))),Verb.none(),Modifier("blue"))

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),red_table),
    "I have this table is red.",
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),blue_table),
    "I have this table is blue.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I go to my school.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.you(),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I go to your school.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I go to him school.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.female(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I go to her school.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.plural(Pronoun.I()),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I go to our school.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.plural(Pronoun.you()),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I go to your school.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.plural(DeterminerN.male(Pronoun.he())),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I go to their school.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.plural(DeterminerN.female(Pronoun.he())),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I go to their school.",
)

sc.setCorpus(
    Noun.gt(red_table,Verb.none(),WordM.big(),blue_table),
    "This red table is bigger than this blue table.",
)

sc.setCorpus(
    Noun.gt(blue_table,Verb.none(),Modifier.Neg(WordM.big()),red_table),
    "This blue table is smaller than this red table.",
)

sc.setCorpus(
    Noun.doT(Pronoun.you(),Verb("like"),Noun.V2N(Verb("talk"))),
    "You like talking.",
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.you(),Verb("measure"),Noun.M2N(WordM.big()))),
    "I measured a size.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.you(),Verb.none(),Pronoun.I(),Noun("teacher"))),
    "You made me teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.I(),Verb.none(),Pronoun.you(),Noun("teacher"))),
    "I made you teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.I(),Verb.none(),DeterminerN.male(Pronoun.he()),Noun("teacher"))),
    "I made him teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.I(),Verb.none(),DeterminerN.female(Pronoun.he()),Noun("teacher"))),
    "I made her teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.you(),Verb.none(),DeterminerN.plural(Pronoun.I()),Noun("teacher"))),
    "You made us teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.I(),Verb.none(),DeterminerN.plural(Pronoun.you()),Noun("teacher"))),
    "I made you teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.I(),Verb.none(),DeterminerN.plural(DeterminerN.male(Pronoun.he())),Noun("teacher"))),
    "I made them teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeN(Pronoun.I(),Verb.none(),DeterminerN.plural(DeterminerN.female(Pronoun.he())),Noun("teacher"))),
    "I made them teacher.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.you(),Verb.none(),Pronoun.I(),Modifier("happy"))),
    "You made me happy.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.I(),Verb.none(),Pronoun.you(),Modifier("happy"))),
    "I made you happy.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.I(),Verb.none(),DeterminerN.male(Pronoun.he()),Modifier("happy"))),
    "I made him happy.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.I(),Verb.none(),DeterminerN.female(Pronoun.he()),Modifier("happy"))),
    "I made her happy.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.you(),Verb.none(),DeterminerN.plural(Pronoun.I()),Modifier("happy"))),
    "You made us happy.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.I(),Verb.none(),DeterminerN.plural(Pronoun.you()),Modifier("happy"))),
    "I made you happy.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.I(),Verb.none(),DeterminerN.plural(DeterminerN.male(Pronoun.he())),Modifier("happy"))),
    "I made them happy.",
)

sc.setCorpus(
    Phrase.past(Noun.makeM(Pronoun.I(),Verb.none(),DeterminerN.plural(DeterminerN.female(Pronoun.he())),Modifier("happy"))),
    "I made them happy.",
)

sc.setCorpus(
    Noun.eq(Pronoun.I(),Verb.none(),DeterminerN.male(Noun.none())),
    "I am male",
)

sc.setCorpus(
    Noun.eq(Pronoun.you(),Verb.none(),DeterminerN.female(Noun.none())),
    "You are female",
)

sc.setCorpus(
    Phrase.past(Noun.do(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("book"))),Verb.add(Verb.passive(Verb("write")),Modifier.N2M(DeterminerN.affect(DeterminerN.near(Pronoun.I())))))),
    "This book was written by me.",
)

sc.setCorpus(
    Phrase.past(Noun.do(Noun.eq(Pronoun.distal(),Verb.none(),DeterminerN.stressed(Noun("book"))),Verb.add(Verb.passive(Verb("write")),Modifier.N2M(DeterminerN.affect(DeterminerN.near(Pronoun.I())))))),
    "That book was written by me.",
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.progressive(Verb("write")),Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("book"))))),
    "I was writing this book.",
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.progressive(Verb("write")),Noun.eq(Pronoun.distal(),Verb.none(),DeterminerN.stressed(Noun("book"))))),
    "I was writing that book.",
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb.perfective(WordV.exist()),Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.you(),Verb.none(),DeterminerN.stressed(Noun("school"))))))),
    "I had been to your school.",
)

sc.setCorpus(
    Noun.do(DeterminerN.all(Noun("apple")),Verb.M2V(Modifier("red"))),
    "All apples turn red.",
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.I()),Verb.add(Verb.N2V(Noun("zoom")),Modifier.AND(Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.plural(Pronoun.I()),Verb.none(),Noun("company")))),Modifier("recently"))),DeterminerN.some(DeterminerN.plural(Noun("meeting")))),
    "We zoom some meetings at our company recently."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("apple"))),Verb.none(),Modifier.add(Modifier("red"),Modifier("green"))),
    "This apple is red green.",
)

sc.setCorpus(
    Noun.haveP(Noun.have(Pronoun.you(),Verb.none(),DeterminerN.stressed(Noun("plan"))),Verb.none(),Modifier.add(Modifier.V2M(Verb.progressive(Verb("interest"))),Modifier.N2M(DeterminerN.affect(Noun.have(DeterminerN.plural(Pronoun.I()),Verb.none(),DeterminerN.stressed(Noun("project"))))))),
    "Your plan is interesting for our project."
)

sc.setCorpus(
    Noun.haveP(Pronoun.proximal(),Verb.none(),Modifier.none()),
    "This is big."
)

sc.setCorpus(
    Noun.haveP(Pronoun.proximal(),Verb.none(),Modifier.Neg(Modifier.none())),
    "This is small."
)

sc.setCorpus(
    Noun.doT(DeterminerN.male(Pronoun.he()),Verb("buy"),Noun("book")),
    "He buy a book."
)

sc.setCorpus(
    Phrase.interrogative(Phrase.past(Noun.doT(DeterminerN.human(Pronoun.interrogative()),Verb("buy"),Noun("book")))),
    "Who did buy a book?"
)

sc.setCorpus(
    Phrase.interrogative(Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb("buy"),Pronoun.interrogative()))),
    "What did he buy?"
)

sc.setCorpus(
    Phrase.interrogative(Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.add(Verb("buy"),Modifier.N2M(DeterminerN.time(Pronoun.interrogative()))),Noun("book")))),
    "When did he buy a book?"
)

sc.setCorpus(
    Phrase.interrogative(Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.add(Verb("buy"),Modifier.N2M(DeterminerN.place(Pronoun.interrogative()))),Noun("book")))),
    "Where did he buy a book?"
)

sc.setCorpus(
    Phrase.interrogative(Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.add(Verb("buy"),Modifier.N2M(DeterminerN.reason(Pronoun.interrogative()))),Noun("book")))),
    "Why did he buy a book?"
)

sc.setCorpus(
    Phrase.interrogative(Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.add(Verb("buy"),Modifier.N2M(DeterminerN.method(Pronoun.interrogative()))),Noun("book")))),
    "How did he buy a book?"
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),WordV.destroy(),Noun("door"))),
    "He broke a door."
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.biology(Pronoun.interrogative()),WordV.destroy(),Noun("door"))),
    "Who broke a door?"
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.human(Pronoun.interrogative()),WordV.destroy(),Noun("door"))),
    "Who broke a door?"
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.animal(Pronoun.interrogative()),WordV.destroy(),Noun("door"))),
    "Who broke a door?"
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.plant(Pronoun.interrogative()),WordV.destroy(),Noun("door"))),
    "Who broke a door?"
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.human(Pronoun.interrogative()),WordV.destroy(),Noun("door"))),
    "Who broke a door?"
)

sc.setCorpus(
    Noun.do(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("door")),Verb.add(Verb.passive(WordV.create()),Modifier.N2M(DeterminerN.material(Noun("wood"))))),
    "This door is made of wood."
)

sc.setCorpus(
    Phrase.interrogative(Noun.do(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("door")),Verb.add(Verb.passive(WordV.create()),Modifier.N2M(DeterminerN.material(Pronoun.interrogative()))))),
    "What is this door made of?"
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.start(DeterminerN.place(Noun("Osaka")))),Modifier.N2M(DeterminerN.end(DeterminerN.place(Noun("Tokyo")))))))),
    "I went to Tokyo from Osaka."
)

buy_peach_sentence=Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.doT(Pronoun.I(),Verb("buy"),Noun("peach"))))))
sc.setCorpus(
    buy_peach_sentence,
    "I go to buy peaches."
)

go_out_sentence=Noun.do(Pronoun.you(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.Out(Noun.none()))))
sc.setCorpus(
    go_out_sentence,
    "You go out."
)

stay_home_sentence=Noun.do(Pronoun.I(),Verb.add(Verb("stay"),Modifier.N2M(DeterminerN.place((Noun("home"))))))
sc.setCorpus(
    stay_home_sentence,
    "I stay at home."
)

sc.setCorpus(
    Phrase.NOT(buy_peach_sentence),
    "I don't go to buy peaches."
)

sc.setCorpus(
    Phrase.Because(buy_peach_sentence,go_out_sentence),
    "I go to buy peaches, because you go out."
)

sc.setCorpus(
    Phrase.IF(go_out_sentence,buy_peach_sentence),
    "If you go out, I go to buy peaches."
)

sc.setCorpus(
    Phrase.IFELSE(go_out_sentence,buy_peach_sentence,stay_home_sentence),
    "If you go out, I go to buy peaches, otherwise I stay at home."
)

sc.setCorpus(
    Phrase.So(buy_peach_sentence,go_out_sentence),
    "I go to buy peaches, so you go out."
)

sc.setCorpus(
    Phrase.But(buy_peach_sentence,go_out_sentence),
    "I go to buy peaches, but you go out."
)

sc.setCorpus(
    Phrase.AND(buy_peach_sentence,go_out_sentence),
    "I go to buy peaches, and you go out."
)

sc.setCorpus(
    Phrase.OR(buy_peach_sentence,go_out_sentence),
    "I go to buy peaches, or you go out."
)

sc.setCorpus(
    Phrase.NAND(buy_peach_sentence,go_out_sentence),
    "I go to buy peaches, nand you go out."
)

sc.setCorpus(
    Phrase.NOR(buy_peach_sentence,go_out_sentence),
    "I go to buy peaches, nor you go out."
)

sc.setCorpus(
    Phrase.future(Noun.do(Pronoun.I(),Verb.add(Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.doT(Pronoun.I(),Verb("buy"),Noun("peach"))))),Modifier.N2M(DeterminerN.section(go_out_sentence))))),
    "I will go to buy peaches, while you go out."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.add(Verb("research"),Modifier.N2M(DeterminerN.method(Noun("the_internet")))),Noun("Python"))),
    "I researched Python on the internet."
)

sc.setCorpus(
    Phrase.past(Phrase.future(Noun.doT(Pronoun.I(),Verb.add(Verb("research"),Modifier.N2M(DeterminerN.method(Noun("the_internet")))),Noun("Python")))),
    "I researched Python on the internet."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.add(Verb.add(Verb("research"),Modifier("can")),Modifier.N2M(DeterminerN.method(Noun("the_internet")))),Noun("Python"))),
    "I could research Python on the internet."
)

sc.setCorpus(
    Phrase.past(Noun.eq(Pronoun.I(),Verb("become"),DeterminerN.human(Noun.V2N((Verb("teach")))))),
    "I became a teacher."
)

sc.setCorpus(
    Phrase.past(Noun.eq(Pronoun.you(),Verb("become"),DeterminerN.human(Noun.V2N((Verb("teach")))))),
    "You became a teacher."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.place(Noun("Tokyo"))),Modifier.N2M(DeterminerN.affected(DeterminerN.near(Pronoun.you())))))),
    "I go to Tokyo with you."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("study"),DeterminerN.affect(DeterminerN.near(Noun.eq(Noun("computer"),Verb.none(),Noun("science"))))),
    "I study about computer science."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun("box")))),
    "The ball is in a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.Out(Noun("box")))),
    "The ball is out a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.above(Noun("box")))),
    "The ball is above a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.on(DeterminerN.above(Noun("box"))))),
    "The ball is on a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.below(Noun("box")))),
    "The ball is below a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.on(DeterminerN.below(Noun("box"))))),
    "The ball is on a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.right(Noun("box")))),
    "The ball is right a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.on(DeterminerN.right(Noun("box"))))),
    "The ball is on a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.left(Noun("box")))),
    "The ball is left a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.on(DeterminerN.left(Noun("box"))))),
    "The ball is on a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.front(Noun("box")))),
    "The ball is a front of a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.behind(Noun("box")))),
    "The ball is behind a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.move(Noun("box")))),
    "The ball crosses a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.move(DeterminerN.In(Noun("box"))))),
    "The ball is into a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.stop(DeterminerN.on(Noun("box"))))),
    "The ball is on a box."
)

sc.setCorpus(
    Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.stop(DeterminerN.In(Noun("box"))))),
    "The ball is in a box."
)

sc.setCorpus(
    Noun.haveP(DeterminerN.all(DeterminerN.plural(Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.stop(DeterminerN.In(Noun("box"))))))),Verb.none(),Modifier("red")),
    "All balls are in a box is red."
)

sc.setCorpus(
    Noun.haveP(DeterminerN.many(DeterminerN.plural(Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.stop(DeterminerN.In(Noun("box"))))))),Verb.none(),Modifier("red")),
    "Many balls are in a box is red."
)

sc.setCorpus(
    Noun.haveP(DeterminerN.some(DeterminerN.plural(Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.stop(DeterminerN.In(Noun("box"))))))),Verb.none(),Modifier("red")),
    "Some balls are in a box is red."
)

sc.setCorpus(
    Noun.haveP(DeterminerN.one(Noun.haveP(Noun("ball"),Verb.none(),Modifier.N2M(DeterminerN.stop(DeterminerN.In(Noun("box")))))),Verb.none(),Modifier("red")),
    "One ball is in a box is red."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.front(Noun("box")))))),
    "I moved a front of a box."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.behind(Noun("box")))))),
    "I moved behind a box."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.I()),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.behind(Noun("box")))))),
    "We moved behind a box."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.you(),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.behind(Noun("box")))))),
    "You moved behind a box."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.you()),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.behind(Noun("box")))))),
    "You moved behind a box."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.male(Pronoun.he()),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.behind(Noun("box")))))),
    "He moved behind a box."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.female(Pronoun.he()),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.behind(Noun("box")))))),
    "She moved behind a box."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.thing(Pronoun.he()),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.behind(Noun("box")))))),
    "It moved behind a box."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.he()),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.behind(Noun("box")))))),
    "They moved behind a box."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("put"),Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("ball"))))),
    "I put my ball."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("put"),Noun.have(DeterminerN.plural(Pronoun.I()),Verb.none(),DeterminerN.stressed(Noun("ball"))))),
    "I put our ball."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("put"),Noun.have(Pronoun.you(),Verb.none(),DeterminerN.stressed(Noun("ball"))))),
    "I put your ball."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("put"),Noun.have(DeterminerN.plural(Pronoun.you()),Verb.none(),DeterminerN.stressed(Noun("ball"))))),
    "I put your ball."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("put"),Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("ball"))))),
    "I put his ball."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("put"),Noun.have(DeterminerN.female(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("ball"))))),
    "I put her ball."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("put"),Noun.have(DeterminerN.thing(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("ball"))))),
    "I put its ball."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("put"),Noun.have(DeterminerN.plural(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("ball"))))),
    "I put their ball."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.you(),Verb.none(),Pronoun.I(),Pronoun.proximal())),
    "You gave me this."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.you(),Verb.none(),DeterminerN.plural(Pronoun.I()),DeterminerN.plural(Pronoun.proximal()))),
    "You gave us these."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb.none(),Pronoun.you(),Pronoun.proximal())),
    "I gave you this."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb.none(),DeterminerN.plural(Pronoun.you()),DeterminerN.plural(Pronoun.proximal()))),
    "I gave you these."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb.none(),DeterminerN.male(Pronoun.you()),Pronoun.proximal())),
    "I gave him this."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb.none(),DeterminerN.female(Pronoun.you()),Pronoun.proximal())),
    "I gave her this."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb.none(),DeterminerN.thing(Pronoun.you()),Pronoun.proximal())),
    "I gave it this."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb.none(),DeterminerN.plural(Pronoun.you()),DeterminerN.plural(Pronoun.proximal()))),
    "I gave them these."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("pen")),Verb.none(),DeterminerN.possessive(Pronoun.I())),
    "This pen is mine."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("pen")),Verb.none(),DeterminerN.possessive(DeterminerN.plural(Pronoun.I()))),
    "This pen is ours."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("pen")),Verb.none(),DeterminerN.possessive(Pronoun.you())),
    "This pen is yours."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("pen")),Verb.none(),DeterminerN.possessive(DeterminerN.plural(Pronoun.you()))),
    "This pen is yours."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("pen")),Verb.none(),DeterminerN.possessive(DeterminerN.male(Pronoun.he()))),
    "This pen is his."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("pen")),Verb.none(),DeterminerN.possessive(DeterminerN.female(Pronoun.he()))),
    "This pen is hers."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("pen")),Verb.none(),DeterminerN.possessive(DeterminerN.thing(Pronoun.he()))),
    "This pen is its."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("pen")),Verb.none(),DeterminerN.possessive(DeterminerN.plural(Pronoun.he()))),
    "This pen is theirs."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.reflexive(Pronoun.I())),
    "I like myself."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.I()),Verb("like"),DeterminerN.reflexive(DeterminerN.plural(Pronoun.I()))),
    "We like ourselves."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.reflexive(Pronoun.you())),
    "You like yourself."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.I()),Verb("like"),DeterminerN.reflexive(DeterminerN.plural(Pronoun.you()))),
    "You like yourselves."
)

sc.setCorpus(
    Noun.doT(DeterminerN.male(Pronoun.he()),Verb("like"),DeterminerN.reflexive(DeterminerN.male(Pronoun.he()))),
    "He like himself."
)

sc.setCorpus(
    Noun.doT(DeterminerN.female(Pronoun.he()),Verb("like"),DeterminerN.reflexive(DeterminerN.female(Pronoun.he()))),
    "She like herself."
)

sc.setCorpus(
    Noun.doT(DeterminerN.thing(Pronoun.he()),Verb("like"),DeterminerN.reflexive(DeterminerN.thing(Pronoun.he()))),
    "It like itself."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.he()),Verb("like"),DeterminerN.reflexive(DeterminerN.plural(Pronoun.he()))),
    "They like themselves."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),WordV.create(),DeterminerN.etc(Noun("table")))),
    "I created table etc."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),WordV.create(),DeterminerN.etc(Noun("chair")))),
    "I created chair etc."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),WordV.create(),DeterminerN.abstract(Noun("table")))),
    "I created table-ish."
)

sc.setCorpus(
    Noun.eq(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("machine"))),Verb.none(),DeterminerN.abstract(Noun("power"))),
    "This machine is powerful."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Pronoun.distal())))),
    "I go there."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Pronoun.distal()))))),
    "I went there."
)

sub_sentence_05=Phrase.past(Noun.do(Pronoun.you(),Verb.progressive(Verb("eat"))))

sc.setCorpus(
    sub_sentence_05,
    "You were eating."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.place(Pronoun.distal())),Modifier.N2M(DeterminerN.time(DeterminerN.section(sub_sentence_05))))))),
    "I went there while you were eating."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.place(Pronoun.distal())),Modifier.N2M(DeterminerN.time(DeterminerN.past(sub_sentence_05))))))),
    "I went there before you were eating."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.place(Pronoun.distal())),Modifier.N2M(DeterminerN.time(DeterminerN.future(sub_sentence_05))))))),
    "I went there after you were eating."
)

sc.setCorpus(
    Noun.eq(Pronoun.proximal(),Verb.none(),Noun("machine")),
    "This is a machine."
)

sc.setCorpus(
    Noun.eq(Pronoun.distal(),Verb.none(),Noun("machine")),
    "That is a machine."
)

sc.setCorpus(
    Noun.eq(DeterminerN.plural(Pronoun.proximal()),Verb.none(),DeterminerN.plural(Noun("machine"))),
    "These are machines."
)

sc.setCorpus(
    Noun.eq(DeterminerN.plural(Pronoun.distal()),Verb.none(),DeterminerN.plural(Noun("machine"))),
    "Those are machines."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.indefinite(),Verb("open"),Noun("door"))),
    "Someone opened the door."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.indefinite(),Verb("close"),Noun("door"))),
    "Someone closed the door."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),WordV.create(),Noun("bag")),
    "I create a bag."
)

sc.setCorpus(
    Noun.doT(Pronoun.you(),WordV.create(),Noun("bag")),
    "You create a bag."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),WordV.destroy(),Noun("bag")),
    "I break a bag."
)

sc.setCorpus(
    Noun.doT(Pronoun.you(),WordV.destroy(),Noun("bag")),
    "You break a bag."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))),
    "I walked in Tokyo."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(WordV.act(),Modifier.N2M(DeterminerN.affect(Noun("engineer"))))),
    "I work as engineer."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(WordV.turn(),Modifier.N2M(DeterminerN.move(DeterminerN.place(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("home")))))))),
    "I turned around my home."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(WordV.turn(),Modifier.N2M(DeterminerN.move(DeterminerN.place(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("home")))))))),
    "I turned through my home."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),WordV.receive(),Noun("rice"))),
    "I ate rice."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.add(WordV.receive(),Modifier.N2M(DeterminerN.move(DeterminerN.In(Noun("box"))))),Noun("ball"))),
    "I put the ball in the box."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),WordV.stimulate(),Pronoun.you(),Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("bag"))))),
    "I send you my bag."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),WordV.stimulate(),Pronoun.you(),Noun.haveP(Noun("notice"),Verb.none(),Modifier("important")))),
    "I told you an important notice."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(WordV.exist(),Modifier.N2M(DeterminerN.place(Noun.have(Pronoun.you(),Verb.none(),DeterminerN.stressed(Noun("home"))))))),
    "I stay in your home."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(WordV.exist(),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "I live in Tokyo."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),WordV.use(),Noun("computer"))),
    "I used computer."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.you(),WordV.use(),Noun("computer"))),
    "You used computer."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),WordV.change(),Noun("doctor"))),
    "I become doctor."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),WordV.change(),Noun("clerk"))),
    "I become clerk."
)

sc.setCorpus(
    Noun.haveP(Noun("window"),Verb.none(),WordM.big()),
    "This window is big."
)

sc.setCorpus(
    Noun.haveP(Noun("stick"),Verb.none(),WordM.big()),
    "This stick is long."
)

sc.setCorpus(
    Noun.haveP(Noun("window"),Verb.none(),WordM.good()),
    "This window is good."
)

sc.setCorpus(
    Noun.haveP(Noun("stick"),Verb.none(),WordM.good()),
    "This stick is new."
)

sc.setCorpus(
    Noun.haveP(DeterminerN.plural(Pronoun.I()),Verb.none(),WordM.near()),
    "We are close."
)

sc.setCorpus(
    Noun.haveP(Noun.AND(Pronoun.you(),Pronoun.I()),Verb.none(),WordM.near()),
    "You and I are close."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("room"))),Verb.none(),WordM.bright()),
    "This room is bright."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("table"))),Verb.none(),WordM.bright()),
    "This table is white."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.add(Verb("study"),Modifier.add(Modifier.N2M(DeterminerN.start(DeterminerN.time(Noun("10am")))),Modifier.N2M(DeterminerN.end(DeterminerN.time(Noun("12am")))))),Noun("mathematics"))),
    "I studied mathematics from 10am to 12am."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("work"),Modifier.add(Modifier.N2M(DeterminerN.start(DeterminerN.time(Noun("8am")))),Modifier.N2M(DeterminerN.end(DeterminerN.time(Noun("8pm")))))))),
    "I worked from 8am to 8pm."
)

sc.setCorpus(
    Noun.haveP(Noun.haveP(DeterminerN.all(DeterminerN.plural(Noun("student"))),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school")))))),Verb.none(),Modifier("wise")),
    "All students in my school is wise."
)

sc.setCorpus(
    Noun.haveP(Noun.haveP(DeterminerN.many(DeterminerN.plural(Noun("student"))),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school")))))),Verb.none(),Modifier("wise")),
    "Many students in my school is wise."
)

sc.setCorpus(
    Noun.haveP(Noun.haveP(DeterminerN.some(DeterminerN.plural(Noun("student"))),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school")))))),Verb.none(),Modifier("wise")),
    "Some students in my school is wise."
)

sc.setCorpus(
    Noun.haveP(Noun.haveP(DeterminerN.one(DeterminerN.plural(Noun("student"))),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school")))))),Verb.none(),Modifier("wise")),
    "One students in my school is wise."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb.perfective(Verb("study")),Modifier.add(Modifier.N2M(DeterminerN.time(Pronoun.proximal())),Modifier.N2M(DeterminerN.time(DeterminerN.start(Noun("8:00"))))))),
    "I have studied here since 8:00."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb.add(Verb.perfective(Verb("seen")),Modifier.N2M(Noun.eq(Noun("three"),Verb.none(),Noun("time")))),Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("movie")))),
    "I have seen this movie three times."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb.add(Verb.perfective(Verb("finish")),Modifier("already")),Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("homework")))),
    "I have already finished my homework."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))))),Modifier.N2M(DeterminerN.affected(DeterminerN.near(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("friend")))))))))),
    "I went to my school with my friend."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))))),Modifier.N2M(DeterminerN.past(DeterminerN.time(Noun("8am")))))))),
    "I went to my school before 8am."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))))),Modifier.N2M(DeterminerN.future(DeterminerN.time(Noun("8am")))))))),
    "I went to my school after 8am."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.add(Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))))),Modifier.N2M(DeterminerN.reason(Noun("procedure"))))))),
    "I went to school for the procedure."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.biology(Pronoun.proximal())),
    "I like this biology."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.thing(Pronoun.proximal())),
    "I like this thing."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.time(Pronoun.proximal())),
    "I like this time."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.place(Pronoun.proximal())),
    "I like this place."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.reason(Pronoun.proximal())),
    "I like this reason."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.method(Pronoun.proximal())),
    "I like this method."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.human(Pronoun.proximal())),
    "I like this human."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.animal(Pronoun.proximal())),
    "I like this animal."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.plant(Pronoun.proximal())),
    "I like this plant."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),DeterminerN.material(Pronoun.proximal())),
    "I like this material."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),Noun.V2N(Verb("read"))),
    "I like reading."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("decide"),Noun.M2N(Modifier("long")))),
    "I decided length."
)

sc.setCorpus(
    Noun.do(DeterminerN.many(Noun.eq(DeterminerN.plural(Pronoun.proximal()),Verb.none(),DeterminerN.stressed(DeterminerN.plural(Noun("leaf"))))),Verb.M2V(Modifier("red"))),
    "Many those leaves turn red.",
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb.N2V(Noun("e-mail")),Pronoun.you())),
    "I e-mailed you."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun("France")))))),
    "I went to France."
)

sc.setCorpus(
    Phrase.past(Noun.haveP(Pronoun.I(),Verb.none(),Modifier.V2M(Verb.passive(Verb("surprise"))))),
    "I was surprised."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),Noun.doT(Noun.none(),Verb("watch"),Noun("Youtube"))),
    "I like watching Youtube."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),Noun.doT(Noun.none(),Verb("play"),Noun("Minecraft"))),
    "I like playing Minecraft."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb("like"),Noun("programming")),
    "I like programming."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),Verb.M2V(WordM.near()),Noun.V2N(Verb("program"))),
    "I like programming."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("table"))),Verb.none(),WordM.bright()),
    "This table is colorful."
)

sub_sentence_06=Noun.haveP(Noun.AND(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("table"))),Noun("sea")),Verb.none(),Modifier.add(WordM.near(),WordM.bright()))

sc.setCorpus(
    sub_sentence_06,
    "This table and the sea are similar in color."
)

sub_sentence_07=Noun.have(Pronoun.I(),Verb.none(),sub_sentence_06)

sc.setCorpus(
    sub_sentence_07,
    "I have this table is colored like the sea."
)

sub_sentence_08=lambda x=(lambda x:x):Noun.give(Pronoun.I(),x(Verb("lend")),DeterminerN.male(Pronoun.he()),sub_sentence_07)

sc.setCorpus(
    sub_sentence_08(),
    "I lend this my table is colored like the sea to him."
)

sc.setCorpus(
    sub_sentence_08(lambda x:Verb.add(x,Modifier("will"))),
    "I will lend this my table is colored like the sea to him."
)

sc.setCorpus(
    Phrase.past(sub_sentence_08()),
    "I lent this my table is colored like the sea to him."
)

sub_sentence_08_will=sub_sentence_08(lambda x:Verb.add(x,Modifier("will")))

sc.setCorpus(
    Phrase.past(sub_sentence_08_will),
    "I will lent this my table is colored like the sea to him."
)

sub_sentence_09=Noun.give(Noun.do(DeterminerN.male(Pronoun.he()),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),Verb("say"),Pronoun.I(),Noun.doT(Pronoun.I(),Verb("want"),Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("table")))))

sc.setCorpus(
    sub_sentence_09,
    "He who live in Tokyo say me I want this table."
)

sc.setCorpus(
    Noun.IF(sub_sentence_09,sub_sentence_08_will),
    "If he who live in Tokyo say me I want this table, I will lend this my table is colored like the sea to him.",
)

sc.setCorpus(
    Noun.IF(Phrase.past(sub_sentence_09),Phrase.past(sub_sentence_08_will)),
    "If he who live in Tokyo said me I want this table, I would lend this my table is colored like the sea to him.",
    md_out_path=OUT_DIR+"sample01_01.md"
)

sc.setCorpus(
    Bool.B2N(Noun.have(Pronoun.I(),Verb.none(),Noun("pen")),Bool.false()),
    "'I have a pen' is False."
)

sc.setCorpus(
    Bool.B2N(Noun.have(Pronoun.I(),Verb.none(),Noun("pen")),Bool.true()),
    "'I have a pen' is True."
)

sc.setCorpus(
    Noun.eq(BoolList.NaturalNum(BoolList.append(BoolList.append(BoolList(),Bool.true()),Bool.false())),Verb.none(),Noun.haveP(Noun("2"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun("binary"))))),
    "'10' is 2 in binary."
)

sc.setCorpus(
    Noun.eq(BoolList.NaturalNum(BoolList.twoBit(Bool.true(),Bool.false())),Verb.none(),Noun.haveP(Noun("2"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun("binary"))))),
    "'10' is 2 in binary."
)

sc.setCorpus(
    Noun.eq(BoolList.NaturalNum(BoolList.twoBit(Bool.true(),Bool.false())),Verb.none(),Noun.haveP(Noun("3"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun("binary"))))),
    "'11' is 3 in binary."
)

sc.setCorpus(
    Noun.eq(BoolList.NaturalNum(BoolList.fourBit(Bool.true(),Bool.false(),Bool.false(),Bool.false())),Verb.none(),Noun.haveP(Noun("8"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun("binary"))))),
    "'1000' is 8 in binary."
)

sc.setCorpus(
    Noun.eq(BoolList.NaturalNum(BoolList.fourBit(Bool.true(),Bool.false(),Bool.false(),Bool.false())),Verb.none(),Noun.haveP(Noun("10"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun("binary"))))),
    "'1010' is 10 in binary."
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("pen"),Verb.none(),BoolList.NaturalNum(BoolList.fourBit(Bool.true(),Bool.false(),Bool.false(),Bool.false())))),
    "I have ten pens."
)

#0100 0001
b1=BoolList.byte(Bool.false(),Bool.true(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.true())
b1_1=BoolList.NaturalNum(b1)#65
b1_2=BoolList.Int(b1)#65
b1_3=BoolList.ASCII(b1)#A

sc.setCorpus(
    Noun.eq(b1_1,Verb.none(),Noun.haveP(Noun("65"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("natural")))))),
    "'01000001' is 65 in natural number."
)

sc.setCorpus(
    Noun.eq(b1_2,Verb.none(),Noun.haveP(Noun("65"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("integer")))))),
    "'01000001' is 65 in integer number."
)

sc.setCorpus(
    Noun.eq(b1_3,Verb.none(),Noun.haveP(Noun("A"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("character"),Verb.none(),Modifier("ascii")))))),
    "'01000001' is A in ascii character."
)

#0100 0001
b2=BoolList.byte(Bool.false(),Bool.true(),Bool.true(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.true())
b2_1=BoolList.NaturalNum(b1)#97
b2_2=BoolList.Int(b1)#97
b2_3=BoolList.ASCII(b1)#a

sc.setCorpus(
    Noun.eq(b2_1,Verb.none(),Noun.haveP(Noun("97"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("natural")))))),
    "'01100001' is 97 in natural number."
)

sc.setCorpus(
    Noun.eq(b2_2,Verb.none(),Noun.haveP(Noun("97"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("integer")))))),
    "'01100001' is 97 in integer number."
)

sc.setCorpus(
    Noun.eq(b2_3,Verb.none(),Noun.haveP(Noun("a"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("character"),Verb.none(),Modifier("ascii")))))),
    "'01100001' is a in ascii character."
)

b3_bin_str="1"+"10001001"+"00000000000100000000000"
b3=BoolList.binstr32ToBoolList(b3_bin_str)
b3_1=BoolList.NaturalNum(b3)#3296724992
b3_2=BoolList.Int(b3)#-998242304
b3_3=BoolList.Float(b3)#-1024.25

sc.setCorpus(
    Noun.eq(b3_1,Verb.none(),Noun.haveP(Noun("3296724992"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("natural")))))),
    "'"+b3_bin_str+"' is 3296724992 in natural number."
)

sc.setCorpus(
    Noun.eq(b3_1,Verb.none(),Noun.haveP(Noun("-998242304"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("integer")))))),
    "'"+b3_bin_str+"' is -998242304 in integer number."
)

sc.setCorpus(
    Noun.eq(b3_1,Verb.none(),Noun.haveP(Noun("-1024.25"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("float")))))),
    "'"+b3_bin_str+"' is -1024.25 in float number."
)

b4_bin_str="0"+"10000000"+"10010010000111111011011"
b4=BoolList.binstr32ToBoolList(b4_bin_str)
b4_1=BoolList.NaturalNum(b4)#1078530011
b4_2=BoolList.Int(b4)#1078530011
b4_3=BoolList.Float(b4)#3.1415927410125732

sc.setCorpus(
    Noun.eq(b4_1,Verb.none(),Noun.haveP(Noun("1078530011"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("natural")))))),
    "'"+b4_bin_str+"' is 1078530011 in natural number."
)

sc.setCorpus(
    Noun.eq(b4_1,Verb.none(),Noun.haveP(Noun("1078530011"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("integer")))))),
    "'"+b4_bin_str+"' is 1078530011 in integer number."
)

sub_sentence_10=Noun.eq(b4_1,Verb.none(),Noun.haveP(Noun("3.1415927410125732"),Verb.none(),Modifier.N2M(DeterminerN.In(Noun.haveP(Noun("number"),Verb.none(),Modifier("float"))))))

sc.setCorpus(
    sub_sentence_10,
    "'"+b4_bin_str+"' is 3.1415927410125732 in float number."
)

sub_sentence_11=Noun.haveP(Noun.AND(sub_sentence_10,Noun("pi")),Verb.none(),WordM.near())

sc.setCorpus(
    sub_sentence_11,
    "'"+b4_bin_str+"' is 3.1415927410125732 in float number and pi is close to."
)

sc.setCorpus(
    Phrase.So(sub_sentence_11,Noun.doT(Noun("SFGPL"),Verb.add(Verb("represent"),Modifier("can")),Noun.eq(Noun("Number"),Verb.none(),Noun.eq(Noun.haveP(Noun("point"),Verb.none(),Modifier("floating")),Verb.none(),Noun.haveP(Noun("precision"),Verb.none(),Modifier("single")))))),
    "'"+b4_bin_str+"' is 3.1415927410125732 in float number and pi is close to, so SFGPL can represent single-precision floating-point number.",
    md_out_path=OUT_DIR+"sample01_02.md"
)

#index_1=1
index_1=BoolList.fourBit(Bool.false(),Bool.false(),Bool.false(),Bool.true())
#index_2=3
index_2=BoolList.fourBit(Bool.false(),Bool.false(),Bool.true(),Bool.true())
#index_3=7
index_3=BoolList.fourBit(Bool.false(),Bool.true(),Bool.true(),Bool.true())

sc.setCorpus(
    Bool.B2N(Noun.none(),BoolList.get(b4,index_1)),
    "The 1st value of '"+b4_bin_str+"'is True."
)

sc.setCorpus(
    Bool.B2N(Noun.none(),BoolList.get(b4,index_2)),
    "The 3rd value of '"+b4_bin_str+"'is False."
)

sc.setCorpus(
    BoolList.slice(b4,index_1,index_2),
    "The first through third values of '"+b4_bin_str+"'is 100."
)

sc.setCorpus(
    BoolList.slice(b4,index_1,index_3),
    "The first through third values of '"+b4_bin_str+"'is 1000000."
)

func_01=LangList.append(LangList(),LangFunc.arg())

sc.setCorpus(
    LangFunc.setFunc(Noun("f1"),func_01),
    "Define a function f1 that returns its arguments as they are."
)

x1=LangList.append(LangList.append(LangList(),Noun("student")),Noun("teacher"))

sc.setCorpus(
    LangFunc.runFunc(Noun("f1"),x1),
    "Assign \""+str(x1)+"\" to f1."
)

number_bl_0=BoolList.twoBit(Bool.false(),Bool.false())
number_bl_1=BoolList.twoBit(Bool.false(),Bool.true())
number_bl_2=BoolList.twoBit(Bool.true(),Bool.false())
number_bl_3=BoolList.twoBit(Bool.true(),Bool.true())

func_02=LangList.append(LangList(),Bool.AND(LangList.get(LangFunc.arg(),number_bl_0),LangList.get(LangFunc.arg(),number_bl_1)))

sc.setCorpus(
    LangFunc.setFunc(Noun("f2"),func_02),
    "Define a function f2 that returns the logical product of the 0th and 1st values of the argument BoolList."
)

x2=LangList.append(LangList.append(LangList(),Bool.true()),Bool.false())

sc.setCorpus(
    LangFunc.runFunc(Noun("f2"),x2),
    "Assign \""+str(x2)+"\" to f2."
)

lang_list_01=LangList.append(LangList.append(LangList.append(LangList.append(LangList(),Pronoun.I()),Verb("go")),Pronoun.you()),Noun("student"))
lang_list_02=LangList.append(LangList.append(LangList.append(LangList.append(LangList(),Noun("apple")),Modifier("high")),Pronoun.proximal()),WordV.turn())
lang_list_03=LangList.append(LangList.append(LangList(),Noun.eq(Pronoun.I(),Verb.none(),Noun("student"))),Noun.have(Pronoun.I(),Verb.none(),Noun("pen")))
lang_list_04=LangList.add(LangList.add(lang_list_01,lang_list_02),lang_list_03)

sc.setCorpus(
    lang_list_04,
    "Combine \""+str(lang_list_01)+"\" and \""+str(lang_list_02)+"\"."
)

lang_list_05=LangList.slice(lang_list_04,number_bl_0,number_bl_1)

sc.setCorpus(
    lang_list_05,
    "Slicing the first from the zeroth of \""+str(lang_list_04)+"\" yields \""+str(lang_list_05)+"\"."
)

lang_list_06=LangList.slice(lang_list_04,number_bl_0,number_bl_3)

sc.setCorpus(
    lang_list_06,
    "Slicing the third from the zeroth of \""+str(lang_list_04)+"\" yields \""+str(lang_list_06)+"\"."
)

lang_list_06_01=LangList.get(lang_list_06,number_bl_0)

sc.setCorpus(
    lang_list_06_01,
    "Slicing the third from the zeroth of \""+str(lang_list_04)+"\" yields \""+str(lang_list_06)+"\" and the zeroth value in that list is \""+str(lang_list_06_01)+"\".",
    md_out_path=OUT_DIR+"sample01_03.md"
)

lang_list_07=lambda tense=void_func,determinerV=void_func:tense(Noun.doT(DeterminerN.male(Pronoun.he()),determinerV(Verb("study")),Noun("English")))

sc.setCorpus(
    lang_list_07(),
    "He study English."
)

sc.setCorpus(
    lang_list_07(tense=Phrase.past),
    "He studied English."
)

sc.setCorpus(
    lang_list_07(tense=Phrase.past,determinerV=DeterminerV.Estimation100),
    "He 100% probability studied English."
)

sc.setCorpus(
    lang_list_07(tense=Phrase.past,determinerV=DeterminerV.Estimation75),
    "He 75% probability studied English."
)

sc.setCorpus(
    lang_list_07(tense=Phrase.past,determinerV=DeterminerV.Estimation50),
    "He 50% probability studied English."
)

sc.setCorpus(
    lang_list_07(tense=Phrase.past,determinerV=DeterminerV.Estimation25),
    "He 25% probability studied English."
)

sc.setCorpus(
    lang_list_07(tense=Phrase.past,determinerV=DeterminerV.Estimation0),
    "He 0% probability studied English."
)

sc.setCorpus(
    lang_list_07(determinerV=DeterminerV.Frequency100),
    "He 100% frequently study English."
)

sc.setCorpus(
    lang_list_07(determinerV=DeterminerV.Frequency75),
    "He 75% frequently study English."
)

sc.setCorpus(
    lang_list_07(determinerV=DeterminerV.Frequency50),
    "He 50% frequently study English."
)

sc.setCorpus(
    lang_list_07(determinerV=DeterminerV.Frequency25),
    "He 25% frequently study English."
)

sc.setCorpus(
    lang_list_07(determinerV=DeterminerV.Frequency0),
    "He 0% frequently study English."
)

lang_list_08=lambda tense=void_func,determinerV=void_func:tense(Noun.do(DeterminerN.male(Pronoun.he()),Verb.add(determinerV(Verb("go")),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))))

sc.setCorpus(
    lang_list_08(),
    "He goes to Tokyo."
)

sc.setCorpus(
    lang_list_08(tense=Phrase.past),
    "He went to Tokyo."
)

sc.setCorpus(
    lang_list_08(tense=Phrase.past,determinerV=DeterminerV.Estimation100),
    "He 100% probability went to Tokyo."
)

sc.setCorpus(
    lang_list_08(tense=Phrase.past,determinerV=DeterminerV.Estimation75),
    "He 75% probability went to Tokyo."
)

sc.setCorpus(
    lang_list_08(tense=Phrase.past,determinerV=DeterminerV.Estimation50),
    "He 50% probability went to Tokyo."
)

sc.setCorpus(
    lang_list_08(tense=Phrase.past,determinerV=DeterminerV.Estimation25),
    "He 25% probability went to Tokyo."
)

sc.setCorpus(
    lang_list_08(tense=Phrase.past,determinerV=DeterminerV.Estimation0),
    "He 0% probability went to Tokyo."
)

sc.setCorpus(
    lang_list_08(determinerV=DeterminerV.Frequency100),
    "He 100% frequently goes to Tokyo."
)

sc.setCorpus(
    lang_list_08(determinerV=DeterminerV.Frequency75),
    "He 75% frequently goes to Tokyo."
)

sc.setCorpus(
    lang_list_08(determinerV=DeterminerV.Frequency50),
    "He 50% frequently goes to Tokyo."
)

sc.setCorpus(
    lang_list_08(determinerV=DeterminerV.Frequency25),
    "He 25% frequently goes to Tokyo."
)

sc.setCorpus(
    lang_list_08(determinerV=DeterminerV.Frequency0),
    "He 0% frequently goes to Tokyo."
)

lang_list_09=lambda determinerV=void_func:(Noun.doT(Pronoun.I(),determinerV(Verb("wear")),Noun("dress")))

sc.setCorpus(
    lang_list_09(),
    "I wear a dress."
)

sc.setCorpus(
    lang_list_09(DeterminerV.Start),
    "I start to wear a dress. (The state in which the wearing operation is initiated)"
)

sc.setCorpus(
    lang_list_09(DeterminerV.Condition),
    "I am in the process of changing a dress. (in the process of changing a dress)"
)

sc.setCorpus(
    lang_list_09(DeterminerV.Complete),
    "I end to change a dress. (Finished changing a dress and wearing them)"
)

sc.setCorpus(
    lang_list_09(DeterminerV.Continue),
    "I'm in a state wearing a dress. (Wearing)"
)

sc.setCorpus(
    lang_list_09(DeterminerV.Continue),
    "I finish wearing a dress. (Finished wearing and undressing or beginning to undress)"
)

lang_list_10=lambda tense_base=void_func,determinerV=void_func:(tense_base(Noun.do(Pronoun.I(),determinerV(Verb("sit")))))

sc.setCorpus(
    lang_list_10(),
    "I sit."
)

sc.setCorpus(
    lang_list_10(determinerV=DeterminerV.Start),
    "I start to sit."
)

sc.setCorpus(
    lang_list_10(determinerV=DeterminerV.Condition),
    "I am in the process of sitting down."
)

sc.setCorpus(
    lang_list_10(determinerV=DeterminerV.Complete),
    "I complete the sitting process."
)

sc.setCorpus(
    lang_list_10(determinerV=DeterminerV.Continue),
    "I am in a sitting position."
)

sc.setCorpus(
    lang_list_10(determinerV=DeterminerV.Continue),
    "I finish sitting and begin to stand."
)

lang_list_11=lambda subject=Pronoun.I(),tense_base=void_func,determinerV=void_func:(tense_base(Noun.doT(subject,determinerV(Verb("create")),Noun("table"))))

sc.setCorpus(
    lang_list_11(),
    "I create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.present),
    "I create a table."
)

sc.setCorpus(
    lang_list_11(tense_base=Phrase.past),
    "I created a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.past),
    "I created a table."
)

sc.setCorpus(
    lang_list_11(tense_base=Phrase.future),
    "I will create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.future),
    "I will create a table."
)

sc.setCorpus(
    lang_list_11(tense_base=Phrase.past,determinerV=DeterminerV.past),
    "I created a table.(Past in the past at a point in time)"
)

sc.setCorpus(
    lang_list_11(tense_base=Phrase.past,determinerV=DeterminerV.present),
    "I created a table.(Present in the past at a point in time)"
)

sc.setCorpus(
    lang_list_11(tense_base=Phrase.past,determinerV=DeterminerV.future),
    "I would create a table.(Future in the past at a point in time)"
)

sc.setCorpus(
    lang_list_11(tense_base=Phrase.past,determinerV=DeterminerV.past),
    "I will have created a table.(Past in the future at a point in time)"
)

sc.setCorpus(
    lang_list_11(tense_base=Phrase.past,determinerV=DeterminerV.present),
    "I will create a table.(Present in the future at a point in time)"
)

sc.setCorpus(
    lang_list_11(tense_base=Phrase.past,determinerV=DeterminerV.future),
    "I will create a table.(Future in the future at a point in time)"
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.Possible),
    "I can create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.Ability),
    "I can create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.Will),
    "I will create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.Obligation),
    "I should create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.Necessary),
    "I need to create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.Duty),
    "I must create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.forced),
    "I am forced to create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.want),
    "I want to create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.dare),
    "I dare create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.allow),
    "I allow to create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.easy),
    "I am easy to create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.hard),
    "I am hard to create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.habit),
    "I habitually create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.Polite),
    "I create a table.(polite expression)"
)

sc.setCorpus(
    lang_list_11(subject=DeterminerN.male(Pronoun.he()),determinerV=DeterminerV.Respect),
    "He creates a table.(respectful expression)"
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.volitional),
    "I consciously create a table."
)

sc.setCorpus(
    lang_list_11(determinerV=DeterminerV.nonVolitional),
    "I unconsciously create a table."
)

sc.setCorpus(
    Phrase.interrogative(lang_list_11(subject=Pronoun.you(),determinerV=DeterminerV.Requests)),
    "Can you create a table?"
)

sc.setCorpus(
    Phrase.interrogative(lang_list_11(determinerV=DeterminerV.Permission)),
    "May I create a table?"
)

sc.setCorpus(
    Phrase.interrogative(lang_list_11(determinerV=DeterminerV.Suggestion)),
    "Shall I create a table?"
)

lang_list_12=lambda subject=Pronoun.I(),tense_base=void_func,determinerV=void_func:(tense_base(Noun.doT(subject,determinerV(Verb("teach")),Noun.eq(Noun("engineering"),Verb.none(),Noun("information")))))

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.Possible),
    "I can teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.Ability),
    "I can teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.Will),
    "I will teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.Obligation),
    "I should teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.Necessary),
    "I need to teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.Duty),
    "I must teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.forced),
    "I am forced to teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.want),
    "I want to teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.dare),
    "I dare teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.allow),
    "I allow to teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.easy),
    "I am easy to teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.hard),
    "I am hard to teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.habit),
    "I habitually teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.Polite),
    "I teach information engineering.(polite expression)"
)

sc.setCorpus(
    lang_list_12(subject=DeterminerN.male(Pronoun.he()),determinerV=DeterminerV.Respect),
    "He teaches information engineering.(respectful expression)"
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.volitional),
    "I consciously teach information engineering."
)

sc.setCorpus(
    lang_list_12(determinerV=DeterminerV.nonVolitional),
    "I unconsciously teach information engineering."
)

sc.setCorpus(
    Phrase.interrogative(lang_list_12(subject=Pronoun.you(),determinerV=DeterminerV.Requests)),
    "Can you teach information engineering?"
)

sc.setCorpus(
    Phrase.interrogative(lang_list_12(determinerV=DeterminerV.Permission)),
    "May I teach information engineering?"
)

sc.setCorpus(
    Phrase.interrogative(lang_list_12(determinerV=DeterminerV.Suggestion)),
    "Shall I teach information engineering?"
)

sc.setCorpus(
    Noun.do(Pronoun.I(),DeterminerV.Ability(Verb("swim"))),
    "I can swim."
)

sc.setCorpus(
    Phrase.NOT(Noun.do(Pronoun.I(),DeterminerV.Ability(Verb("swim")))),
    "I can't swim."
)

sc.setCorpus(
    Phrase.past(Noun.do(Pronoun.I(),DeterminerV.Ability(Verb("swim")))),
    "I could swim."
)

sc.setCorpus(
    Phrase.past(Phrase.NOT(Noun.do(Pronoun.I(),DeterminerV.Ability(Verb("swim"))))),
    "I couldn't swim."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(DeterminerV.Possible(Verb("rest")),Modifier.N2M(DeterminerN.time(Noun("tomorrow"))))),
    "I can rest tomorrow."
)

sc.setCorpus(
    Phrase.NOT(Noun.do(Pronoun.I(),Verb.add(DeterminerV.Possible(Verb("rest")),Modifier.N2M(DeterminerN.time(Noun("tomorrow")))))),
    "I can't rest tomorrow."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(DeterminerV.Duty(Verb("rest")),Modifier.N2M(DeterminerN.time(Noun("tomorrow"))))),
    "I have to rest tomorrow."
)

sc.setCorpus(
    Phrase.NOT(Noun.do(Pronoun.I(),Verb.add(DeterminerV.Duty(Verb("rest")),Modifier.N2M(DeterminerN.time(Noun("tomorrow")))))),
    "I don't have to rest tomorrow."
)

lang_list_13=lambda x:Noun.do(Pronoun.I(),Verb.add(x(Verb("go")),Modifier.N2M(DeterminerN.place(Noun("NewYork")))))

sc.setCorpus(
    lang_list_13(DeterminerV.easy),
    "I am easy to go to New York."
)

sc.setCorpus(
    lang_list_13(DeterminerV.hard),
    "I am hard to go to New York."
)

sc.setCorpus(
    Phrase.past(lang_list_13(DeterminerV.easy)),
    "I was easy to go to New York."
)

sc.setCorpus(
    Phrase.past(lang_list_13(DeterminerV.hard)),
    "I was hard to go to New York."
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
    Phrase.past(Noun.hearSay(Pronoun.I(),Verb.none(),Noun.doT(DeterminerN.male(Pronoun.he()),Verb("create"),Noun("table")),Noun("John"))),
    "According to John, I heard that he create a table."
)

sc.setCorpus(
    Phrase.past(Noun.hearSay(Pronoun.you(),Verb.none(),Noun.doT(DeterminerN.male(Pronoun.he()),Verb("create"),Noun("table")),Noun("John"))),
    "According to John, you heard that he create a table."
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("apple"),Verb.none(),NumberList.digit1(Number.three()))),
    "I have 3 apples."
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("apple"),Verb.none(),NumberList.append(NumberList(),Number.six()))),
    "I have 6 apples."
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("apple"),Verb.none(),NumberList.digit2(Number.one(),Number.five()))),
    "I have 15 apples."
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("apple"),Verb.none(),NumberList.digit2(Number.two(),Number.three()))),
    "I have 23 apples."
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("peach"),Verb.none(),NumberList.digit1(Number.nine()))),
    "I have 9 peaches."
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("peach"),Verb.none(),NumberList.digit2(Number.one(),Number.zero()))),
    "I have 10 peaches."
)

sc.setCorpus(
    Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("peach"),Verb.none(),NumberList.append(NumberList.append(NumberList(),Number.one()),Number.zero()))),
    "I have 10 peaches."
)

sc.setCorpus(
    Noun.have(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))),Verb.none(),Noun.eq(Noun("people"),Verb.none(),NumberList.digit3(Number.five(),Number.two(),Number.seven()))),
    "My school has 527 people."
)

sc.setCorpus(
    Noun.have(Noun.belong(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("school"))),Verb.none(),Noun.eq(Noun("people"),Verb.none(),NumberList.digit3(Number.four(),Number.zero(),Number.nine()))),
    "His school has 409 people."
)

sc.setCorpus(
    Noun.have(Noun.belong(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("village"))),Verb.none(),Noun.eq(Noun("people"),Verb.none(),NumberList.digit4(Number.one(),Number.three(),Number.two(),Number.four()))),
    "This village has 1324 people."
)

sc.setCorpus(
    Noun.have(Noun.belong(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("town"))),Verb.none(),Noun.eq(Noun("people"),Verb.none(),NumberList.digit4(Number.eight(),Number.one(),Number.two(),Number.three()))),
    "This town has 8123 people."
)

sc.setCorpus(
    Noun.have(Noun.belong(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("city"))),Verb.none(),Noun.eq(Noun("people"),Verb.none(),NumberList.digit5(Number.six(),Number.three(),Number.two(),Number.eight(),Number.seven()))),
    "This city has 63287 people."
)

sc.setCorpus(
    Noun.have(Noun("Tokyo"),Verb.none(),Noun.eq(Noun("people"),Verb.none(),NumberList.add(NumberList.digit3(Number.one(),Number.four(),Number.one()),NumberList.digit5(Number.one(),Number.zero(),Number.seven(),Number.three(),Number.three())))),
    "Tokyo has 14110733 people."
)

sc.setCorpus(
    Noun.have(Noun("Japan"),Verb.none(),Noun.eq(Noun("people"),Verb.none(),NumberList.add(NumberList.digit4(Number.one(),Number.two(),Number.five(),Number.four()),NumberList.digit5(Number.one(),Number.six(),Number.eight(),Number.seven(),Number.seven())))),
    "Japan has 125416877 people."
)

num_1024=NumberList.digit4(Number.one(),Number.zero(),Number.two(),Number.four())

sc.setCorpus(
    NumberList.get(num_1024,NumberList.IntNL2BL(NumberList.digit1(Number.zero()))),
    "The upper 0th digit of 1024 is 1."
)

sc.setCorpus(
    NumberList.get(num_1024,NumberList.IntNL2BL(NumberList.digit1(Number.three()))),
    "The upper 3rd digit of 1024 is 4."
)

sc.setCorpus(
    NumberList.slice(num_1024,NumberList.IntNL2BL(NumberList.digit1(Number.zero())),NumberList.IntNL2BL(NumberList.digit1(Number.one()))),
    "The upper 2 digit of 1024 is 10."
)

sc.setCorpus(
    NumberList.slice(num_1024,NumberList.IntNL2BL(NumberList.digit1(Number.zero())),NumberList.IntNL2BL(NumberList.digit1(Number.two()))),
    "The upper 3 digit of 1024 is 102."
)

num_16=NumberList.digit2(Number.one(),Number.six())
num_60=NumberList.digit2(Number.six(),Number.zero())
num_12=NumberList.digit2(Number.one(),Number.two())
num_3=NumberList.digit1(Number.three())

calc_01=NumberList.calcSub(NumberList.calcAdd(NumberList.calcDiv(num_1024,num_16),num_60),NumberList.calcMul(num_12,num_3))

sc.setCorpus(
    calc_01,
    "1024/16+60-12*3=88."
)

sc.setCorpus(
    NumberList.IntNL2BL(calc_01),
    "Converting 88 in decimal to binary gives 01011000."
)

sc.setCorpus(
    BoolList.IntBL2NL(NumberList.IntNL2BL(calc_01)),
    "Converting the binary number 01011000 to decimal gives 88."
)

num_360=NumberList.digit3(Number.three(),Number.six(),Number.zero())
num_32768=NumberList.digit5(Number.three(),Number.two(),Number.seven(),Number.six(),Number.eight())
num_9=NumberList.digit1(Number.nine())
num_95=NumberList.digit2(Number.nine(),Number.five())

calc_02=NumberList.calcAdd(NumberList.calcSub(NumberList.calcAdd(NumberList.calcDiv(num_32768,num_1024),NumberList.calcDiv(num_360,num_60)),NumberList.calcMul(num_9,num_12)),num_95)

sc.setCorpus(
    calc_02,
    "32768/1024+360/60-9*12+95=25."
)

sc.setCorpus(
    NumberList.IntNL2BL(calc_02),
    "Converting 25 in decimal to binary gives 00011001."
)

sc.setCorpus(
    BoolList.IntBL2NL(NumberList.IntNL2BL(calc_02)),
    "Converting the binary number 00011001 to decimal gives 25."
)

calc_03=NumberList.calcSub(calc_01,calc_02)

sc.setCorpus(
    calc_03,
    "(1024/16+60-12*3)-(32768/1024+360/60-9*12+95)=63."
)

sc.setCorpus(
    NumberList.IntNL2BL(calc_03),
    "Converting 63 in decimal to binary gives 00111111."
)

sc.setCorpus(
    BoolList.IntBL2NL(NumberList.IntNL2BL(calc_03)),
    "Converting the binary number 00111111 to decimal gives 63."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("bag"))),Verb.none(),Modifier.Very(WordM.big())),
    "This bag is very big."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("bag"))),Verb.none(),Modifier.Very(Modifier.Neg(WordM.big()))),
    "This bag is very small."
)

I_have_a_pen=Noun.have(Pronoun.I(),Verb.none(),Noun("pen"))

sc.setCorpus(
    LangObj.logicIFELSE(Bool.true(),I_have_a_pen,Phrase.NOT(I_have_a_pen)),
    "if true, I have a pen."
)

sc.setCorpus(
    LangObj.logicIFELSE(Bool.false(),I_have_a_pen,Phrase.NOT(I_have_a_pen)),
    "if false, I don't have a pen."
)

sc.setCorpus(
    Bool.B2N(Noun("true"),NumberList.isPN(NumberList.calcSub(num_16,num_9))),
    "If 16 and 9, 16 is greater."
)

sc.setCorpus(
    Bool.B2N(Noun("false"),NumberList.isPN(NumberList.calcSub(num_9,num_16))),
    "If 16 and 9, 16 is greater."
)

sc.setCorpus(
    Bool.B2N(Noun("false"),NumberList.isPN(NumberList.calcSub(num_9,num_16))),
    "If 16 and 9, 16 is greater."
)

def loopFunc(s:str,fin_num:NumberList,num_str:str,count_num:NumberList,count_str:str):
    num_0=NumberList.digit1(Number.zero())
    num_1=NumberList.digit1(Number.one())

    l_0=LangList.get(LangFunc.arg(),NumberList.IntNL2BL(num_0))
    l_1=LangList.get(LangFunc.arg(),NumberList.IntNL2BL(num_1))

    c_func_str="condition_func_"+s
    p_func_str="process_func_"+s

    sc.setCorpus(
        LangFunc.setFunc(Noun(c_func_str),LangList.append(LangList(),NumberList.isPN(NumberList.calcSub(fin_num,l_0)))),
        "Define a function for a condition as True if {} or less.".format(num_str)
    )

    sc.setCorpus(
        LangFunc.setFunc(Noun(p_func_str),LangList.append(LangList.append(LangList(),NumberList.calcAdd(l_0,num_1)),NumberList.calcAdd(l_1,count_num))),
        "Define the function for processing as [i+1,i+{}].".format(count_str)
    )
    
    a=LangList.append(LangList.append(LangList.append(LangList(),num_0),num_0),num_1)

    sc.setCorpus(
        a,
        "Define the initial value as [0,0]."
    )

    sc.setCorpus(
        LangList.While(a,Noun(c_func_str),Noun(p_func_str)),
        "Loop processing is performed with [0,0] as the initial value, {X} as the function for the condition and {Y} as the function for processing.".format(X=c_func_str,Y=p_func_str)
    )

loopFunc("01",NumberList.digit1(Number.two()),"2",NumberList.digit1(Number.two()),"2")
loopFunc("02",NumberList.digit1(Number.two()),"2",NumberList.digit1(Number.five()),"5")
loopFunc("03",NumberList.digit1(Number.three()),"3",NumberList.digit1(Number.five()),"5")
loopFunc("04",NumberList.digit1(Number.four()),"4",NumberList.digit2(Number.one(),Number.zero()),"10")

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("see"),Noun.do(DeterminerN.male(Pronoun.he()),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("school"))))))))),
    "I saw him go to his school."
)

sc.setCorpus(
    Phrase.future(Noun.doT(Pronoun.I(),Verb("buy"),Noun("computer"))),
    "I'm going to buy a computer."
)

sc.setCorpus(
    Phrase.past(Noun.do(Noun.eq(Noun("name"),Verb.none(),Noun.eq(Noun("era"),Verb.none(),Noun("Japan"))),Verb.add(Verb("change"),Modifier.AND(Modifier.AND(Modifier.N2M(DeterminerN.start(Noun("Heisei"))),Modifier.N2M(DeterminerN.end(Noun("Reiwa")))),Modifier.N2M(DeterminerN.time(Noun("2019"))))))),
    "Japan's era name changed from Heisei to Reiwa in 2019."
)

sc.setCorpus(
    Noun.gt(Noun("Tokyo_Sky_Tree"),Verb.none(),Modifier("tall"),Noun("Tokyo_Tower")),
    "The Tokyo Sky Tree is taller than the Tokyo Tower."
)

sc.setCorpus(
    appendixGrammar.Superlative(Noun("Tokyo_Sky_Tree"),Verb.none(),Modifier("tall"),Noun.AND(Noun.eq(Noun("tower"),Verb.none(),Noun("ratio")),Noun("the_world"))),
    "The Tokyo Sky Tree is the tallest radio tower in the world."
)

sc.setCorpus(
    appendixGrammar.EquivalentClass(Noun("Azabudai_Hills_Mori_JP_Tower"),Verb.none(),Modifier("tall"),Noun("Tokyo_Tower")),
    "The Azabudai Hills Mori JP Tower is as tall as the Tokyo Tower."
)

var1_name=Noun("var1")
lang_list_01=LangList.append(LangList.append(LangList(),Noun("a")),Noun("b"))

sc.setCorpus(
    lang_list_01,
    "Define [\"a\",\"b\"]."
)

sc.setCorpus(
    LangVar.set(var1_name,lang_list_01),
    "Assign [\"a\", \"b\"] to the variable named \"var1\"."
)

sc.setCorpus(
    LangVar.set(var1_name,LangList.append(LangVar.get(var1_name),Noun("c"))),
    "Add \"c\" to the variable named \"var1\"."
)

sc.setCorpus(
    LangVar.set(var1_name,LangList.append(LangVar.get(var1_name),Noun("d"))),
    "Add \"d\" to the variable named \"var1\"."
)

sc.setCorpus(
    Noun.eq(Pronoun.I(),Verb.none(),Noun.borrowed("student","English")),
    "I am student."
)

sc.setCorpus(
    Noun.eq(Pronoun.I(),Verb.none(),Noun.borrowed("学生","Japanese")),
    "私は学生です。"
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb.borrowed("go","English"),Modifier.N2M(DeterminerN.place(Noun.borrowed("London","English"))))),
    "I go to London."
)

sc.setCorpus(
    Noun.do(Pronoun.I(),Verb.add(Verb.borrowed("行く","Japanese"),Modifier.N2M(DeterminerN.place(Noun.borrowed("東京","Japanese"))))),
    "私は東京に行く。"
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun.borrowed("apple","English"))),Verb.none(),Modifier.borrowed("big","English")),
    "This apple is big."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun.borrowed("りんご","Japanese"))),Verb.none(),Modifier.borrowed("大きい","Japanese")),
    "このりんごは大きい。"
)

num_10=NumberList.digit2(Number.one(),Number.zero())
num_minus_10=NumberList.minus(num_10)

sc.setCorpus(
    Bool.B2N(Noun("false"),NumberList.isPN(num_minus_10)),
    "-10 isn't positive number."
)

sc.setCorpus(
    Bool.B2N(Noun("true"),NumberList.isPN(NumberList.abs(num_minus_10))),
    "abs(-10) is positive number."
)

num_1000=NumberList.digit4(Number.one(),Number.zero(),Number.zero(),Number.zero())

num_1_024=NumberList.calcDiv(num_1024,num_1000)
num_minus_1_024=NumberList.minus(num_1_024)

sc.setCorpus(
    Bool.B2N(Noun("false"),NumberList.isPN(num_minus_1_024)),
    "-1.024 isn't positive number."
)

sc.setCorpus(
    Bool.B2N(Noun("true"),NumberList.isPN(NumberList.abs(num_minus_1_024))),
    "abs(-1.024) is positive number."
)

sc.setCorpus(
    NumberList.calcAdd(num_10,num_minus_1_024),
    "10+(-1.024)=8.976"
)

sc.setCorpus(
    NumberList.calcSub(num_10,num_minus_1_024),
    "10-(-1.024)=11.024"
)

num_32_768=NumberList.calcDiv(num_32768,num_1000)
num_minus_32_768=NumberList.minus(num_32_768)

sc.setCorpus(
    NumberList.calcAdd(num_32_768,num_minus_1_024),
    "32.786+(-1.024)=31.762"
)

sc.setCorpus(
    NumberList.calcSub(num_32_768,num_minus_1_024),
    "32.786-(-1.024)=33.81"
)

sc.setCorpus(
    NumberList.calcAdd(num_minus_32_768,num_minus_1_024),
    "-32.786+(-1.024)=-33.81"
)

sc.setCorpus(
    NumberList.calcSub(num_minus_32_768,num_minus_1_024),
    "-32.786-(-1.024)=-31.762"
)

py_list01=[i*13 for i in range(13)]
sc.setCorpus(
    SFGPLLib.LangListLib.pyList2LangList(py_list01,func=BoolList.NaturalNum),
    f"Python list {py_list01} converted to LangList."
)

py_list02=[i*19 for i in range(19)]
sc.setCorpus(
    SFGPLLib.LangListLib.pyList2LangList(py_list02,func=BoolList.NaturalNum),
    f"Python list {py_list02} converted to LangList."
)

py_str01="abc"
sc.setCorpus(
    SFGPLLib.LangListLib.str2LangList(py_str01),
    f"String '{py_str01}' converted to LangList."
)

py_str02="I am student."
sc.setCorpus(
    SFGPLLib.LangListLib.str2LangList(py_str02),
    f"String '{py_str02}' converted to LangList."
)

sc.setCorpus(
    Noun.doT(DeterminerN.female(Pronoun.he()),Verb.borrowed("love","English"),Noun.V2N(Verb.borrowed("read","English"))),
    "She loves to read."
)

sc.setCorpus(
    Noun.do(Noun.borrowed("The_sun","English"),Verb.progressive(Verb.borrowed("shine","English"))),
    "The sun is shining."
)

sc.setCorpus(
    Noun.doT(Pronoun.I(),DeterminerV.Necessary(Verb.none()),DeterminerN.some(Noun.borrowed("help","English"))),
    "I need some help."
)

sc.setCorpus(
    Noun.doT(DeterminerN.male(Pronoun.he()),Verb.add(Verb.borrowed("speak","English"),Modifier.borrowed("fluently","English")),Noun.borrowed("French","English")),
    "He speaks French fluently."
)

sc.setCorpus(
    Noun.eq(DeterminerN.plural(Pronoun.I()),Verb.add(Verb.none(),Modifier("forever")),Noun("friend")),
    "We are friends forever."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.add(Verb("play"),Modifier.N2M(DeterminerN.every(Noun("weekend")))),Noun("soccer")),
    "They play soccer every weekend."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.add(Verb("play"),Modifier.N2M(DeterminerN.every(Noun("weekend")))),Noun.AND(Noun("soccer"),Noun("tennis"))),
    "They play soccer and tennis every weekend."
)

sc.setCorpus(
    Phrase.interrogative(Noun.have(Pronoun.you(),Verb.none(),Noun("table"))),
    "Do you have a table?"
)

sc.setCorpus(
    Bool.B2N(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.thing(Pronoun.he())),Bool.true()),
    "Yes, I have it."
)

sc.setCorpus(
    Bool.B2N(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.thing(Pronoun.he())),Bool.false()),
    "No, I don't have it."
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.every(Noun("student")),Verb("pass"),Noun.eq(DeterminerN.thing(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("exam"))))),
    "Every student passed the exam."
)

sc.setCorpus(
    Noun.doT(DeterminerN.female(Pronoun.he()),Verb.add(Verb("visit"),Modifier.N2M(DeterminerN.every(Noun("month")))),Noun.have(DeterminerN.female(Pronoun.he()),Verb.none(),DeterminerN.plural(Noun("grandparent")))),
    "She visits her grandparents every month."
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.each(Noun("child")),Verb("receive"),Noun("gift"))),
    "Each child received a gift."
)

sc.setCorpus(
    Phrase.past(Pronoun.give(Noun.eq(Pronoun.he(),Verb.none(),Noun("teacher")),Verb.none(),DeterminerN.each(Noun("student")),Noun("book"))),
    "The teacher gave each student a book."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.female(Pronoun.he()),Verb.add(Verb("look"),Modifier.N2M(DeterminerN.place(DeterminerN.other(Noun.haveP(Noun("side"),Verb.none(),Modifier.N2M(DeterminerN.place(Noun("street")))))))))),
    "She looked at the other side of the street."
)

sc.setCorpus(
    Noun.do(DeterminerN.other(DeterminerN.method(Noun.doT(DeterminerN.plural(Pronoun.I()),Verb("solve"),Noun.eq(Pronoun.proximal(),Verb.none(),Noun("problem"))))),WordV.exist()),
    "There are other ways to solve this problem."
)

sc.setCorpus(
    Noun.do(Noun("book"),Verb.add(WordV.exist(),Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("table")))))),
    "There is a book on this table."
)

sc.setCorpus(
    Noun.do(DeterminerN.plural(Noun("book")),Verb.add(WordV.exist(),Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.proximal(),Verb.none(),Noun("table")))))),
    "There are books on this table."
)

sc.setCorpus(
    Noun.do(DeterminerN.many(DeterminerN.human(Noun.none())),Verb.add(WordV.exist(),Modifier.N2M(DeterminerN.place(Noun("park"))))),
    "There are many people in the park."
)

sc.setCorpus(
    Noun.haveP(Pronoun.I(),Verb.none(),Modifier.add(WordM.good(),Modifier.V2M(Verb("run")))),
    "I am good at running."
)

lang_list_14=LangList.append(LangList.append(LangList(),Noun("apple")),Noun("banana"))
sc.setCorpus(
    LangList.len(lang_list_14),
    "Length of [apple,banana] is 2."
)

lang_list_15=LangList.append(lang_list_14,Noun("peach"))
sc.setCorpus(
    LangList.len(lang_list_15),
    "Length of [apple,banana,peach] is 2."
)

bool_list_01=BoolList.dec2BoolList(23,True)
sc.setCorpus(
    BoolList.len(bool_list_01),
    "Length of binary of 23 is 5."
)

bool_list_02=BoolList.dec2BoolList(1023,True)
sc.setCorpus(
    BoolList.len(bool_list_02),
    "Length of binary of 1023 is 10."
)

number_list_01=NumberList.digit3(Number.one(),Number.two(),Number.three())
sc.setCorpus(
    NumberList.len(number_list_01),
    "Length of 123 is 3."
)

number_list_02=NumberList.digit5(Number.one(),Number.two(),Number.three(),Number.four(),Number.five())
sc.setCorpus(
    NumberList.len(number_list_02),
    "Length of 12345 is 5."
)

index_00=BoolList.twoBit(Bool.false(),Bool.false())
index_01=BoolList.twoBit(Bool.false(),Bool.true())
index_10=BoolList.fourBit(Bool.false(),Bool.false(),Bool.true(),Bool.false())
index_11=BoolList.fourBit(Bool.false(),Bool.false(),Bool.true(),Bool.true())

nl_01=NumberList.digit1(Number.one())
nl_05=NumberList.digit1(Number.five())
nl_10=NumberList.digit2(Number.one(),Number.zero())
nl_11=NumberList.digit2(Number.one(),Number.one())
nl_12=NumberList.digit2(Number.one(),Number.two())
nl_13=NumberList.digit2(Number.one(),Number.three())
nl_14=NumberList.digit2(Number.one(),Number.four())

map_func_item=LangList.get(LangFunc.arg(),index_00)
map_func_index=LangList.get(LangFunc.arg(),index_01)
map_func_all_list=LangList.get(LangFunc.arg(),index_10)

sc.setCorpus(
    LangFunc.setFunc(Noun("map_func_01"),LangList.append(LangList(),NumberList.calcMul(map_func_item,nl_01))),
    "Use the function map_func_01 to add 1 to all elements of the LangList."
)

sc.setCorpus(
    LangFunc.setFunc(Noun("map_func_02"),LangList.append(LangList(),NumberList.calcMul(map_func_item,nl_05))),
    "Use the function map_func_02 to multiply all elements of the LangList by 5."
)

lang_list_16=LangList.append(LangList.append(LangList.append(LangList(),nl_10),nl_11),nl_12)
sc.setCorpus(
    LangList.map(lang_list_16,Noun("map_func_01")),
    "Apply the map_func_01 function to all elements in [10,11,12]."
)

sc.setCorpus(
    LangList.map(lang_list_16,Noun("map_func_02")),
    "Apply the map_func_02 function to all elements in [10,11,12]."
)

lang_list_17=LangList.append(lang_list_16,nl_13)
sc.setCorpus(
    LangList.map(lang_list_17,Noun("map_func_01")),
    "Apply the map_func_01 function to all elements in [10,11,12,13]."
)

sc.setCorpus(
    LangList.map(lang_list_17,Noun("map_func_02")),
    "Apply the map_func_02 function to all elements in [10,11,12,13]."
)

lang_list_18=LangList.append(lang_list_17,nl_14)
sc.setCorpus(
    LangList.map(lang_list_18,Noun("map_func_01")),
    "Apply the map_func_01 function to all elements in [10,11,12,13,14]."
)

sc.setCorpus(
    LangList.map(lang_list_18,Noun("map_func_02")),
    "Apply the map_func_02 function to all elements in [10,11,12,13,14]."
)

def unixTime2SFGPLObj(unix_time_raw:int,N:int=64):
    dtn_ut=int(unix_time_raw*10**9)
    dt_ut=int(unix_time_raw)
    d_ut=int(unix_time_raw/86400)

    dtn_obj=BoolList.UnixTimeDTN(BoolList.hexstr2BoolList(hex(dtn_ut),N))
    dt_obj=BoolList.UnixTimeDT(BoolList.hexstr2BoolList(hex(dt_ut),N))
    d_obj=BoolList.UnixTimeD(BoolList.hexstr2BoolList(hex(d_ut),N))
    
    sc.setCorpus(
        d_obj,
        f"Unix time in day {d_ut} is {d_obj.getData(True)}."
    )

    sc.setCorpus(
        dt_obj,
        f"Unix time in second {dt_ut} is {dt_obj.getData(True)}."
    )

    sc.setCorpus(
        dtn_obj,
        f"Unix time in nano second {dtn_ut} is {dtn_obj.getData(True)}."
    )
    
    return [d_obj,dt_obj,dtn_obj]

unixTime2SFGPLObj(datetime.now().timestamp())

unixTime2SFGPLObj(datetime(2024,9,19,8,38,18,123456,tzinfo=timezone.utc).timestamp())

unixTime2SFGPLObj(datetime(2001,10,7,13,19,0,0,tzinfo=timezone.utc).timestamp())

unixTime2SFGPLObj(-1429029393)

sc.setCorpus(
    Noun.doT(DeterminerN.female(Pronoun.he()),Verb("enjoy"),Noun.V2N(Verb("paint"))),
    "She enjoys painting."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("bus"))),Verb.none(),Modifier.add(Modifier("late"),Modifier("again"))),
    "The bus is late again."
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb("forget"),Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.plural(Noun("key"))))),
    "He forgot his keys."
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb("forget"),Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.plural(Noun("bag"))))),
    "He forgot his bags."
)

sc.setCorpus(
    Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb("forget"),Noun.have(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.plural(Noun("book"))))),
    "He forgot his books."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.progressive(Verb("play")),Noun("basketball")),
    "They are playing basketball."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.progressive(Verb("play")),Noun("baseball")),
    "They are playing baseball."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.progressive(Verb("play")),Noun("football")),
    "They are playing football."
)

sc.setCorpus(
    Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.progressive(Verb("play")),Noun("tennis")),
    "They are playing tennis."
)

sc.setCorpus(
    Pronoun.doT(Pronoun.I(),DeterminerV.Necessary(Verb.none()),Noun.haveP(DeterminerN.time(Noun.none()),Verb.none(),Modifier("more"))),
    "I need more time."
)

sc.setCorpus(
    Noun.do(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("dog"))),Verb.add(Verb.progressive(Verb("bark")),Modifier("loudly"))),
    "The dog is barking loudly."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.I()),Verb.add(Verb("go"),Modifier.AND(Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("beach"))))),Modifier.N2M(DeterminerN.time(Noun("yesterday"))))))),
    "We went to the beach yesterday."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.I()),Verb.add(Verb("go"),Modifier.AND(Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("park"))))),Modifier.N2M(DeterminerN.time(Noun("yesterday"))))))),
    "We went to the park yesterday."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.I()),Verb.add(Verb("go"),Modifier.AND(Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("school"))))),Modifier.N2M(DeterminerN.time(Noun("yesterday"))))))),
    "We went to the school yesterday."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.I()),Verb.add(Verb("go"),Modifier.AND(Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("airport"))))),Modifier.N2M(DeterminerN.time(Noun("yesterday"))))))),
    "We went to the airport yesterday."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.I()),Verb.add(Verb("go"),Modifier.AND(Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("station"))))),Modifier.N2M(DeterminerN.time(Noun("yesterday"))))))),
    "We went to the station yesterday."
)
sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.I()),Verb.add(Verb("go"),Modifier.AND(Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("library"))))),Modifier.N2M(DeterminerN.time(Noun("yesterday"))))))),
    "We went to the library yesterday."
)

sc.setCorpus(
    Phrase.past(Noun.do(DeterminerN.plural(Pronoun.I()),Verb.add(Verb("go"),Modifier.AND(Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun.eq(Noun("store"),Verb.none(),DeterminerN.affect(Noun("book"))))))),Modifier.N2M(DeterminerN.time(Noun("yesterday"))))))),
    "We went to the book store yesterday."
)

sc.setCorpus(
    Noun.doT(DeterminerN.female(Pronoun.he()),Verb("read"),DeterminerN.many(Noun("book"))),
    "She reads a lot of books."
)

sc.setCorpus(
    Noun.haveP(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("food"))),Verb("smell"),Modifier("delicious")),
    "The food smells delicious."
)

sc.setCorpus(
    Noun.doT(DeterminerN.male(Pronoun.he()),Verb.progressive(Verb("learn")),Noun("spanish")),
    "He is learning Spanish."
)

sc.setCorpus(
    Noun.doT(DeterminerN.female(Pronoun.he()),Verb.progressive(Verb("learn")),Noun("spanish")),
    "She is learning Spanish."
)

sc.setCorpus(
    Phrase.past(Noun.haveP(Phrase.past(Noun.doT(Pronoun.I(),Verb("borrow"),DeterminerN.stressed(Noun.eq(Pronoun.he(),Verb.none(),DeterminerN.stressed(Noun("book")))))),Verb.none(),Modifier.Very(Modifier("interesting")))),
    "The book that I borrowed from the library was very interesting."
)

sc.setCorpus(
    Noun.eq(DeterminerN.female(Pronoun.he()),Verb.none(),Phrase.past(Noun.doT(Noun("teacher"),Verb.add(Verb("help"),Modifier.N2M(DeterminerN.affected(DeterminerN.near(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("homework"))))))),Pronoun.I()))),
    "She is the teacher who helped me with my homework."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("buy"),Noun.AND(Pronoun("apple"),Noun("banana")))),
    "I bought an apple and a banana."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("buy"),Noun.AND(Noun.AND(Pronoun("apple"),Noun("banana")),Noun("peach")))),
    "I bought an apple, a banana and a peach."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("buy"),Noun.AND(Noun.AND(Pronoun("apple"),Noun("banana")),Noun.AND(Noun("peach"),Noun("grape"))))),
    "I bought an apple, a banana, a peach and a grape."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("buy"),Noun.AND(Noun.AND(Noun.AND(Pronoun("apple"),Noun("banana")),Noun.AND(Noun("peach"),Noun("grape"))),Noun.AND(Noun("orange"),Noun("melon"))))),
    "I bought an apple, a banana, a peach, a grape, an orange and a melon."
)

sc.setCorpus(
    Phrase.past(Noun.doT(Pronoun.I(),Verb("buy"),Noun.AND(Noun.AND(Noun.AND(Pronoun("apple"),Noun("banana")),Noun.AND(Noun("peach"),Noun("grape"))),Noun.AND(Noun.AND(Noun("orange"),Noun("melon")),Noun.AND(Noun("strawberry"),Noun("lemon")))))),
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon."
)

sub_sentence_12=Phrase.past(Noun.doT(Pronoun.I(),Verb.add(Verb("buy"),Modifier.N2M(Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(Noun.AND(DeterminerN.place(Noun("Tokyo")),DeterminerN.time(Noun.haveP(Noun("year"),Verb.none(),Modifier("last")))))))))),Noun.AND(Noun.AND(Noun.AND(Pronoun("apple"),Noun("banana")),Noun.AND(Noun("peach"),Noun("grape"))),Noun.AND(Noun.AND(Noun("orange"),Noun("melon")),Noun.AND(Noun("strawberry"),Noun("lemon"))))))
sc.setCorpus(
    sub_sentence_12,
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year."
)

sc.setCorpus(
    Noun.AND(sub_sentence_12,Phrase.past(Noun.doT(Pronoun.I(),Verb("eat"),DeterminerN.all(Pronoun.he())))),
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I ate them all."
)

sc.setCorpus(
    Noun.AND(sub_sentence_12,Phrase.past(Noun.doT(Pronoun.I(),Verb("eat"),DeterminerN.all(Pronoun.he())))),
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I ate them all."
)

sub_sentence_13=Noun.AND(sub_sentence_12,Phrase.past(Noun.doT(Noun.AND(Pronoun.I(),Noun("Mary")),Verb("eat"),DeterminerN.all(Pronoun.he()))))
sc.setCorpus(
    sub_sentence_13,
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all."
)

sc.setCorpus(
    Noun.AND(sub_sentence_13,Noun.haveP(DeterminerN.plural(Pronoun.I()),Verb.none(),Modifier("happy"))),
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we are happy."
)

sub_sentence_14=Noun.AND(sub_sentence_13,Phrase.past(Noun.haveP(DeterminerN.plural(Pronoun.I()),Verb.none(),Modifier("happy"))))
sc.setCorpus(
    sub_sentence_14,
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy."
)

sc.setCorpus(
    Noun.But(sub_sentence_14,Noun.Because(Phrase.past(Noun.haveP(Noun("Eric"),Verb.none(),Modifier("sad"))),Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.NOT(DeterminerV.Possible(Verb("eat"))),DeterminerN.plural(Pronoun.he()))))),
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric was sad because he could not eat them."
)

sc.setCorpus(
    Noun.But(sub_sentence_14,Noun.Because(Phrase.past(Noun.haveP(Noun.AND(Noun("Eric"),Noun("Ken")),Verb.none(),Modifier("sad"))),Phrase.past(Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.NOT(DeterminerV.Possible(Verb("eat"))),DeterminerN.plural(Pronoun.he()))))),
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric and Ken were sad because they could not eat them."
)

sc.setCorpus(
    Noun.But(sub_sentence_14,Noun.Because(Phrase.past(Noun.haveP(Noun.AND(Noun.AND(Noun("Eric"),Noun("Ken")),Noun("John")),Verb.none(),Modifier("sad"))),Phrase.past(Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.NOT(DeterminerV.Possible(Verb("eat"))),DeterminerN.plural(Pronoun.he()))))),
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken and John were sad because they could not eat them."
)

sub_sentence_15=Noun.But(sub_sentence_14,Noun.Because(Phrase.past(Noun.haveP(Noun.AND(Noun.AND(Noun("Eric"),Noun("Ken")),Noun.AND(Noun("John"),Noun("Emma"))),Verb.none(),Modifier("sad"))),Phrase.past(Noun.doT(DeterminerN.plural(Pronoun.he()),Verb.NOT(DeterminerV.Possible(Verb("eat"))),DeterminerN.plural(Pronoun.he())))))
sc.setCorpus(
    sub_sentence_15,
    "I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them."
)

sub_sentence_16=Phrase.past(Noun.doT(Noun.have(Noun("Tom"),Verb.none(),DeterminerN.stressed(Noun.eq(Noun("post"),Verb.none(),DeterminerN.affect(Noun("blog"))))),Verb("say"),sub_sentence_15))
sc.setCorpus(
    sub_sentence_16,
    "Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'."
)

sc.setCorpus(
    Noun.hearSay(Pronoun.I(),Verb.none(),sub_sentence_16,Noun("Alice")),
    "According to Alice, I hear, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\"."
)

sc.setCorpus(
    Noun.hearSay(Pronoun.you(),Verb.none(),sub_sentence_16,Noun("Alice")),
    "According to Alice, you hear, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\"."
)

sc.setCorpus(
    Noun.hearSay(Noun("Noah"),Verb.none(),sub_sentence_16,Noun("Alice")),
    "According to Alice, Noah hear, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\"."
)

sc.setCorpus(
    Phrase.past(Noun.hearSay(Pronoun.I(),Verb.none(),sub_sentence_16,Noun("Alice"))),
    "According to Alice, I heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\"."
)

sc.setCorpus(
    Phrase.past(Noun.hearSay(Pronoun.you(),Verb.none(),sub_sentence_16,Noun("Alice"))),
    "According to Alice, you heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\"."
)

sub_sentence_17=Phrase.past(Noun.hearSay(Noun("Noah"),Verb.none(),sub_sentence_16,Noun("Alice")))
sc.setCorpus(
    sub_sentence_17,
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\"."
)

sc.setCorpus(
    Noun.So(sub_sentence_17,Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.NOT(Verb("know")),Pronoun.he()))),
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", so he didn't know it."
)

sc.setCorpus(
    Noun.But(sub_sentence_17,Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.perfective(Verb("know")),Pronoun.he()))),
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it."
)

sc.setCorpus(
    Noun.But(sub_sentence_17,Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.add(Verb.perfective(Verb("know")),Modifier.N2M(DeterminerN.time(Phrase.past(Noun.do(DeterminerN.male(Pronoun.he()),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("school"))))))))))),Pronoun.he()))),
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school."
)

sc.setCorpus(
    Noun.But(sub_sentence_17,Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.add(Verb.perfective(Verb("know")),Modifier.N2M(DeterminerN.time(Phrase.past(Noun.do(DeterminerN.male(Pronoun.he()),Verb.add(Verb("go"),Noun.AND(Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.male(Pronoun.he()),Verb.none(),DeterminerN.stressed(Noun("school"))))),Modifier.N2M(DeterminerN.time(Noun.haveP(Noun("month"),Verb.none(),Modifier("last"))))))))))),DeterminerN.thing(Pronoun.he())))),
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school last month."
)

sub_sentence_18=Noun.But(sub_sentence_17,Phrase.past(Noun.doT(DeterminerN.male(Pronoun.he()),Verb.add(Verb.perfective(Verb("know")),Modifier.N2M(DeterminerN.time(Phrase.past(Noun.do(DeterminerN.male(Pronoun.he()),Verb.add(Verb("go"),Noun.AND(Modifier.N2M(DeterminerN.place(Noun.belong(DeterminerN.male(Pronoun.he()),Verb.add(Verb.none(),Modifier.N2M(DeterminerN.place(Noun("Osaka")))),DeterminerN.stressed(Noun("school"))))),Modifier.N2M(DeterminerN.time(Noun.haveP(Noun("month"),Verb.none(),Modifier("last"))))))))))),DeterminerN.thing(Pronoun.he()))))
sc.setCorpus(
    sub_sentence_18,
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month."
)

sc.setCorpus(
    Noun.AND(sub_sentence_18,Noun.have(Pronoun.I(),Verb.none(),Noun.eq(DeterminerN.thing(Pronoun.he()),Verb.none(),Noun("information")))),
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, I have the information."
)

sc.setCorpus(
    Noun.AND(sub_sentence_18,Noun.have(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("company"))),Verb.none(),Noun.eq(DeterminerN.thing(Pronoun.he()),Verb.none(),Noun("information")))),
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company has the information."
)

sc.setCorpus(
    Noun.AND(sub_sentence_18,Noun.have(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Phrase.past(Noun.do(Noun("company"),Verb.add(Verb("found"),Modifier.N2M(DeterminerN.time(Noun("2010")))))))),Verb.none(),Noun.eq(DeterminerN.thing(Pronoun.he()),Verb.none(),Noun("information")))),
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010, has the information."
)

sub_sentence_19=Noun.AND(sub_sentence_18,Noun.have(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Phrase.past(Noun.do(Noun("company"),Verb.add(Verb("found"),Modifier.AND(Modifier.N2M(DeterminerN.time(Noun("2010"))),Modifier.N2M(DeterminerN.place(Noun("Yokohama"))))))))),Verb.none(),Noun.eq(DeterminerN.thing(Pronoun.he()),Verb.none(),Noun("information"))))
sc.setCorpus(
    sub_sentence_19,
    "According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010 in Yokohama, has the information."
)

sc.setCorpus(
    Noun.give(Pronoun.I(),Verb("tell"),Pronoun.you(),sub_sentence_19),
    "I tell you \'According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010 in Yokohama, has the information.\'."
)

sc.setCorpus(
    Noun.give(Pronoun.I(),Verb("tell"),Noun.AND(Pronoun.you(),Noun("Mike")),sub_sentence_19),
    "I tell you and Mike \'According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010 in Yokohama, has the information.\'."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb("tell"),Noun.AND(Pronoun.you(),Noun("Mike")),sub_sentence_19)),
    "I told you and Mike \'According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010 in Yokohama, has the information.\'."
)

sc.setCorpus(
    Phrase.past(Noun.give(Pronoun.I(),Verb("tell"),Noun.AND(Noun.AND(Pronoun.you(),Noun("Mike")),Noun("Ariel")),sub_sentence_19)),
    "I told you, Mike and Ariel \'According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010 in Yokohama, has the information.\'."
)

sub_sentence_20=Phrase.past(Noun.give(Pronoun.I(),Verb("tell"),Noun.AND(Noun.AND(Pronoun.you(),Noun("Mike")),Noun.AND(Noun("Ariel"),Noun("Ellie"))),sub_sentence_19))
sc.setCorpus(
    sub_sentence_20,
    "I told you, Mike, Ariel and Ellie \'According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010 in Yokohama, has the information.\'."
)

sc.setCorpus(
    Noun.AND(sub_sentence_20,Phrase.past(Noun.haveP(DeterminerN.plural(Pronoun.he()),Verb.none(),Modifier("surprised")))),
    "I told you, Mike, Ariel and Ellie \'According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010 in Yokohama, has the information.\', they were surprised."
)

sc.setCorpus(
    Noun.AND(sub_sentence_20,Phrase.past(Noun.haveP(DeterminerN.plural(Pronoun.he()),Verb.none(),Modifier.V2M(Verb.passive(Verb("surprise")))))),
    "I told you, Mike, Ariel and Ellie \'According to Alice, Noah heard, that \"Tom's blog post said \'I bought an apple, a banana, a peach, a grape, an orange, a melon, a strawberry and lemon, when I went in Tokyo last year, I and Mary ate them all, we were happy, but Eric, Ken, John and Emma were sad because they could not eat them.\'\", but he has know it, when he went to his school in Osaka last month, My company, founded in 2010 in Yokohama, has the information.\', they were surprised."
)

num_1=NumberList.digit1(Number.one())
num_2=NumberList.digit1(Number.two())
num_3=NumberList.digit1(Number.three())
num_5=NumberList.digit1(Number.five())
num_7=NumberList.digit1(Number.seven())
num_13=NumberList.digit2(Number.one(),Number.three())

sc.setCorpus(
    NumberList.calcPow(num_2,num_5),
    "2**5=32"
)

sc.setCorpus(
    NumberList.calcPow(num_5,num_2),
    "5**2=25"
)

sc.setCorpus(
    NumberList.calcIntDiv(num_5,num_2),
    "5//2=2"
)

sc.setCorpus(
    NumberList.calcMod(num_5,num_2),
    "5%2=1"
)

sc.setCorpus(
    NumberList.calcIntDiv(num_7,num_2),
    "7//2=3"
)

sc.setCorpus(
    NumberList.calcMod(num_7,num_2),
    "7%2=1"
)

num_1_per_3=NumberList.calcDiv(num_1,num_3)
sc.setCorpus(
    num_1_per_3,
    "1/3=0.3333..."
)

sc.setCorpus(
    NumberList.FloatNL2BL(num_1_per_3),
    "1/3 in BoolList."
)

sc.setCorpus(
    BoolList.FloatBL2NL(NumberList.FloatNL2BL(num_1_per_3)),
    "1/3 represented by BoolList back to NumberList."
)

num_1_per_7=NumberList.calcDiv(num_1,num_7)
sc.setCorpus(
    num_1_per_7,
    "1/7=0.14285..."
)

sc.setCorpus(
    NumberList.FloatNL2BL(num_1_per_3),
    "1/7 in BoolList."
)

sc.setCorpus(
    BoolList.FloatBL2NL(NumberList.FloatNL2BL(num_1_per_3)),
    "1/7 represented by BoolList back to NumberList."
)

tmp_str=sc.toStringSFGPL(opt_str="\n")
print(tmp_str)

sc.saveJson(OUT_DIR+"sample01.json")
sc.saveTextFileOfSFGPL(OUT_DIR+"sample01.txt",opt_str="\n")
sc.saveCSV(OUT_DIR+"sample01.csv")

#Clear defined functions
LangFunc.clearDict()
LangVar.clearDict()

json_obj=SFGPLCorpus.readJson(OUT_DIR+"sample01.json")
#print(len(json_obj))
#print(json_obj)
