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

if_01=Bool.IF(Bool.true(),Bool.true())
print(if_01)
print(if_01.getBool())

if_02=Bool.IF(Bool.true(),Bool.false())
print(if_02)
print(if_02.getBool())

if_03=Bool.IF(Bool.false(),Bool.true())
print(if_03)
print(if_03.getBool())

if_04=Bool.IFELSE(Bool.false(),Bool.false(),Bool.true())
print(if_04)
print(if_04.getBool())


test_bool_list_01=BoolList.hex2BoolList(21)
print(test_bool_list_01)
print(test_bool_list_01.getNaturalNumber())

test_bool_list_02=BoolList.hex2BoolList(0)
print(test_bool_list_02)
print(test_bool_list_02.getNaturalNumber())

test_bool_list_03=BoolList.hex2BoolList(12345678900987654321)
print(test_bool_list_03)
print(test_bool_list_03.getNaturalNumber())
