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
    "I_live_in_Tokyo":Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "determinerN_place":LangObj._getKeyOfDict("DeterminerN.place"),
    "this":Pronoun.proximal(),
    "building":Noun.V2N(Verb("build")),
    "I":Pronoun.I(),
    "live":Verb("live"),
    "in_Tokyo":Modifier.N2M(DeterminerN.place(Noun("Tokyo"))),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
