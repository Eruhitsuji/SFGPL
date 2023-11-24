from createDocs import *

NAME="exampleSentence"

import exampleSentence_sub

table_str=exampleSentence_sub.sc.corpus2MDtableStr()


pre_space_chars=[")","}","]"]
post_space_chars=["(","{","["]

pre_space_chars_r=[" "+c for c in pre_space_chars]
post_space_chars_r=[c+" " for c in post_space_chars]

before_replace_chars=pre_space_chars+post_space_chars
after_replace_chars=pre_space_chars_r+post_space_chars_r

for i in range(len(before_replace_chars)):
    table_str=table_str.replace(before_replace_chars[i],after_replace_chars[i])


format_str_list={
    "example_sentence_table":table_str
}

createDocs(name=NAME,format_str_list=format_str_list,lang_mode="JP",md_mode=True,out_flag=True,all_docs_flag=True)
createDocs(name=NAME,format_str_list=format_str_list,lang_mode="EN",md_mode=True,out_flag=True,all_docs_flag=True)
