from createDocs import *

FILE_NAME="Modifier.md"

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

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)