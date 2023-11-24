from createDocs import *

NAME="pronoun"

format_str_list={
    "pronoun_I":Pronoun.I(),
    "pronoun_you":Pronoun.you(),
    "pronoun_he":Pronoun.he(),
    "pronoun_proximal":Pronoun.proximal(),
    "pronoun_distal":Pronoun.distal(),
    "pronoun_interrogative":Pronoun.interrogative(),
    "pronoun_indefinite":Pronoun.indefinite(),
    "determinerN_plural":LangObj._getKeyOfDict("DeterminerN.plural"),
    
    "pronoun_we":DeterminerN.plural(Pronoun.I()),
    "pronoun_what":DeterminerN.thing(Pronoun.interrogative()),
    "pronoun_who":DeterminerN.human(Pronoun.interrogative()),
    "pronoun_when":DeterminerN.time(Pronoun.interrogative()),
    "pronoun_where":DeterminerN.place(Pronoun.interrogative()),
    "pronoun_why":DeterminerN.reason(Pronoun.interrogative()),
    "pronoun_how":DeterminerN.method(Pronoun.interrogative()),
    
    "pronoun_he_male":DeterminerN.male(Pronoun.he()),
    "pronoun_he_female":DeterminerN.female(Pronoun.he()),
    "pronoun_he_thing":DeterminerN.thing(Pronoun.he()),

    "determinerN_possessive":LangObj._getKeyOfDict("DeterminerN.possessive"),
    "determinerN_reflexive":LangObj._getKeyOfDict("DeterminerN.reflexive"),
    "mine":DeterminerN.possessive(Pronoun.I()),
    "myself":DeterminerN.reflexive(Pronoun.I()),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
