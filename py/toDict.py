# This Python File create "dict.py"
import os
import csv
    
THIS_FILE_DIR=os.path.dirname(os.path.abspath(__file__))


DICT_CSV_PATH=os.path.join(THIS_FILE_DIR,"../","dict.csv")
DICT_PY_PATH=os.path.join(THIS_FILE_DIR,"../","SFGPL","dict.py")

def readWordListCSV():
    TO_INT_KEYS=["arg"]
    NECESSARY_KEYS=["word","func","arg"]
    KEYS_KEY="word"
    
    dl={}
    with open(DICT_CSV_PATH,"r",encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_include_flag=True
            for nk in NECESSARY_KEYS:
                if(row[nk].isspace()):
                    row_include_flag=False
            for tik in TO_INT_KEYS:
                try:
                    row[tik]=int(row[tik])
                except ValueError:
                    row_include_flag=False
            
            if(row_include_flag):
                dl[row[KEYS_KEY]]=row
    return dl

dl=readWordListCSV()

w_str=""

w_str+="SFGPL_DICT_DATA={\n"
for key in dl:
    w_str+="\t'{key}':{data},\n".format(key=key,data=str(dict(dl[key])))
w_str+="}"

with open(DICT_PY_PATH,mode="w",encoding="utf-8") as f:
    f.write(w_str)