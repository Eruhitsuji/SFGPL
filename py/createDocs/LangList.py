from createDocs import *

FILE_NAME="LangList.md"

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

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)