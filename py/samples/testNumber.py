import sys
sys.path.append("")

from SFGPL import *

x=NumberList()
x=NumberList.append(x,Number.one())
print(x)
print(x.getNumber())

x=NumberList.append(x,Number.two())
print(x)
print(x.getNumber())

y1=NumberList.digit5(Number.zero(),Number.one(),Number.two(),Number.three(),Number.four())
print(y1)
print(y1.getNumber())

y2=NumberList.digit5(Number.five(),Number.six(),Number.seven(),Number.eight(),Number.nine())
print(y2)
print(y2.getNumber())

y=NumberList.add(y1,y2)
print(y)
print(y.getNumber())

z1=NumberList.digit2(Number.three(),Number.six())
print(z1)
print(z1.getNumber())

z2=NumberList.digit2(Number.one(),Number.two())
print(z2)
print(z2.getNumber())

z3=NumberList.digit1(Number.three())
print(z3)
print(z3.getNumber())

z12_add=NumberList.calcAdd(z1,z2)
print(z12_add)
print(z12_add.getNumber())

z123_add=NumberList.calcAdd(z12_add,z3)
print(z123_add)
print(z123_add.getNumber())

z12_sub=NumberList.calcSub(z1,z2)
print(z12_sub)
print(z12_sub.getNumber())

z123_sub=NumberList.calcSub(z12_sub,z3)
print(z123_sub)
print(z123_sub.getNumber())

z12_mul=NumberList.calcMul(z1,z2)
print(z12_mul)
print(z12_mul.getNumber())

z123_mul=NumberList.calcMul(z12_mul,z3)
print(z123_mul)
print(z123_mul.getNumber())

z12_div=NumberList.calcDiv(z1,z2)
print(z12_div)
print(z12_div.getNumber())

z123_div=NumberList.calcDiv(z12_div,z3)
print(z123_div)
print(z123_div.getNumber())

z1233_div=NumberList.calcDiv(z123_div,z3)
print(z1233_div)
print(z1233_div.getNumber())

a1=NumberList.digit4(Number.one(),Number.zero(),Number.two(),Number.four())
print(a1)
print(a1.getNumber())

a2=NumberList.digit3(Number.two(),Number.five(),Number.six())
print(a2)
print(a2.getNumber())

a=NumberList.calcAdd(a1,a2)
print(a)
print(a.getNumber())

a_minus=NumberList.calcSub(NumberList.digit1(Number.zero()),a)
print(a_minus)
print(a_minus.getNumber())

a_bl=BoolList.Int(NumberList.IntNL2BL(a))
print(a_bl)
print(a_bl.getData())

a_minus_bl=BoolList.Int(NumberList.IntNL2BL(a_minus))
print(a_minus_bl)
print(a_minus_bl.getData())

a_bl_nl=BoolList.IntBL2NL(a_bl)
print(a_bl_nl)
print(a_bl_nl.getNumber())

a_minus_bl_nl=BoolList.IntBL2NL(a_minus_bl)
print(a_minus_bl_nl)
print(a_minus_bl_nl.getNumber())
