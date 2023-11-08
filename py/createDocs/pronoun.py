from createDocs import *

FILE_NAME="pronoun.md"

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

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)