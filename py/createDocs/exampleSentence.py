from createDocs import *

FILE_NAME="exampleSentence.md"

import exampleSentence_sub

table_str=exampleSentence_sub.sc.corpus2MDtableStr()

format_str_list={
    "example_sentence_table":table_str
}

createDocs(FILE_NAME,format_str_list,INDIR_JP,OUTDIR_JP)
createDocs(FILE_NAME,format_str_list,INDIR_EN,OUTDIR_EN)