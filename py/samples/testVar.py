import sys
sys.path.append("")

from SFGPL import *

# initial assignment 
var1=Noun("var1")
ll1=LangList.append(LangList.append(LangList(),Noun("a")),Noun("b"))

print(ll1.getLangList())
print(LangVar.set(var1,ll1))

var1_01=LangVar.get(var1)

print(var1_01)
print(var1_01.getLangList())

# 2nd assignment
ll1=LangList.append(ll1,Noun("c"))

print(LangVar.set(var1,ll1))

var1_02=LangVar.get(var1)

print(var1_02)
print(var1_02.getLangList())

#test Func
f1=LangList.append(LangFunc.arg(),Noun("append"))
print(f1)

print(LangFunc.setFunc(Noun("f1"),f1))

var2=Noun("var2")
print(LangVar.set(var2,LangFunc.runFunc(Noun("f1"),LangVar.get(var1))))

var2_01=LangVar.get(var2)
print(var2_01)
print([str(x) for x in var2_01.getLangList()])

#test func 2
print(LangVar.set(var2,LangFunc.runFunc(Noun("f1"),LangVar.get(var2))))

var2_02=LangVar.get(var2)
print(var2_02)
print([str(x) for x in var2_02.getLangList()])
