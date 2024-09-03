from createDocs import *

NAME="Word"

format_str_list={
    "noun_apple":Noun("apple"),
    "verb_open":Verb("open"),
    "modifier_tall":Modifier("tall"),
    "create":WordV.create(),
    "big":WordM.big(),
    "I_have_an_apple":Noun.have(Pronoun.I(),Verb.none(),Noun("apple")),
    "I_open_a_door":Noun.doT(Pronoun.I(),Verb("open"),Noun("door")),
    "I_am_tall":Noun.haveP(Pronoun.I(),Verb.none(),Modifier("tall")),

    "language_en":Noun("language"),
    "language_ja":Noun("言語"),
    "language_zh-Hans":Noun("语言"),
    "language_zh-Hant":Noun("語言"),
    "language_hi":Noun("भाषा"),
    "language_es":Noun("idioma"),
    "language_ar":Noun("لغة"),
    "language_bn":Noun("ভাষা"),
    "language_fr":Noun("langue"),
    "language_ru":Noun("язык"),
    "language_pt":Noun("linguagem"),
    "language_ur":Noun("زبان"),
    "language_id":Noun("bahasa"),
    "language_de":Noun("Sprache"),
    "language_eo":Noun("lingvo"),

    "Noun_borrowed":LangObj._getKeyOfDict("Noun.borrowed"),
    "Verb_borrowed":LangObj._getKeyOfDict("Verb.borrowed"),
    "Modifier_borrowed":LangObj._getKeyOfDict("Modifier.borrowed"),

    "language_English_borrowed":Noun.borrowed("language","English"),
    "go_English_borrowed":Verb.borrowed("go","English"),
    "big_English_borrowed":Modifier.borrowed("big","English"),

    "I_create_a_door":Noun.doT(Pronoun.I(),WordV.create(),Noun("door")),
    "the_apple_is_big":Noun.haveP(Noun("apple"),Verb.none(),WordM.big()),
    "noun_none":LangObj._getKeyOfDict("Noun.none"),
    "human":DeterminerN.human(Noun.none()),
    "I_am_human":Noun.eq(Pronoun.I(),Verb.none(),DeterminerN.human(Noun.none())),
    "verb_none":LangObj._getKeyOfDict("Verb.none"),
    "modifier_none":LangObj._getKeyOfDict("Modifier.none"),

    "pronoun_I":Pronoun.I(),
    "pronoun_you":Pronoun.you(),
    "pronoun_he":Pronoun.he(),
    "pronoun_proximal":Pronoun.proximal(),
    "pronoun_distal":Pronoun.distal(),
    "pronoun_interrogative":Pronoun.interrogative(),
    "pronoun_indefinite":Pronoun.indefinite(),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
