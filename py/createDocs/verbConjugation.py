from createDocs import *

NAME="verbConjugation"

format_str_list={
    "I_lived_in_Tokyo":Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))),
    "I_live_in_Tokyo":Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "I_will_live_in_Tokyo":Phrase.future(Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))),
    "phrase_past":LangObj._getKeyOfDict("Phrase.past"),
    "phrase_future":LangObj._getKeyOfDict("Phrase.future"),
    "determinerV_past":LangObj._getKeyOfDict("DeterminerV.past"),
    "determinerV_present":LangObj._getKeyOfDict("DeterminerV.present"),
    "determinerV_future":LangObj._getKeyOfDict("DeterminerV.future"),
    "I_would_live_in_Tokyo":Phrase.future(Noun.do(Pronoun.I(),Verb.add(DeterminerV.past(Verb("live")),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))),

    "I_had_lived_in_Tokyo":Phrase.past(Noun.do(Pronoun.I(),Verb.perfective(Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))))),
    "I_have_lived_in_Tokyo":Noun.do(Pronoun.I(),Verb.perfective(Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))),
    "I_will_have_lived_in_Tokyo":Phrase.future(Noun.do(Pronoun.I(),Verb.perfective(Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))))),
    "verb_perfective":LangObj._getKeyOfDict("Verb.perfective"),

    "I_am_wearing_the_dress":Noun.doT(Pronoun.I(),Verb.progressive(Verb("wear")),Noun("dress")),
    "verb_progressive":LangObj._getKeyOfDict("Verb.progressive"),
    "I_was_wearing_the_dress":Phrase.past(Noun.doT(Pronoun.I(),Verb.progressive(Verb("wear")),Noun("dress"))),
    "I_will_be_wearing_the_dress":Phrase.future(Noun.doT(Pronoun.I(),Verb.progressive(Verb("wear")),Noun("dress"))),

    "verb_start":LangObj._getKeyOfDict("DeterminerV.Start"),
    "verb_condition":LangObj._getKeyOfDict("DeterminerV.Condition"),
    "verb_complete":LangObj._getKeyOfDict("DeterminerV.Complete"),
    "verb_continue":LangObj._getKeyOfDict("DeterminerV.Continue"),
    "verb_end":LangObj._getKeyOfDict("DeterminerV.End"),
    "verb_progressive":LangObj._getKeyOfDict("Verb.progressive"),

    "I_wear_a_dress":Noun.doT(Pronoun.I(),Verb("wear"),Noun("dress")),
    "I_begin_wear_a_dress":Noun.doT(Pronoun.I(),DeterminerV.Start(Verb("wear")),Noun("dress")),
    "I_am_in_the_process_of_wearing_a_dress":Noun.doT(Pronoun.I(),DeterminerV.Condition(Verb("wear")),Noun("dress")),
    "I_wear_a_dress_complete":Noun.doT(Pronoun.I(),DeterminerV.Complete(Verb("wear")),Noun("dress")),
    "I_am_wearing_a_dress_continue":Noun.doT(Pronoun.I(),DeterminerV.Continue(Verb("wear")),Noun("dress")),
    "I_finish_wear_a_dress":Noun.doT(Pronoun.I(),DeterminerV.End(Verb("wear")),Noun("dress")),
    "I_am_wearing_a_dress":Noun.doT(Pronoun.I(),Verb.progressive(Verb("wear")),Noun("dress")),
    "I_began_wear_a_dress":Phrase.past(Noun.doT(Pronoun.I(),DeterminerV.Start(Verb("wear")),Noun("dress"))),
    "I_began_will_begin_a_dress":Phrase.future(Noun.doT(Pronoun.I(),DeterminerV.Start(Verb("wear")),Noun("dress"))),
    "I_have_been_wearing_a_dress":Noun.doT(Pronoun.I(),Verb.perfective(Verb.progressive(Verb("wear"))),Noun("dress")),    

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

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
