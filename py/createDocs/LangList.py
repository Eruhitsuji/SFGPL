from createDocs import *

NAME="LangList"

I_am_a_student=Noun.eq(Pronoun.I(),Verb.none(),Noun("student"))

lang_list_01=LangList.append(LangList.append(LangList.append(LangList.append(LangList.append(LangList(),Pronoun.I()),Noun("pen")),Verb("go")),Modifier("happy")),I_am_a_student)

number_0=BoolList.hex2BoolList(0)

format_str_list={
    "LangList":LangObj._getKeyOfDict("LangList"), 
    "LangList_get":LangObj._getKeyOfDict("LangList.get"), 
    "LangList_append":LangObj._getKeyOfDict("LangList.append"), 
    "LangList_slice":LangObj._getKeyOfDict("LangList.slice"), 
    "LangList_add":LangObj._getKeyOfDict("LangList.add"),
    
    "lang_list_01":lang_list_01,
    "lang_list_01_get_0":LangList.get(lang_list_01,number_0),

    "number_0":number_0,

    "I":Pronoun.I(),
    "pen":Noun("pen"),
    "go":Verb("go"),
    "happy":Modifier("happy"),
    "I_am_a_student":I_am_a_student,
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
