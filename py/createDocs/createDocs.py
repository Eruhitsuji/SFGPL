import sys
import os

PRJ_BASE="../../"
THIS_BASE="py/createDocs/"

sys.path.append(os.path.join(os.path.dirname(__file__),PRJ_BASE))

from SFGPL import *


OUTDIR_BASE="docs/"
OUTDIR_JP=OUTDIR_BASE+"jp/"
OUTDIR_EN=OUTDIR_BASE+"en/"

INDIR_BASE=THIS_BASE+"docs/"
INDIR_JP=INDIR_BASE+"jp/"
INDIR_EN=INDIR_BASE+"en/"

os.makedirs(OUTDIR_JP,exist_ok=True)
os.makedirs(OUTDIR_EN,exist_ok=True)

def formatMD(input_md_path,format_str_list):
    r_str=""
    with open(input_md_path,mode="r",encoding="utf-8") as f:
        str_list=f.readlines()

    for str_i in str_list:
        r_str+=str_i.format(**format_str_list)
    return r_str

def createDocs(filename:str,format_str_list:dict,input_dir:str,output_dir:str):
    input_md_path=input_dir+filename
    output_md_path=output_dir+filename

    write_str=formatMD(input_md_path,format_str_list)

    with open(output_md_path,mode='w',encoding="utf-8") as f:
        f.write(write_str)
