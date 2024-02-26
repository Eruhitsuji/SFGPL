from createDocs import *

NAME="negativeSentence"

format_str_list={
    "langobj_not":LangObj._getKeyOfDict("LangObj.NOT"),
    "I_have_a_table":Noun.have(Pronoun.I(),Verb.none(),Noun("table")),
    "I_don't_have_a_table":Phrase.NOT(Noun.have(Pronoun.I(),Verb.none(),Noun("table"))),
    "I":Pronoun.I(),
    "table":Noun("table"),

    "a_I_don't_make_a_table":Phrase.NOT(Noun.doT(Pronoun.I(),Verb("make"),Noun("table"))),
    "v_I_don't_make_a_table":Noun.doT(Pronoun.I(),Verb.NOT(Verb("make")),Noun("table")),
    "make":Verb("make"),

    "a_I_didn't_ran_my_school":Phrase.past(Phrase.NOT(Noun.do(Pronoun.I(),Verb.add(Verb("run"),Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))))))))),
    "v_I_didn't_ran_my_school":Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb.NOT(Verb("run")),Modifier.N2M(DeterminerN.place(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school")))))))),
    "run":Verb("run"),
    "my_school":Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))),

    "modifier_neg":LangObj._getKeyOfDict("Modifier.Neg"),
    "big":WordM.big(),
    "neg_big":Modifier.Neg(WordM.big()),
    "my_table_is_small":Noun.haveP(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("table"))),Verb.none(),Modifier.Neg(WordM.big()))
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
