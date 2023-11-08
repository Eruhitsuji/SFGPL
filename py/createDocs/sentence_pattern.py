from createDocs import *

FILE_NAME="sentence_pattern.md"

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
    "I_run":Noun.do(Pronoun.I(),Verb("run")),
    "I":Pronoun.I(),
    "run":Verb("run"),
    "verb_none":Verb.none(),
    "this_is_a_table":Noun.eq(Pronoun.proximal(),Verb.none(),Noun("table")),
    "this":Pronoun.proximal(),
    "table":Noun("table"),
    "the_table_is_red":Noun.haveP(Noun("table"),Verb.none(),Modifier("red")),
    "red":Modifier("red"),
    "you_become_a_teacher":Noun.eq(Pronoun.you(),Verb("become"),Noun("teacher")),
    "you":Pronoun.you(),
    "become":Verb("become"),
    "teacher":Noun("teacher"),
    "you_look_sad":Noun.haveP(Pronoun.you(),Verb("look"),Modifier("sad")),
    "look":Verb("look"),
    "sad":Modifier("sad"),
    "I_study_English":Noun.doT(Pronoun.I(),Verb("study"),Noun("English")),
    "study":Verb("study"),
    "English":Noun("English"),
    "I_give_you_a_table":Noun.give(Pronoun.I(),Verb.none(),Pronoun.you(),Noun("table")),
    "I_make_you_a_teacher":Noun.makeN(Pronoun.I(),Verb.none(),Pronoun.you(),Noun("teacher")),
    "I_make_you_sad":Noun.makeM(Pronoun.I(),Verb.none(),Pronoun.you(),Modifier("sad")),
    "I_have_a_table":Noun.have(Pronoun.I(),Verb.none(),Noun("table")),
    "I_belong_to_a_school":Noun.belong(Pronoun.I(),Verb.none(),Noun("school")),
    "school":Noun("school"),
    "The_bed_is_bigger_than_yours":Noun.gt(Noun("bed"),Verb.none(),WordM.big(),DeterminerN.possessive(Pronoun.you())),
    "bed":Noun("bed"),
    "big":WordM.big(),
    "yours_possessive":DeterminerN.possessive(Pronoun.you()),
    "your_table_is_red":Noun.haveP(Noun.have(Pronoun.you(),Verb.none(),Noun("table")),Verb.none(),Modifier("red")),
    "you_have_table":Noun.have(Pronoun.you(),Verb.none(),Noun("table")),
    "you_have_red_table":Noun.have(Pronoun.you(),Verb.none(),Noun.haveP(Noun("table"),Verb.none(),Modifier("red"))),
    "determinerN_stressed":LangObj._getKeyOfDict("DeterminerN.stressed"),
    "stressed_your_table_is_red":Noun.haveP(Noun.have(Pronoun.you(),Verb.none(),DeterminerN.stressed(Noun("table"))),Verb.none(),Modifier("red")),

}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)