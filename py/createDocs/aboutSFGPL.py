from createDocs import *

NAME="aboutSFGPL"

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
    "noun_hearSay":LangObj._getKeyOfDict("Noun.hearSay"),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
