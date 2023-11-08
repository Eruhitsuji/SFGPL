from createDocs import *

FILE_NAME="verbConjugation.md"

format_str_list={
    "I_lived_in_Tokyo":Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))),
    "I_live_in_Tokyo":Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "I_will_live_in_Tokyo":Phrase.future(Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))),
    "phrase_past":LangObj._getKeyOfDict("Phrase.past"),
    "phrase_future":LangObj._getKeyOfDict("Phrase.future"),
    
    "I_had_lived_in_Tokyo":Phrase.past(Noun.do(Pronoun.I(),Verb.perfective(Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))))),
    "I_have_lived_in_Tokyo":Noun.do(Pronoun.I(),Verb.perfective(Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))),
    "I_will_have_lived_in_Tokyo":Phrase.future(Noun.do(Pronoun.I(),Verb.perfective(Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))))),
    "verb_perfective":LangObj._getKeyOfDict("Verb.perfective"),

    "I_am_wearing_the_dress":Noun.doT(Pronoun.I(),Verb.progressive(Verb("wear")),Noun("dress")),
    "verb_progressive":LangObj._getKeyOfDict("Verb.progressive"),
    "I_was_wearing_the_dress":Phrase.past(Noun.doT(Pronoun.I(),Verb.progressive(Verb("wear")),Noun("dress"))),
    "I_will_be_wearing_the_dress":Phrase.future(Noun.doT(Pronoun.I(),Verb.progressive(Verb("wear")),Noun("dress"))),


    "the_dress_is_worn":Noun.do(Noun("dress"),Verb.passive(Verb("wear"))),
    "verb_passive":LangObj._getKeyOfDict("Verb.passive"),
    "the_dress_was_worn":Phrase.past(Noun.do(Noun("dress"),Verb.passive(Verb("wear")))),
    "the_dress_will_be_worn":Phrase.future(Noun.do(Noun("dress"),Verb.passive(Verb("wear")))),
    
    "I":Pronoun.I(),
    "live":Verb("live"),
    "in_Tokyo":Modifier.N2M(DeterminerN.place(Noun("Tokyo"))),
    "wear":Verb("wear"),
    "dress":Noun("dress"),
}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)