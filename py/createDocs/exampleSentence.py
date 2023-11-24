from createDocs import *

NAME="exampleSentence"

import exampleSentence_sub

table_str=exampleSentence_sub.sc.corpus2MDtableStr()

format_str_list={
    "example_sentence_table":table_str
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
