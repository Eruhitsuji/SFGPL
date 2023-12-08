#!/usr/bin/env python

import os
import sys
import re
from subprocess import Popen, PIPE, call

from pandocfilters import toJSONFilter, Link, Str

PRE_MODE="pre"
PANDOC_FILTER_MODE="pandoc_filter"

MODE=PRE_MODE

def imgLinkReplace(path_str):
    return re.sub(r"(../)+img/","./",path_str)

def tdNewLineReplace(td_str):
    replace_str_config=[
        {
            "key":r"<div class=\"long_td\">",
            "tex":"\\\\begin{tabular}{c}",
            "small":"\\\\scriptsize ",
            "blank":"",
        },
        {
            "key":r"<br>",
            "tex":"\\\\\\\\",
            "small":"",
            "blank":"",

        },
        {
            "key":r"</div>",
            "tex":"\\\\end{tabular}",
            "small":"",
            "blank":"",
        }        
    ]

    R_MODE="small"
    if(re.match(r".*<div class=\"long_td\">(.*<br>.*)+</div>.*",td_str)):
        for config in replace_str_config:
            td_str=re.sub(config["key"],config[R_MODE],td_str)
    return td_str

def myfilter(key,value,format_,meta):
    if(key=="Link"):
        value[1][0]=imgLinkReplace(value[1][0])
        return Link(*value)
    elif(key=="Str"):
        value=imgLinkReplace(value)
        return Str(*value)
    
if __name__ == "__main__":
    if(MODE==PRE_MODE):
        path=sys.argv[1]

        with open(path,mode="r",encoding="utf-8") as f:
            l=f.readlines()

        with open(path,mode="w",encoding="utf-8") as f:
            for line in l:
                line=imgLinkReplace(line)
                line=tdNewLineReplace(line)
                f.write(line)
    
    elif(MODE==PANDOC_FILTER_MODE):
        toJSONFilter(myfilter)
