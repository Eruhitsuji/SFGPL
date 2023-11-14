from SFGPL import *

b1=BoolList.byte(Bool.false(),Bool.true(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.true())
print("b1\t",b1)
print(b1.getBytes())
print(b1.getNaturalNumber())
print(b1.getData())

#65
b1_1=BoolList.NaturalNum(b1)
print(b1_1)
print(b1_1.getData())

#65
b1_2=BoolList.Int(b1)
print(b1_2)
print(b1_2.getData())

#A
b1_3=BoolList.ASCII(b1)
print(b1_3)
print(b1_3.getData())


b2_bin_str="1"+"10001001"+"00000000000100000000000"
b2=BoolList.binstr32ToBoolList(b2_bin_str)
print("b2\t",b2)
print(b2.getBytes())
print(b2.getNaturalNumber())

#3296724992
b2_1=BoolList.NaturalNum(b2)
print(b2_1)
print(b2_1.getData())

#-998242304
b2_2=BoolList.Int(b2)
print(b2_2)
print(b2_2.getData())

#-1024.25
b2_3=BoolList.Float(b2)
print(b2_3)
print(b2_3.getData())



b3_bin_str="0"+"10000000"+"10010010000111111011011"
b3=BoolList.binstr32ToBoolList(b3_bin_str)
print("b3\t",b3)
print(b3.getBytes())
print(b3.getNaturalNumber())

#1078530011
b3_1=BoolList.NaturalNum(b3)
print(b3_1)
print(b3_1.getData())

#1078530011
b3_2=BoolList.Int(b3)
print(b3_2)
print(b3_2.getData())

#3.1415927410125732
b3_3=BoolList.Float(b3)
print(b3_3)
print(b3_3.getData())


#i1=1
i1=BoolList.fourBit(Bool.false(),Bool.false(),Bool.false(),Bool.true())
#i2=3
i2=BoolList.fourBit(Bool.false(),Bool.false(),Bool.true(),Bool.true())
#i3=7
i3=BoolList.fourBit(Bool.false(),Bool.true(),Bool.true(),Bool.true())

print(BoolList.get(b3,i1).getBool())#1
print(BoolList.slice(b3,i1,i2).getData())#100
print(BoolList.slice(b3,i1,i3).getData())#1000000
