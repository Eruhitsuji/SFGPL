from createDocs import *

NAME="Modifier"

format_str_list={
    "WordM_big":WordM.big(),
    "Neg_WordM_big":Modifier.Neg(WordM.big()),
    "Modifier_N":LangObj._getKeyOfDict("Noun.haveP"),
    "Modifier_V":LangObj._getKeyOfDict("Verb.add"),
    "Modifier_M":LangObj._getKeyOfDict("Modifier.add"),
    "Noun_gt":LangObj._getKeyOfDict("Noun.gt"),


    "Modifier_N2M":LangObj._getKeyOfDict("Modifier.N2M"),
    "I_live_in_Tokyo":Noun.do(Pronoun.I(),Verb.add(Verb("live"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "DeterminerN_place":LangObj._getKeyOfDict("DeterminerN.place"),
    
    "I":Pronoun.I(),
    "live":Verb("live"),
    "in_Tokyo":Modifier.N2M(DeterminerN.place(Noun("Tokyo"))),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
