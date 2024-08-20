import sys
sys.path.append("")

from SFGPL import *

num_0=NumberList.digit1(Number.zero())
num_1=NumberList.digit1(Number.one())
num_2=NumberList.digit1(Number.two())
num_4=NumberList.digit1(Number.four())
num_9=NumberList.digit1(Number.nine())
num_10=NumberList.digit2(Number.one(),Number.zero())

l_0=LangList.get(LangFunc.arg(),NumberList.IntNL2BL(num_0))
l_1=LangList.get(LangFunc.arg(),NumberList.IntNL2BL(num_1))
l_2=LangList.get(LangFunc.arg(),NumberList.IntNL2BL(num_2))

#[0,0,1]
a=LangList.append(LangList.append(LangList.append(LangList(),num_0),num_0),num_1)

#4-arg[0]>=0
condition_func=LangFunc.setFunc(Noun("condition_func"),LangList.append(LangList(),NumberList.isPN(NumberList.calcSub(num_4,l_0))))

#[arg[0]+1,arg[1]+10,arg[2]*2]
process_func=LangFunc.setFunc(Noun("process_func"),LangList.append(LangList.append(LangList.append(LangList(),NumberList.calcAdd(l_0,num_1)),NumberList.calcAdd(l_1,num_10)),NumberList.calcMul(l_2,num_2)))


w=LangList.While(a,Noun("condition_func"),Noun("process_func"))
print(w)
print([i.getNumber() for i in w.getLangList()])
