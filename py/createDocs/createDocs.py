import sys
import os
import json
import re

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


def makeDocsDir():
    os.makedirs(OUTDIR_JP,exist_ok=True)
    os.makedirs(OUTDIR_EN,exist_ok=True)

makeDocsDir()

DIR_DICT={
    "EN":{
        "in_dir":INDIR_EN,
        "out_dir":OUTDIR_EN
    },
    "JP":{
        "in_dir":INDIR_JP,
        "out_dir":OUTDIR_JP
    }
}

ALL_DOCS_NAME="SFGPL_docs"

def getPathAllDocs(lang_mode:str,ext:str=".md"):
    return DIR_DICT[lang_mode]["out_dir"]+ALL_DOCS_NAME+ext

def removeFile(p:str):
    if(os.path.exists(p)):
        os.remove(p)

#import config json file
CONFIG_PATH=THIS_BASE+"docs_config.json"

DEFAULT_TITLE_MODE="d"
DEFAULT_ALL_DOCS_TITLE_MODE="g"
GITHUB_PRJ_DOCS_URL="https://github.com/Eruhitsuji/SFGPL/blob/main/docs/"


def readConfig(path=CONFIG_PATH):
    with open(path,mode="r",encoding="utf-8") as f:
        return json.load(f)

def preProcessConfig(data):

    dc_data=data["docs_config"]
    r_list=[]
    for i,di in enumerate(dc_data):
        en_title_md="{i}. {title}".format(i=i+1,title=di["EN_title"])
        jp_title_md="{i}. {title}".format(i=i+1,title=di["JP_title"])

        format_key="docs_{name}".format(i=i,name=di["name"])
        tmp_dict={
            "EN_title_md":en_title_md,
            "JP_title_md":jp_title_md,
            "format_key":format_key,
            "EN_github_link":GITHUB_PRJ_DOCS_URL+"en/"+di["md_filename"],
            "JP_github_link":GITHUB_PRJ_DOCS_URL+"jp/"+di["md_filename"],
        }
        
        r_list_dict={**di,**tmp_dict}
        r_list.append(r_list_dict)

    return {"docs_config":r_list}

CONFIG_DATA=preProcessConfig(readConfig())

def mdLinkString(tmp:str):
    tmp=tmp.replace(" ","-")
    code_regex=("[!@#$%^&*\(\)+|~=\\\\`\[\]\{\};':\",./<>?　！＠＃＄％＾＆＊（）＋｜〜＝￥｀「」｛｝；’：”、。，．・＜＞？【】『』《》〔〕［］‹›«»〘〙〚〛]")
    tmp=re.sub(code_regex,"",tmp)
    tmp=tmp.lower()
    tmp="#"+tmp
    return tmp

def getTitleKey(lang_mode:str,md_mode:bool,title_mode:str=DEFAULT_TITLE_MODE):
    data_key=""
    if(md_mode):
        data_key="md_filename"
    else:
        if(title_mode=="d"):
            if(lang_mode=="EN"):
                data_key="EN_title_md"
            elif(lang_mode=="JP"):
                data_key="JP_title_md"
        elif(title_mode=="g"):
            if(lang_mode=="EN"):
                data_key="EN_github_link"
            elif(lang_mode=="JP"):
                data_key="JP_github_link"
    return data_key

def getFormatkeyDict(lang_mode:str,md_mode:bool,title_mode:str,base_str:str="",data=CONFIG_DATA):
    #md_mode
    #   True:Each file mode
    #   False:Include All mode
    data_key=getTitleKey(lang_mode,md_mode,title_mode)

    r_dict={}
    for di in data["docs_config"]:
        tmp=base_str+di[data_key]
        if(not md_mode and title_mode=="d"):
            tmp=mdLinkString(tmp)
            
        r_dict[di["format_key"]]=tmp
    return r_dict

def getDataOfName(name:str,data=CONFIG_DATA):
    for di in data["docs_config"]:
        if(name==di["name"]):
            return di
    return None

def createHeader(name:str,lang_mode:str,md_mode:bool,data=CONFIG_DATA):
    n_data=getDataOfName(name,data)

    data_key=getTitleKey(lang_mode,False,"d")

    r_str="# {}".format(n_data[data_key])

    if(md_mode):
        top_md="../../readme.md"
        lang=""
        lang_md=""
        if(lang_mode=="EN"):
            lang="JP"
            lang_md="../jp/"+n_data["md_filename"]
        
        elif(lang_mode=="JP"):
            lang="EN"
            lang_md="../en/"+n_data["md_filename"]

        r_str+="\n\n[TOP]({top_md})\n/\n[{lang}]({lang_md})".format(top_md=top_md,lang=lang,lang_md=lang_md)

    return r_str


def formatMD(input_md_path,format_str_list):
    r_str=""
    with open(input_md_path,mode="r",encoding="utf-8") as f:
        str_list=f.readlines()

    for str_i in str_list:
        r_str+=str_i.format(**format_str_list)
    return r_str

def __createDocsSub(filename:str,format_str_list:dict,input_dir:str,output_dir:str,out_flag:bool):
    input_md_path=input_dir+filename
    output_md_path=output_dir+filename

    write_str=formatMD(input_md_path,format_str_list)
    if(out_flag):
        with open(output_md_path,mode="w",encoding="utf-8") as f:
            f.write(write_str)
    return write_str

def createDocsSub(name:str,format_str_list:dict,lang_mode:str,md_mode:bool,title_mode:str,data:dict=CONFIG_DATA,out_flag:bool=True):
    dict_data=DIR_DICT[lang_mode]
    n_data=getDataOfName(name,data)

    header_dict={"page_header":createHeader(name,lang_mode,md_mode,data)}
    link_dict=getFormatkeyDict(lang_mode,md_mode,title_mode,"",data)

    fsl_dict={**header_dict,**link_dict,**format_str_list}

    r_str=__createDocsSub(n_data["md_filename"],fsl_dict,dict_data["in_dir"],dict_data["out_dir"],out_flag)
    return r_str

def createDocs(name:str,format_str_list:dict,lang_mode:str,md_mode:bool,title_mode:str=DEFAULT_ALL_DOCS_TITLE_MODE,data:dict=CONFIG_DATA,out_flag:bool=True,all_docs_flag:bool=True):
    r_str=createDocsSub(name=name,format_str_list=format_str_list,lang_mode=lang_mode,md_mode=md_mode,title_mode=title_mode,data=data,out_flag=out_flag)
    if(all_docs_flag):
        r_str_all=createDocsSub(name=name,format_str_list=format_str_list,lang_mode=lang_mode,md_mode=False,title_mode=title_mode,data=data,out_flag=False)
        all_docs_path=getPathAllDocs(lang_mode)

        with open(all_docs_path,mode="a",encoding="utf-8") as f:
            f.write(r_str_all+"\n")

    return r_str

def createReadme(filename="readme.md",input_dir:str=THIS_BASE,out_dir:str="",dir_dict:dict=DIR_DICT,data:dict=CONFIG_DATA):
    doc_en_dir=dir_dict["EN"]["out_dir"]
    doc_jp_dir=dir_dict["JP"]["out_dir"]

    en_list_str=""
    jp_list_str=""

    count=0
    for di in data["docs_config"]:
        if(count!=0):
            en_list_str+="\n"
            jp_list_str+="\n"
        en_list_str+="- [{s}]({p})".format(s=di["EN_title_md"],p=doc_en_dir+di["md_filename"])
        jp_list_str+="- [{s}]({p})".format(s=di["JP_title_md"],p=doc_jp_dir+di["md_filename"])
        count+=1

    format_str_list={"en_list":en_list_str,"jp_list":jp_list_str}
    return __createDocsSub(filename,format_str_list,input_dir,out_dir,True)
