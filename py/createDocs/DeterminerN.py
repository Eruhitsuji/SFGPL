from createDocs import *

NAME="DeterminerN"

format_str_list={
    "N2M":LangObj._getKeyOfDict("Modifier.N2M"),
    
    "determinerN_male":LangObj._getKeyOfDict("DeterminerN.male"),
    "determinerN_female":LangObj._getKeyOfDict("DeterminerN.female"),
    "determinerN_plural":LangObj._getKeyOfDict("DeterminerN.plural"),
    "determinerN_place":LangObj._getKeyOfDict("DeterminerN.place"),
    "determinerN_time":LangObj._getKeyOfDict("DeterminerN.time"),
    "determinerN_father":LangObj._getKeyOfDict("DeterminerN.father"),

    "He_is_student":Noun.eq(DeterminerN.male(Pronoun.he()),Verb.none(),Noun("student")),
    "She_is_student":Noun.eq(DeterminerN.female(Pronoun.he()),Verb.none(),Noun("student")),
    "They_are_student":Noun.eq(DeterminerN.plural(Pronoun.he()),Verb.none(),Noun("student")),
    "I_go_to_Tokyo":Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "I_go_today":Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.time(Noun("today"))))),

    "pronoun_he":Pronoun.he(),
    "student":Noun("student"),
    "I":Pronoun.I(),
    "go":Verb("go"),
    "Tokyo":Noun("Tokyo"),
    "today":Noun("today")
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
