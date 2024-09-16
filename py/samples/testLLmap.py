
import sys
sys.path.append("")

from SFGPL import *

index_00=BoolList.twoBit(Bool.false(),Bool.false())
index_01=BoolList.twoBit(Bool.false(),Bool.true())
index_10=BoolList.fourBit(Bool.false(),Bool.false(),Bool.true(),Bool.false())
index_11=BoolList.fourBit(Bool.false(),Bool.false(),Bool.true(),Bool.true())

nl_05=NumberList.digit1(Number.five())
nl_10=NumberList.digit2(Number.one(),Number.zero())
nl_11=NumberList.digit2(Number.one(),Number.one())
nl_12=NumberList.digit2(Number.one(),Number.two())
nl_13=NumberList.digit2(Number.one(),Number.three())


map_item=LangList.get(LangFunc.arg(),index_00)
map_index=LangList.get(LangFunc.arg(),index_01)
map_all_list=LangList.get(LangFunc.arg(),index_10)

LangFunc.setFunc(Noun("map_func"),LangList.append(LangList(),NumberList.calcMul(map_item,nl_05)))

def checkMap(lang_list):
    result_map=LangList.map(lang_list,Noun("map_func"))
    print(result_map)
    print(list(map(lambda x:x.getNumber(),result_map.getLangList())))


test_lang_list_01=LangList.append(LangList.append(LangList.append(LangList(),nl_10),nl_11),nl_12)
checkMap(test_lang_list_01)

test_lang_list_02=LangList.append(test_lang_list_01,nl_13)
checkMap(test_lang_list_02)