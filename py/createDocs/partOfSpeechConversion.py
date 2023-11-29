from createDocs import *

NAME="partOfSpeechConversion"

format_str_list={
    "V2N":LangObj._getKeyOfDict("Noun.V2N"),
    "M2N":LangObj._getKeyOfDict("Noun.M2N"),
    "M2V":LangObj._getKeyOfDict("Verb.M2V"),
    "N2V":LangObj._getKeyOfDict("Verb.N2V"),
    "N2M":LangObj._getKeyOfDict("Modifier.N2M"),
    "V2M":LangObj._getKeyOfDict("Modifier.V2M"),
    
    "this_is_building":Noun.eq(Pronoun.proximal(),Verb.none(),Noun.V2N(Verb("build"))),
    "this":Pronoun.proximal(),
    "build":Verb("build"),

    "I_live_in_Tokyo":Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "determinerN_place":LangObj._getKeyOfDict("DeterminerN.place"),
    "I":Pronoun.I(),
    "live":Verb("live"),
    "in_Tokyo":Modifier.N2M(DeterminerN.place(Noun("Tokyo"))),
    
    "determinerN_abstract":LangObj._getKeyOfDict("DeterminerN.abstract"),
    "my_daughter_has_a_cat_like_stuffed_toy":Noun.have(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("daughter"))),Verb.none(),Noun.haveP(Noun.haveP(Noun("toy"),Verb.none(),Modifier.V2M(Verb.passive(Verb("stuff")))),Verb.none(),Modifier.N2M(DeterminerN.abstract(Noun("cat"))))),
    "daughter":Noun("daughter"),
    "cat":Noun("cat"),
    "stuffed":Modifier.V2M(Verb.passive(Verb("stuff"))),
    "toy":Noun("toy"),

    "there_is_a_sleeping_boy":Noun.eq(DeterminerN.place(Pronoun.distal()),Verb.none(),Noun.haveP(Noun("boy"),Verb.none(),Modifier.V2M(Verb.progressive(Verb("sleep"))))),
    "there":DeterminerN.place(Pronoun.distal()),
    "sleep":Verb("sleep"),
    "boy":Noun("boy"),

    "I_lived_in_that_destroyed_building":Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun.eq(Pronoun.distal(),Verb.none(),DeterminerN.stressed(Noun.haveP(Noun.V2N(Verb("build")),Verb.none(),Modifier.V2M(Verb.passive(Verb("destroy"))))))))))),
    "that":Pronoun.distal(),
    "destroy":Verb("destroy"),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
