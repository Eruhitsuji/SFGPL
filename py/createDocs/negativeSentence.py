from createDocs import *

NAME="negativeSentence"

format_str_list={
    "langobj_not":LangObj._getKeyOfDict("LangObj.NOT"),
    "I_have_a_table":Noun.have(Pronoun.I(),Verb.none(),Noun("table")),
    "I_don't_have_a_table":Phrase.NOT(Noun.have(Pronoun.I(),Verb.none(),Noun("table"))),
    "I":Pronoun.I(),
    "table":Noun("table"),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
