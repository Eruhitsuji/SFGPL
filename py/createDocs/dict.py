from createDocs import *
import csv

NAME="dict"
DICT_PATH="dict.csv"
EXTRACT_KEYS=[
    "ID",
    "word",
    "func",
    "How to use",
    "Japanese",
    "English",
]

DEF_WBR_DICT={
    "func":["."],
    "English":["/"]
}
def readDictCSV(dict_path=DICT_PATH,extract_keys=EXTRACT_KEYS):

    def addWbrStr(s:str,key:str,wbr_dict=DEF_WBR_DICT):
        WBR_STR=" "
        if(key in wbr_dict):
            for k in wbr_dict[key]:
                s=s.replace(k,k+WBR_STR)
        return s


    with open(dict_path,mode="r",encoding="utf8",newline="") as f:
        csvreader=csv.reader(f)
        header=next(csvreader)
        content=[row for row in csvreader]
    content.insert(0,header)

    dictionary_str=""

    header_str="|"
    under_header_str="|"
    for key in header:
        if(key in extract_keys):
            if(key in extract_keys):
                header_str+=key+"|"
                under_header_str+=":--:|"
    dictionary_str+=header_str+"\n"
    dictionary_str+=under_header_str+"\n"

    for ci in content:
        line_str="|"
        for i,key in enumerate(header):
            if(key in extract_keys):
                line_str+=addWbrStr(ci[i],key)+"|"
        dictionary_str+=line_str+"\n"

    return dictionary_str

format_str_list={
    "SFGPL_word_dictionary":readDictCSV()
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
