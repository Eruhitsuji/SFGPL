import sys
sys.path.append("")

from SFGPL import *
import os

OUT_DIR="out/"

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
b3_3=BoolList.Float(b2)#-1024.25

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



tmp_str=sc.toStringSFGPL(opt_str="\n")
print(tmp_str)

sc.saveJson(OUT_DIR+"sample01.json")
sc.saveTextFileOfSFGPL(OUT_DIR+"sample01.txt",opt_str="\n")
sc.saveCSV(OUT_DIR+"sample01.csv")
json_obj=SFGPLCorpus.readJson(OUT_DIR+"sample01.json")
#print(len(json_obj))
#print(json_obj)