from createDocs import *

NAME="DeterminerV"

format_str_list={
    "determinerV_possible":LangObj._getKeyOfDict("DeterminerV.Possible"),
    "determinerV_ability":LangObj._getKeyOfDict("DeterminerV.Ability"),
    "determinerV_obligation":LangObj._getKeyOfDict("DeterminerV.Obligation"),
    "determinerV_necessary":LangObj._getKeyOfDict("DeterminerV.Necessary"),
    "determinerV_duty":LangObj._getKeyOfDict("DeterminerV.Duty"),
    "determinerV_want":LangObj._getKeyOfDict("DeterminerV.want"),

    "I_can_see_a_sea":Noun.doT(Pronoun.I(),DeterminerV.Possible(Verb("see")),Noun("sea")),
    "I_can_swim":Noun.do(Pronoun.I(),DeterminerV.Ability(Verb("swim"))),
    "I_should_swim":Noun.do(Pronoun.I(),DeterminerV.Obligation(Verb("swim"))),
    "I_need_to_swim":Noun.do(Pronoun.I(),DeterminerV.Necessary(Verb("swim"))),
    "I_must_swim":Noun.do(Pronoun.I(),DeterminerV.Duty(Verb("swim"))),
    "I_want_to_swim":Noun.do(Pronoun.I(),DeterminerV.want(Verb("swim"))),

    "I":Pronoun.I(),
    "see":Verb("see"),
    "sea":Noun("sea"),
    "swim":Verb("swim"),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
