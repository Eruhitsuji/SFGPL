from createDocs import *

NAME="imperativeSentence"

format_str_list={
    "phrase_imperative":LangObj._getKeyOfDict("Phrase.imperative"),
    "you_buy_a_table":Noun.doT(Pronoun.you(),Verb("buy"),Noun("table")),
    "buy_a_table_you":Phrase.imperative(Noun.doT(Pronoun.you(),Verb("buy"),Noun("table"))),
    "you":Pronoun.you(),
    "buy":Verb("buy"),
    "table":Noun("table"),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
