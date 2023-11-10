from SFGPL import *

b1=BoolList.byte(Bool.false(),Bool.true(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.true())
print(b1)
print(b1.get())

#65
b1_1=BoolList.NaturalNum(b1)
print(b1_1)
print(b1_1.get())

#65
b1_2=BoolList.Int(b1)
print(b1_2)
print(b1_2.get())

#A
b1_3=BoolList.ASCII(b1)
print(b1_3)
print(b1_3.get())


b2_bin_str="1"+"10001001"+"00000000000100000000000"
b2=BoolList.binstr32ToBoolList(b2_bin_str)

print(b2)

#3296724992
b2_1=BoolList.NaturalNum(b2)
print(b2_1)
print(b2_1.get())

#-998242304
b2_2=BoolList.Int(b2)
print(b2_2)
print(b2_2.get())

#-1024.25
b2_3=BoolList.Float(b2)
print(b2_3)
print(b2_3.get())



b3_bin_str="0"+"10000000"+"10010010000111111011011"
b3=BoolList.binstr32ToBoolList(b3_bin_str)

print(b3)

#1078530011
b3_1=BoolList.NaturalNum(b3)
print(b3_1)
print(b3_1.get())

#1078530011
b3_2=BoolList.Int(b3)
print(b3_2)
print(b3_2.get())

#3.1415927410125732
b3_3=BoolList.Float(b3)
print(b3_3)
print(b3_3.get())