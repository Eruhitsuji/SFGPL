from createDocs import *

NAME="detailedGrammar"

def multiWord(l):
    return " ".join(l)

n2m=LangObj._getKeyOfDict("Modifier.N2M")

format_str_list={
    "verb_add":LangObj._getKeyOfDict("Verb.add"),
    "noun_havep":LangObj._getKeyOfDict("Noun.haveP"),
    "I_go_to_Tokyo_1":Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun("Tokyo"))))),
    "I_go_to_Tokyo_2":Noun.haveP(Noun.do(Pronoun.I(),Verb("go")),Verb.none(),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))),

    "I":Pronoun.I(),
    "go":Verb("go"),
    "to_tokyo":Modifier.N2M(DeterminerN.place(Noun("Tokyo"))),
    
    "modifier_n2m":n2m,

    "pre_time":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.time")]),
    "pre_place":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.place")]),
    "pre_reason":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.reason")]),
    "pre_way":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.method")]),
    "pre_start":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.start")]),
    "pre_end":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.end")]),
    "pre_section":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.section")]),
    "pre_in":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.In")]),
    "pre_into":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.move"),LangObj._getKeyOfDict("DeterminerN.In")]),
    "pre_out":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.Out")]),
    "pre_up":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.move"),LangObj._getKeyOfDict("DeterminerN.above")]),
    "pre_above":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.above")]),
    "pre_down":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.move"),LangObj._getKeyOfDict("DeterminerN.below")]),
    "pre_under":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.on"),LangObj._getKeyOfDict("DeterminerN.below")]),
    "pre_below":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.below")]),
    "pre_on":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.on")]),
    "pre_right":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.right")]),
    "pre_left":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.left")]),
    "pre_near":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.near")]),
    "pre_by":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.affect"),LangObj._getKeyOfDict("DeterminerN.near")]),
    "pre_with":multiWord([n2m,LangObj._getKeyOfDict("DeterminerN.affected"),LangObj._getKeyOfDict("DeterminerN.near")]),
    
    
    

}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
