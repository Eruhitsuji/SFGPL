from SFGPL import *

x1=LangList.append(LangList.append(LangList(),Noun("a")),Noun("b"))
f1=LangList.append(LangList(),LangFunc.arg())
print(f1)

print(LangFunc.setFunc(Noun("f1"),f1))

f1_run_x1=LangFunc.runFunc(Noun("f1"),x1)
print(f1_run_x1)
print(type(f1_run_x1))
print(f1_run_x1.LangListLen())

x2=LangList.append(LangList.append(LangList(),Bool.true()),Bool.false())
print(x2)

f1_run_x2=LangFunc.runFunc(Noun("f1"),x2)
print(f1_run_x2)
print(type(f1_run_x2))
print(f1_run_x2.LangListLen())

index_0=BoolList.twoBit(Bool.false(),Bool.false())
index_1=BoolList.twoBit(Bool.false(),Bool.true())


print(LangList.get(LangFunc.arg(),index_0))
print(LangList.get(x2,index_0))
f2=LangList.append(LangList(),Bool.AND(LangList.get(LangFunc.arg(),index_0),LangList.get(LangFunc.arg(),index_1)))
print(f2)

print(LangFunc.setFunc(Noun("f2"),f2))
f2_run_x2=LangFunc.runFunc(Noun("f2"),x2)
print(f2_run_x2)
print(type(f2_run_x2))
print(f2_run_x2.LangListLen())

print(LangList.get(f2_run_x2,index_0).getBool())
print(f2.getWordsAll())
print(Noun.eq(DeterminerN.plural(Pronoun.I()),Verb.none(),Noun("student")).getWordsAll())

f3=LangList.append(LangList(),BoolList.get(LangList.get(LangFunc.arg(),index_0),index_0))
print(f3)
print(LangFunc.setFunc(Noun("f3"),f3))

x3=LangList.append(LangList(),BoolList.append(BoolList(),Bool.true()))
f3_run_x3=LangFunc.runFunc(Noun("f3"),x3)
print(f3_run_x3)


f4=LangList.append(LangList(),DeterminerN.male(LangList.get(LangFunc.arg(),index_0)))
x4=LangList.append(LangList(),Noun("student"))
print(LangFunc.setFunc(Noun("f4"),f4))

f4_run_x4=LangFunc.runFunc(Noun("f4"),x4)
print(f4_run_x4)


x_2bit_00=LangList.append(LangList.append(LangList(),Bool.false()),Bool.false())
x_2bit_01=LangList.append(LangList.append(LangList(),Bool.true()),Bool.false())
x_2bit_10=LangList.append(LangList.append(LangList(),Bool.false()),Bool.true())
x_2bit_11=LangList.append(LangList.append(LangList(),Bool.true()),Bool.true())

#xor
a=LangList.get(LangFunc.arg(),index_0)
b=LangList.get(LangFunc.arg(),index_1)
a_nand_b=Bool.NAND(a,b)

xor=LangList.append(LangList(),Bool.NAND(Bool.NAND(a,a_nand_b),Bool.NAND(a_nand_b,b)))
print(LangFunc.setFunc(Noun("xor"),xor))

print(LangFunc.runFunc(Noun("xor"),x_2bit_00))

print(LangFunc.runFunc(Noun("xor"),x_2bit_00).getLangList()[0].getBool())
print(LangFunc.runFunc(Noun("xor"),x_2bit_01).getLangList()[0].getBool())
print(LangFunc.runFunc(Noun("xor"),x_2bit_10).getLangList()[0].getBool())
print(LangFunc.runFunc(Noun("xor"),x_2bit_11).getLangList()[0].getBool())


xnor=LangList.append(LangList(),Bool.NOT(LangList.get(LangFunc.runFunc(Noun("xor"),LangFunc.arg()),index_0)))
print(LangFunc.setFunc(Noun("xnor"),xnor))

print(LangFunc.runFunc(Noun("xnor"),x_2bit_00))

print(LangFunc.runFunc(Noun("xnor"),x_2bit_00).getLangList()[0].getBool())
print(LangFunc.runFunc(Noun("xnor"),x_2bit_01).getLangList()[0].getBool())
print(LangFunc.runFunc(Noun("xnor"),x_2bit_10).getLangList()[0].getBool())
print(LangFunc.runFunc(Noun("xnor"),x_2bit_11).getLangList()[0].getBool())
