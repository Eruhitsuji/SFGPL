from createDocs import *

FILE_NAME="aboutSFGPL.md"

format_str_list={
    "noun_do":LangObj._getKeyOfDict("Noun.do"),
    "noun_eq":LangObj._getKeyOfDict("Noun.eq"),
    "noun_haveP":LangObj._getKeyOfDict("Noun.haveP"),
    "noun_doT":LangObj._getKeyOfDict("Noun.doT"),
    "noun_give":LangObj._getKeyOfDict("Noun.give"),
    "noun_makeN":LangObj._getKeyOfDict("Noun.makeN"),
    "noun_makeM":LangObj._getKeyOfDict("Noun.makeM"),
    "noun_have":LangObj._getKeyOfDict("Noun.have"),
    "noun_belong":LangObj._getKeyOfDict("Noun.belong"),
    "noun_gt":LangObj._getKeyOfDict("Noun.gt"),
}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)