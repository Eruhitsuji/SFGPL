from createDocs import *

NAME="otherLang"

format_str_list={
    "私はりんごを持っている":Noun.have(Pronoun.I(),Verb.none(),Noun("りんご")),
    "私の鞄は赤い":Noun.haveP(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("鞄"))),Verb.none(),Modifier("赤い")),

    "mi_havas_pomon":Noun.have(Pronoun.I(),Verb.none(),Noun("pom")),
    "mia_sako_estas_ruĝa":Noun.haveP(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("sak"))),Verb.none(),Modifier("ruĝ")),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
