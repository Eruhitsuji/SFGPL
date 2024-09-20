from createDocs import *

NAME="Bool"

def FloatObj(hex_str:str,order_n:int):
    return BoolList.Float(BoolList.hexstr2BoolList(hex_str,order_n))

I_am_a_student=Noun.eq(Pronoun.I(),Verb.none(),Noun("student"))

b1_bin_str="0"+"10000000"+"10010010000111111011011"
b1=BoolList.binstr32ToBoolList(b1_bin_str)
b1_1=BoolList.NaturalNum(b1)#1078530011
b1_2=BoolList.Int(b1)#1078530011
b1_3=BoolList.Float(b1)#3.1415927410125732

b2_bin_str="01100110111010111110111001111111"
b2=BoolList.binstr32ToBoolList(b2_bin_str)

float_h_hex_str="3555"
float_s_hex_str="3eaa aaab"
float_d_hex_str="3FD5 5555 5555 5555"
float_q_hex_str="3ffd 5555 5555 5555 5555 5555 5555 5555"

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

    "true_or_false":Bool.OR(Bool.true(),Bool.false()),

    "LangObj_IFELSE":LangObj._getKeyOfDict("LangObj.IFELSE"),
    "LangObj_logicIFELSE":LangObj._getKeyOfDict("LangObj.logicIFELSE"),
    "If_true_I_am_a_student":LangObj.logicIFELSE(Bool.true(),I_am_a_student,Phrase.NOT(I_am_a_student)),

    "BoolList":LangObj._getKeyOfDict("BoolList"), 
    "BoolList_get":LangObj._getKeyOfDict("BoolList.get"), 
    "BoolList_append":LangObj._getKeyOfDict("BoolList.append"), 
    "BoolList_slice":LangObj._getKeyOfDict("BoolList.slice"), 
    "BoolList_add":LangObj._getKeyOfDict("BoolList.add"), 
    "BoolList_len":LangObj._getKeyOfDict("BoolList.len"), 
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

    "Float_H_HEX":float_h_hex_str,
    "Float_S_HEX":float_s_hex_str,
    "Float_D_HEX":float_d_hex_str,
    "Float_Q_HEX":float_q_hex_str,
    "Float_H_SFGPL":FloatObj(float_h_hex_str,16),
    "Float_S_SFGPL":FloatObj(float_s_hex_str,32),
    "Float_D_SFGPL":FloatObj(float_d_hex_str,64),
    "Float_Q_SFGPL":FloatObj(float_q_hex_str,128),

    "BoolList_UnixTimeD":LangObj._getKeyOfDict("BoolList.UnixTimeD"), 
    "BoolList_UnixTimeDT":LangObj._getKeyOfDict("BoolList.UnixTimeDT"), 
    "BoolList_UnixTimeDTN":LangObj._getKeyOfDict("BoolList.UnixTimeDTN"),

    "bin_0110_0110_1110_1011_1110_1110_0111_1111":b2,
    "dt_bin_0110_0110_1110_1011_1110_1110_0111_1111":BoolList.UnixTimeDT(b2),
    "dt_bin_0110_0110_1110_1011_1110_1110_0111_1111_str":BoolList.UnixTimeDT(b2).getData(True),

}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
