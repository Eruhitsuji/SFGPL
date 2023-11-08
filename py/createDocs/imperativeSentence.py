from createDocs import *

FILE_NAME="imperativeSentence.md"

format_str_list={
    "phrase_imperative":LangObj._getKeyOfDict("Phrase.imperative"),
    "you_buy_a_table":Noun.doT(Pronoun.you(),Verb("buy"),Noun("table")),
    "buy_a_table_you":Phrase.imperative(Noun.doT(Pronoun.you(),Verb("buy"),Noun("table"))),
    "you":Pronoun.you(),
    "buy":Verb("buy"),
    "table":Noun("table"),
}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)