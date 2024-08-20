from createDocs import *

NAME="LangList"

I_am_a_student=Noun.eq(Pronoun.I(),Verb.none(),Noun("student"))

lang_list_01=LangList.append(LangList.append(LangList.append(LangList.append(LangList.append(LangList(),Pronoun.I()),Noun("pen")),Verb("go")),Modifier("happy")),I_am_a_student)

number_0=BoolList.hex2BoolList(0)

num_0=NumberList.digit1(Number.zero())
num_1=NumberList.digit1(Number.one())
num_2=NumberList.digit1(Number.two())
num_4=NumberList.digit1(Number.four())
num_9=NumberList.digit1(Number.nine())
num_10=NumberList.digit2(Number.one(),Number.zero())

arg_get_0=LangList.get(LangFunc.arg(),NumberList.IntNL2BL(num_0))
arg_get_1=LangList.get(LangFunc.arg(),NumberList.IntNL2BL(num_1))
arg_get_2=LangList.get(LangFunc.arg(),NumberList.IntNL2BL(num_2))

arg_init=LangList.append(LangList.append(LangList.append(LangList(),num_0),num_0),num_1)
condition_func=LangFunc.setFunc(Noun("condition_func"),LangList.append(LangList(),NumberList.isPN(NumberList.calcSub(num_4,arg_get_0))))
process_func=LangFunc.setFunc(Noun("process_func"),LangList.append(LangList.append(LangList.append(LangList(),NumberList.calcAdd(arg_get_0,num_1)),NumberList.calcAdd(arg_get_1,num_10)),NumberList.calcMul(arg_get_2,num_2)))
while_test=LangList.While(arg_init,Noun("condition_func"),Noun("process_func"))


format_str_list={
    "LangList":LangObj._getKeyOfDict("LangList"), 
    "LangList_get":LangObj._getKeyOfDict("LangList.get"), 
    "LangList_append":LangObj._getKeyOfDict("LangList.append"), 
    "LangList_slice":LangObj._getKeyOfDict("LangList.slice"), 
    "LangList_add":LangObj._getKeyOfDict("LangList.add"), 
    "LangList_While":LangObj._getKeyOfDict("LangList.While"),
    
    "lang_list_01":lang_list_01,
    "lang_list_01_get_0":LangList.get(lang_list_01,number_0),

    "number_0":number_0,

    "I":Pronoun.I(),
    "pen":Noun("pen"),
    "go":Verb("go"),
    "happy":Modifier("happy"),
    "I_am_a_student":I_am_a_student,

    "langlist_while_example_1":condition_func,
    "langlist_while_example_2":process_func,
    "langlist_while_example_3":while_test,
    
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
