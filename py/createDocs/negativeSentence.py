from createDocs import *

FILE_NAME="negativeSentence.md"

format_str_list={
    "langobj_not":LangObj._getKeyOfDict("LangObj.NOT"),
    "I_have_a_table":Noun.have(Pronoun.I(),Verb.none(),Noun("table")),
    "I_don't_have_a_table":Phrase.NOT(Noun.have(Pronoun.I(),Verb.none(),Noun("table"))),
    "I":Pronoun.I(),
    "table":Noun("table"),
}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)