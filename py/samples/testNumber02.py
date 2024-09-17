import sys
sys.path.append("")

from SFGPL import *

def printBLData(bl:BoolList):
    print("BL - raw          : ",bl.getData())
    print("BL - natural      : ",BoolList.NaturalNum(bl).getData())
    print("BL - int          : ",BoolList.Int(bl).getData())
    print("BL - NL           : ",BoolList.IntBL2NL(bl).getNumber())
    print("BL - NL - BL      : ",NumberList.IntNL2BL(BoolList.IntBL2NL(bl)).getData())
    print()

def printNLData(nl:NumberList):
    tmp_bl=NumberList.IntNL2BL(nl)
    print("NL                : ",nl.getNumber())
    print("NL - BL - raw     : ",tmp_bl.getData())
    print("NL - BL - natural : ",BoolList.NaturalNum(tmp_bl).getData())
    print("NL - BL - int     : ",BoolList.Int(tmp_bl).getData())
    print("NL - BL - NL      : ",BoolList.IntBL2NL(tmp_bl).getNumber())
    print()


#[0,1,0,0,0,0,0,0]
bl_01=BoolList.byte(Bool.false(),Bool.true(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.false())
printBLData(bl_01)

#[1,1,0,0,0,0,0,0]
bl_02=BoolList.byte(Bool.true(),Bool.true(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.false(),Bool.false())
printBLData(bl_02)

#12345
nl_01=NumberList.digit5(Number.one(),Number.two(),Number.three(),Number.four(),Number.five())
printNLData(nl_01)

#-12345
nl_01_minus=NumberList.minus(nl_01)
printNLData(nl_01_minus)

#12
nl_02=NumberList.digit2(Number.one(),Number.two())
printNLData(nl_02)

#12345+12=12357
printNLData(NumberList.calcAdd(nl_01,nl_02))

#12345-12=12333
printNLData(NumberList.calcSub(nl_01,nl_02))

#12-12345=-12333
printNLData(NumberList.calcSub(nl_02,nl_01))

#12345*12=148140
printNLData(NumberList.calcMul(nl_01,nl_02))

#12345/12=1028.75
#The solution will not be an integer, resulting in a NoneType Error.
#printNLData(NumberList.calcDiv(nl_01,nl_02))

#5
nl_03=NumberList.digit1(Number.five())
printNLData(nl_03)

#12345*5=2469
printNLData(NumberList.calcDiv(nl_01,nl_03))

