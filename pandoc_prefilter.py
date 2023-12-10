#!/usr/bin/env python

import os
import sys
import re

GITHUB_REPOSITORY="https://github.com/Eruhitsuji/SFGPL/blob/main/"

def imgLinkReplace(path_str):
    return re.sub(r"(../)+img/","./",path_str)

def inPageLinkReplace(s):
    pl=re.findall(r"\[([\w ]+)\]\(#(\d+)-([\w-]+)\)",s)
    for pli in pl:
        display_word=pli[0]
        link_num=pli[1]
        link_str=pli[2]
        raw_str="[{dw}](#{ln}-{ls})".format(dw=display_word,ln=link_num,ls=link_str)
        rp_str="\\hyperref[sec:sec_num_{label}]{{{text}}}".format(label=link_num,text=display_word)
        s=s.replace(raw_str,rp_str)
    return s

def inFileLinkReplace(s):
    pl=re.findall(r"\[(.+)\]\(../../(.+)\)",s)
    for pli in pl:
        display_word=pli[0]
        link=pli[1]
        raw_str="[{dw}](../../{link})".format(dw=display_word,link=link)
        rp_str="[{dw}]({dir}{link})".format(dw=display_word,dir=GITHUB_REPOSITORY,link=link)
        s=s.replace(raw_str,rp_str)
    return s

def texPartReplace(s):
    l=re.findall(r"<div class=\"tex_part\" text=\"(.+)\"></div>",s)
    for li in l:
        raw_str="<div class=\"tex_part\" text=\"{}\"></div>".format(li)
        rp_str="\\part{{{}}}".format(li)
        s=s.replace(raw_str,rp_str)
    return s

def texSectionLabelReplace(s):
    l=re.findall(r"<div id=\"tex_section_label_(\d+)\"></div>",s)
    for li in l:
        raw_str="<div id=\"tex_section_label_{}\"></div>".format(li)
        rp_str="\\label{{sec:sec_num_{}}}".format(li)
        s=s.replace(raw_str,rp_str)
    return s

def sectionNameReplace(s):
    l=re.findall(r"# (\d+)\. (.+)",s)
    for li in l:
        s_num=li[0]
        s_str=li[1]
        raw_str="# {}. {}".format(s_num,s_str)
        rp_str="# {}".format(s_str)
        s=s.replace(raw_str,rp_str)
    return s

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

if __name__ == "__main__":
    path=sys.argv[1]

    with open(path,mode="r",encoding="utf-8") as f:
        l=f.readlines()

    with open(path,mode="w",encoding="utf-8") as f:
        for line in l:
            line=imgLinkReplace(line)
            line=inPageLinkReplace(line)
            line=inFileLinkReplace(line)
            line=texPartReplace(line)
            line=texSectionLabelReplace(line)
            line=sectionNameReplace(line)
            line=tdNewLineReplace(line)
            f.write(line)

