from createDocs import *

FILE_NAME="LangFunc.md"


index_0=BoolList.twoBit(Bool.false(),Bool.false())
index_1=BoolList.twoBit(Bool.false(),Bool.true())

#xor
a=LangList.get(LangFunc.arg(),index_0)
b=LangList.get(LangFunc.arg(),index_1)
a_nand_b=Bool.NAND(a,b)

xor=LangList.append(LangList(),Bool.NAND(Bool.NAND(a,a_nand_b),Bool.NAND(a_nand_b,b)))

xor_set=LangFunc.setFunc(Noun("xor"),xor)

x_2bit_00=LangList.append(LangList.append(LangList(),Bool.false()),Bool.false())

format_str_list={
    "LangFunc_setFunc":LangObj._getKeyOfDict("LangFunc.setFunc"), 
    "LangFunc_arg":LangObj._getKeyOfDict("LangFunc.arg"), 
    "LangFunc_runFunc":LangObj._getKeyOfDict("LangFunc.runFunc"),
    
    "xor_set":str(xor_set),
    "xor_00":LangFunc.runFunc(Noun("xor"),x_2bit_00),
}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)