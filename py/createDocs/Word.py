from createDocs import *

FILE_NAME="Word.md"

format_str_list={
    "noun_apple":Noun("apple"),
    "verb_open":Verb("open"),
    "modifier_tall":Modifier("tall"),
    "create":WordV.create(),
    "big":WordM.big(),
    "I_have_an_apple":Noun.have(Pronoun.I(),Verb.none(),Noun("apple")),
    "I_open_a_door":Noun.doT(Pronoun.I(),Verb("open"),Noun("door")),
    "I_am_tall":Noun.haveP(Pronoun.I(),Verb.none(),Modifier("tall")),
    "I_create_a_door":Noun.doT(Pronoun.I(),WordV.create(),Noun("door")),
    "the_apple_is_big":Noun.haveP(Noun("apple"),Verb.none(),WordM.big()),
    "noun_none":LangObj._getKeyOfDict("Noun.none"),
    "human":DeterminerN.human(Noun.none()),
    "I_am_human":Noun.eq(Pronoun.I(),Verb.none(),DeterminerN.human(Noun.none())),
    "verb_none":LangObj._getKeyOfDict("Verb.none"),
    "modifier_none":LangObj._getKeyOfDict("Modifier.none"),

}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)