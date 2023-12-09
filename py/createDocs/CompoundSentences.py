from createDocs import *

NAME="CompoundSentences"

s01=Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.N2M(DeterminerN.place(Noun("Tokyo")))))
s02=Noun.do(Pronoun.I(),Verb.add(Verb.progressive(Verb("shop")),Modifier.N2M(DeterminerN.place(Pronoun.proximal()))))

format_str_list={
    "I_went_to_Tokyo_and_I_was_shopping_there_01":Noun.AND(Phrase.past(s01),Phrase.past(s02)),
    "I_went_to_Tokyo_and_I_was_shopping_there_02":Phrase.past(Noun.AND(s01,s02)),
    "I":Pronoun.I(),
    "go":Verb("go"),
    "to_Tokyo":Modifier.N2M(DeterminerN.place(Noun("Tokyo"))),
    "shop_verb":Verb("shop"),
    "there":DeterminerN.place(Pronoun.proximal()),

    "DeterminerN_stressed":LangObj._getKeyOfDict("DeterminerN.stressed"),
    "my_bag_is_big":Noun.haveP(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("bag"))),Verb.none(),WordM.big()),
    "bag":Noun("bag"),
    "big":WordM.big(),
    
    "I_have_a_bag_is_big":Noun.have(Pronoun.I(),Verb.none(),Noun.haveP(Noun("bag"),Verb.none(),WordM.big())),

    "I_give_you_the_desk_I_built":Noun.give(Pronoun.I(),Verb.none(),Pronoun.you(),Phrase.past(Noun.doT(Pronoun.I(),Verb("build"),DeterminerN.stressed(Noun("desk"))))),
    "you":Pronoun.you(),
    "build":Verb("build"),
    "desk":Noun("desk"),

    "I_ate_sushi_when_I_went_to_Tokyo":Phrase.past(Noun.doT(Pronoun.I(),Verb.add(Verb("eat"),Modifier.N2M(s01)),Noun("sushi"))),
    "eat":Verb("eat"),
    "sushi":Noun("sushi"),

    "I_went_grocery_shopping_while_my_kids_were_sleeping":Phrase.past(Noun.do(Pronoun.I(),Verb.add(Verb("go"),Modifier.AND(Modifier.N2M(Noun.eq(Noun.V2N(Verb.progressive(Verb("shop"))),Verb.none(),Noun("grocery"))),Modifier.N2M(Noun.do(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(DeterminerN.plural(Noun("kid")))),Verb.progressive(Verb("sleep")))))))),
    "grocery":Noun("grocery"),
    "kid":Noun("kid"),
    "sleep":Verb("sleep"),

    "noun_eq":LangObj._getKeyOfDict("Noun.eq"),
    "noun_have":LangObj._getKeyOfDict("Noun.have"),
    "noun_belong":LangObj._getKeyOfDict("Noun.belong"),

    "this_pen_is_big":Noun.haveP(Noun.eq(Pronoun.proximal(),Verb.none(),DeterminerN.stressed(Noun("pen"))),Verb.none(),WordM.big()),
    "this":Pronoun.proximal(),
    "pen":Noun("pen"),
    "my_pen_is_big":Noun.haveP(Noun.have(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("pen"))),Verb.none(),WordM.big()),
    "my_school_is_big":Noun.haveP(Noun.belong(Pronoun.I(),Verb.none(),DeterminerN.stressed(Noun("school"))),Verb.none(),WordM.big()),
    "school":Noun("school"),

}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
