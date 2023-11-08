from createDocs import *

FILE_NAME="interrogativeSentence.md"

format_str_list={
    "phrase_interrogative":LangObj._getKeyOfDict("Phrase.interrogative"),
    "you_have_a_table":Noun.have(Pronoun.you(),Verb.none(),Noun("table")),
    "do_you_have_a_table":Phrase.interrogative(Noun.have(Pronoun.you(),Verb.none(),Noun("table"))),
    "you":Pronoun.you(),
    "table":Noun("table"),
    "who_has_a_table":Phrase.interrogative(Noun.have(DeterminerN.human(Pronoun.interrogative()),Verb.none(),Noun("table"))),
    "what_do_you_have":Phrase.interrogative(Noun.have(Pronoun.you(),Verb.none(),DeterminerN.thing(Pronoun.interrogative()))),
    "who":DeterminerN.human(Pronoun.interrogative()),
    "what":DeterminerN.thing(Pronoun.interrogative()),
}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)