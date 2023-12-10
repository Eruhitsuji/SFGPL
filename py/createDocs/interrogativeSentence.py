from createDocs import *

NAME="interrogativeSentence"

format_str_list={
    "phrase_interrogative":LangObj._getKeyOfDict("Phrase.interrogative"),
    "you_have_a_table":Noun.have(Pronoun.you(),Verb.none(),Noun("table")),
    "do_you_have_a_table":Phrase.interrogative(Noun.have(Pronoun.you(),Verb.none(),Noun("table"))),
    "you":Pronoun.you(),
    "table":Noun("table"),
    
    "pronoun_interrogative":LangObj._getKeyOfDict("Pronoun.interrogative"),
    "who_has_a_table":Phrase.interrogative(Noun.have(DeterminerN.human(Pronoun.interrogative()),Verb.none(),Noun("table"))),
    "what_do_you_have":Phrase.interrogative(Noun.have(Pronoun.you(),Verb.none(),DeterminerN.thing(Pronoun.interrogative()))),
    "who":DeterminerN.human(Pronoun.interrogative()),
    "what":DeterminerN.thing(Pronoun.interrogative()),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
