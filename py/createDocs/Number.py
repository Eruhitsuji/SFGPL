from createDocs import *

NAME="Number"

format_str_list={
    "number_zero":Number.zero(),
    "number_one":Number.one(),
    "number_two":Number.two(),
    "number_three":Number.three(),
    "number_four":Number.four(),
    "number_five":Number.five(),
    "number_six":Number.six(),
    "number_seven":Number.seven(),
    "number_eight":Number.eight(),
    "number_nine":Number.nine(),

    "NumberList":LangObj._getKeyOfDict("NumberList"), 
    "NumberList_get":LangObj._getKeyOfDict("NumberList.get"), 
    "NumberList_append":LangObj._getKeyOfDict("NumberList.append"), 
    "NumberList_slice":LangObj._getKeyOfDict("NumberList.slice"), 
    "NumberList_add":LangObj._getKeyOfDict("NumberList.add"),
    "NumberList_len":LangObj._getKeyOfDict("NumberList.len"),

    "NumberList_digit1":LangObj._getKeyOfDict("NumberList.digit1"),
    "NumberList_digit2":LangObj._getKeyOfDict("NumberList.digit2"), 
    "NumberList_digit3":LangObj._getKeyOfDict("NumberList.digit3"),
    "NumberList_digit4":LangObj._getKeyOfDict("NumberList.digit4"),
    "NumberList_digit5":LangObj._getKeyOfDict("NumberList.digit5"),

    "I_have_five_apples":Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("apple"),Verb.none(),NumberList.digit1(Number.five()))),
    "I":Pronoun.I(),
    "apple":Noun("apple"),
    "I_have_fifteen_apples":Noun.have(Pronoun.I(),Verb.none(),Noun.eq(Noun("apple"),Verb.none(),NumberList.digit2(Number.one(),Number.five()))),

    "Japan_has_125416877_people":Noun.have(Noun("Japan"),Verb.none(),Noun.eq(Noun("people"),Verb.none(),NumberList.add(NumberList.digit4(Number.one(),Number.two(),Number.five(),Number.four()),NumberList.digit5(Number.one(),Number.six(),Number.eight(),Number.seven(),Number.seven())))),
    "Japan":Noun("Japan"),
    "people":Noun("people"),

    "NumberList_calcAdd":LangObj._getKeyOfDict("NumberList.calcAdd"),
    "NumberList_calcSub":LangObj._getKeyOfDict("NumberList.calcSub"),
    "NumberList_calcMul":LangObj._getKeyOfDict("NumberList.calcMul"),
    "NumberList_calcDiv":LangObj._getKeyOfDict("NumberList.calcDiv"),

    "real_number_3_14":NumberList.calcDiv(NumberList.digit3(Number.three(),Number.one(),Number.four()),NumberList.digit3(Number.one(),Number.zero(),Number.zero())),

    "NumberList_IntNL2BL":LangObj._getKeyOfDict("NumberList.IntNL2BL"),
    "BoolList_IntBL2NL":LangObj._getKeyOfDict("BoolList.IntBL2NL"),

}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
