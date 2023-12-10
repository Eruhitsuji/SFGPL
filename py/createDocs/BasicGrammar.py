from createDocs import *

NAME="BasicGrammar"


format_str_list={
    "noun_do":LangObj._getKeyOfDict("Noun.do"),
    "I_run":Noun.do(Pronoun.I(),Verb("run")),
    "I":Pronoun.I(),
    "run":Verb("run"),
    "noun_init":LangObj._getKeyOfDict("Noun"),
    "verb_init":LangObj._getKeyOfDict("Verb"),
    "modifier_init":LangObj._getKeyOfDict("Modifier"),

    "noun_eq":LangObj._getKeyOfDict("Noun.eq"),
    "I_am_a_student":Noun.eq(Pronoun.I(),Verb.none(),Noun("student")),
    "verb_none":Verb.none(),
    "student":Noun("student"),

    "noun_haveP":LangObj._getKeyOfDict("Noun.haveP"),
    "I_am_happy":Noun.haveP(Pronoun.I(),Verb.none(),Modifier("happy")),
    "happy":Modifier("happy"),

    "noun_doT":LangObj._getKeyOfDict("Noun.doT"),
    "I_open_the_door":Noun.doT(Pronoun.I(),Verb("open"),Noun("door")),
    "open":Verb("open"),
    "door":Noun("door"),

    "noun_give":LangObj._getKeyOfDict("Noun.give"),
    "I_give_you_a_box":Noun.give(Pronoun.I(),Verb.none(),Pronoun.you(),Noun("box")),
    "you":Pronoun.you(),
    "box":Noun("box"),

    "noun_makeN":LangObj._getKeyOfDict("Noun.makeN"),
    "I_make_you_a_teacher":Noun.makeN(Pronoun.I(),Verb.none(),Pronoun.you(),Noun("teacher")),
    "teacher":Noun("teacher"),

    "noun_makeM":LangObj._getKeyOfDict("Noun.makeM"),
    "I_make_you_happy":Noun.makeM(Pronoun.I(),Verb.none(),Pronoun.you(),Modifier("happy")),

    "noun_have":LangObj._getKeyOfDict("Noun.have"),
    "I_have_a_box":Noun.have(Pronoun.I(),Verb.none(),Noun("box")),

    "noun_belong":LangObj._getKeyOfDict("Noun.belong"),
    "I_belong_to_a_school":Noun.belong(Pronoun.I(),Verb.none(),Noun("school")),
    "school":Noun("school"),

    "the_box_is_big":Noun.haveP(Noun("box"),Verb.none(),WordM.big()),
    "big":WordM.big(),

    "my_box_is_big":Noun.haveP(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("box"))),Verb.none(),WordM.big()),
    "I_have_a___box_":Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("box"))),
    "determinerN_stressed":LangObj._getKeyOfDict("DeterminerN.stressed"),
    "stressed_box":DeterminerN.stressed(Noun("box")),

    "verb_add":LangObj._getKeyOfDict("Verb.add"),
    "I_quickly_run":Noun.do(Pronoun.I(),Verb.add(Verb("run"),Modifier("quickly"))),
    "quickly":Modifier("quickly"),
    "run_quickly":Verb.add(Verb("run"),Modifier("quickly")),

    "modifier_N2M":LangObj._getKeyOfDict("Modifier.N2M"),
    "I_go_to_Tokyo":Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "go":Verb("go"),
    "to_Tokyo":Modifier.N2M(DeterminerN.place(Noun("Tokyo"))),
    "determinerN_place":LangObj._getKeyOfDict("DeterminerN.place"),
    "Tokyo":Noun("Tokyo"),

    "modifier_add":LangObj._getKeyOfDict("Modifier.add"),
    "Your_box_is_a_little_big":Noun.haveP(Noun.have(Pronoun.you(),Verb.none(),DeterminerN.stressed(Noun("box"))),Verb.none(),Modifier.add(WordM.big(),Modifier("little"))),
    "a_little_big":Modifier.add(WordM.big(),Modifier("little")),
    "a_little":Modifier("little"),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
