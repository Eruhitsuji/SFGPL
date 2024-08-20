from createDocs import *

NAME="LangVar"

var1_name=Noun("var1")
ll1=LangList.append(LangList.append(LangList(),Noun("apple")),Noun("banana"))

format_str_list={
    "LangVar_set":LangObj._getKeyOfDict("LangVar.set"), 
    "LangVar_get":LangObj._getKeyOfDict("LangVar.get"), 
    "var1_set_lang_list":LangVar.set(var1_name,ll1),
    "var1_get_lang_list":LangVar.get(var1_name),
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
