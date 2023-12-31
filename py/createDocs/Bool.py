from createDocs import *

NAME="Bool"

I_am_a_student=Noun.eq(Pronoun.I(),Verb.none(),Noun("student"))

b1_bin_str="0"+"10000000"+"10010010000111111011011"
b1=BoolList.binstr32ToBoolList(b1_bin_str)
b1_1=BoolList.NaturalNum(b1)#1078530011
b1_2=BoolList.Int(b1)#1078530011
b1_3=BoolList.Float(b1)#3.1415927410125732


format_str_list={
    "Bool_false":LangObj._getKeyOfDict("Bool.false"),
    "Bool_true":LangObj._getKeyOfDict("Bool.true"),
    "Bool_B2N":LangObj._getKeyOfDict("Bool.B2N"),

    "It_is_true_that_I_am_a_student":Bool.B2N(I_am_a_student,Bool.true()),
    "I_am_a_student":I_am_a_student,

    "LangObj_NOT":LangObj._getKeyOfDict("LangObj.NOT"),
    "LangObj_OR":LangObj._getKeyOfDict("LangObj.OR"),
    "LangObj_AND":LangObj._getKeyOfDict("LangObj.AND"),
    "LangObj_NOR":LangObj._getKeyOfDict("LangObj.NOR"),
    "LangObj_NAND":LangObj._getKeyOfDict("LangObj.NAND"),

    "BoolList":LangObj._getKeyOfDict("BoolList"), 
    "BoolList_get":LangObj._getKeyOfDict("BoolList.get"), 
    "BoolList_append":LangObj._getKeyOfDict("BoolList.append"), 
    "BoolList_slice":LangObj._getKeyOfDict("BoolList.slice"), 
    "BoolList_add":LangObj._getKeyOfDict("BoolList.add"), 
    "BoolList_twoBit":LangObj._getKeyOfDict("BoolList.twoBit"), 
    "BoolList_fourBit":LangObj._getKeyOfDict("BoolList.fourBit"), 
    "BoolList_byte":LangObj._getKeyOfDict("BoolList.byte"), 
    "BoolList_NaturalNum":LangObj._getKeyOfDict("BoolList.NaturalNum"), 
    "BoolList_Int":LangObj._getKeyOfDict("BoolList.Int"), 
    "BoolList_Float":LangObj._getKeyOfDict("BoolList.Float"), 
    "BoolList_ASCII":LangObj._getKeyOfDict("BoolList.ASCII"), 

    "bin_0100_0000_0100_1001_0000_1111_1101_1011":b1,
    "NN_b1":b1_1,
    "INT_b1":b1_2,
    "Float_b1":b1_3,
    "NN_b1_get":b1_1.getData(),
    "INT_b1_get":b1_2.getData(),
    "Float_b1_get":b1_3.getData(),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
