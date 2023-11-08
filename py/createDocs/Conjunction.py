from createDocs import *

FILE_NAME="Conjunction.md"

s1=Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun("store")))))
s1_not=LangObj.NOT(s1)
s2=Noun.doT(Pronoun.I(),Verb("want"),DeterminerN.thing(Pronoun.he()))
s3=Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun("library")))))

format_str_list={
    "word_because":LangObj._getKeyOfDict("LangObj.Because"),
    "word_so":LangObj._getKeyOfDict("LangObj.So"),
    "word_if":LangObj._getKeyOfDict("LangObj.IF"),
    "word_but":LangObj._getKeyOfDict("LangObj.But"),
    "word_and":LangObj._getKeyOfDict("LangObj.AND"),
    "word_or":LangObj._getKeyOfDict("LangObj.OR"),

    "s1_because_s2":LangObj.Because(s1,s2),
    "s2_so_s1":LangObj.So(s2,s1),
    "s1_if_s2":LangObj.IF(s1,s2),
    "s2_but_s1_not":LangObj.But(s2,s1_not),
    "s1_and_s3":LangObj.AND(s1,s3),
    "s1_or_s3":LangObj.OR(s1,s3),

    "store_and_library":LangObj.AND(Noun("store"),Noun("library")),
    "store_or_library":LangObj.OR(Noun("store"),Noun("library")),

    "I_go_to_a_store":s1,
    "I_don't_go_to_a_store":s1_not,
    "I_want_it":s2,
    "I_go_to_a_library":s3,
    "store":Noun("store"),
    "library":Noun("library"),
}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)