import sys
sys.path.append("")

from SFGPL import *
import os
import collections

corpus_json_path=sys.argv[1]
print_number=10

if(len(sys.argv)>=3):
    print_number=int(sys.argv[2])

json_obj=SFGPLCorpus.readJson(corpus_json_path)

count_word_raw=json_obj.corpusWordCount()
#count_word_raw=json_obj.corpusWordCount(include_word_func=lambda x: "'" in x)

count_word=sorted(count_word_raw.items(),key=lambda x:x[1],reverse=True)

for i in range(print_number):
    print(count_word[i][0]+"\t"+str(count_word[i][1]))
