import sys
sys.path.append("")

from SFGPL import *
import os

OUT_DIR="out/"

os.makedirs(OUT_DIR,exist_ok=True)

sc=SFGPLCorpus()

person_list=[
    {"SFGPL":Pronoun.I(),"type":(1,False),"subject":"I","own":"my","object":"me"},
    {"SFGPL":Pronoun.you(),"type":(2,False),"subject":"you","own":"your","object":"you"},
    {"SFGPL":DeterminerN.male(Pronoun.he()),"type":(3,False),"subject":"he","own":"his","object":"him"},
    {"SFGPL":DeterminerN.female(Pronoun.he()),"type":(3,False),"subject":"she","own":"her","object":"her"},
    {"SFGPL":DeterminerN.plural(DeterminerN.human(Pronoun.indefinite())),"type":(3,False),"subject":"someone","own":"someone's","object":"someone"},
    {"SFGPL":Noun("John"),"type":(3,False),"subject":"John","own":"John's","object":"John"},
    {"SFGPL":Noun("Alice"),"type":(3,False),"subject":"Alice","own":"Alice's","object":"Alice"},

    {"SFGPL":DeterminerN.plural(Pronoun.I()),"type":(1,True),"subject":"we","own":"our","object":"us"},
    {"SFGPL":DeterminerN.plural(Pronoun.you()),"type":(2,True),"subject":"you","own":"your","object":"you"},
    {"SFGPL":DeterminerN.plural(DeterminerN.male(Pronoun.he())),"type":(3,True),"subject":"they","own":"their","object":"them"},
    {"SFGPL":DeterminerN.plural(DeterminerN.female(Pronoun.he())),"type":(3,True),"subject":"they","own":"their","object":"them"},
]

verb_doT_list=[
    {"SFGPL":WordV.create(),"present":"create","present-3":"creates","past":"created"},
    {"SFGPL":WordV.destroy(),"present":"break","present-3":"breaks","past":"broke"},
    {"SFGPL":WordV.act(),"present":"move","present-3":"moves","past":"moved"},
    {"SFGPL":Verb("touch"),"present":"touch","present-3":"touches","past":"touched"},
    {"SFGPL":Verb("put"),"present":"put","present-3":"puts","past":"put"}
]

object_list=[
    {"SFGPL":Noun("table"),"raw":"table","a_":"a table"},
    {"SFGPL":Noun("desk"),"raw":"desk","a_":"a desk"},
    {"SFGPL":Noun("chair"),"raw":"chair","a_":"a chair"},
    {"SFGPL":Noun("book"),"raw":"book","a_":"a book"},
    {"SFGPL":Noun("dictionary"),"raw":"dictionary","a_":"a dictionary"},
    {"SFGPL":Noun("notebook"),"raw":"notebook","a_":"notebook"},
    {"SFGPL":Noun("pen"),"raw":"pen","a_":"a pen"},
    {"SFGPL":Noun("pencil"),"raw":"pencil","a_":"a pencil"},
    {"SFGPL":Noun("apple"),"raw":"apple","a_":"an apple"},
    {"SFGPL":Noun("box"),"raw":"box","a_":"a box"},
    {"SFGPL":Noun("ball"),"raw":"ball","a_":"a ball"},
    {"SFGPL":Noun("door"),"raw":"door","a_":"a door"},
    {"SFGPL":Noun("computer"),"raw":"computer","a_":"a computer"},
    {"SFGPL":Noun("cup"),"raw":"cup","a_":"a cup"},
    {"SFGPL":Noun("shelf"),"raw":"shelf","a_":"a shelf"}
]

def upperFirstChar(s):
    return s[0].upper()+s[1:]

def set_data_to_corpus(sc,data):
    sc.setCorpus(
        data["present"][0],
        data["present"][1]
    )

    sc.setCorpus(
        data["past"][0],
        data["past"][1]
    )

    sc.setCorpus(
        data["future"][0],
        data["future"][1]
    )

    sc.setCorpus(
        data["present_not"][0],
        data["present_not"][1]
    )

    sc.setCorpus(
        data["past_not"][0],
        data["past_not"][1]
    )

    sc.setCorpus(
        data["future_not"][0],
        data["future_not"][1]
    )
    return sc


def sample_sentence_01(p1,v,p2,o):
    s=Noun.doT(p1["SFGPL"],v["SFGPL"],Noun.have(p2["SFGPL"],Verb.none(),DeterminerN.stressed(o["SFGPL"])))

    verb_present_str=v["present"] if p1["type"]!=(3,False) else v["present-3"]
    do_not_present_str="don't" if p1["type"]!=(3,False) else "doesn't"

    
    eng_str_present=upperFirstChar("{p1} {v} {p2} {o}.".format(p1=p1["subject"],v=verb_present_str,p2=p2["own"],o=o["raw"]))
    eng_str_past=upperFirstChar("{p1} {v} {p2} {o}.".format(p1=p1["subject"],v=v["past"],p2=p2["own"],o=o["raw"]))
    eng_str_future=upperFirstChar("{p1} will {v} {p2} {o}.".format(p1=p1["subject"],v=v["present"],p2=p2["own"],o=o["raw"]))
    eng_str_present_not=upperFirstChar("{p1} {dn} {v} {p2} {o}.".format(p1=p1["subject"],dn=do_not_present_str,v=v["present"],p2=p2["own"],o=o["raw"]))
    eng_str_past_not=upperFirstChar("{p1} didn't {v} {p2} {o}.".format(p1=p1["subject"],v=v["present"],p2=p2["own"],o=o["raw"]))
    eng_str_future_not=upperFirstChar("{p1} will not {v} {p2} {o}.".format(p1=p1["subject"],v=v["present"],p2=p2["own"],o=o["raw"]))

    return {
        "present":(s,eng_str_present),
        "past":(Phrase.past(s),eng_str_past),
        "future":(Phrase.future(s),eng_str_future),
        "present_not":(Phrase.NOT(s),eng_str_present_not),
        "past_not":(Phrase.past(Phrase.NOT(s)),eng_str_past_not),
        "future_not":(Phrase.future(Phrase.NOT(s)),eng_str_future_not),
        }


for p1 in person_list:
    for v in verb_doT_list:
        for p2 in person_list:
            for o in object_list:
                out_data=sample_sentence_01(p1,v,p2,o)
                print("01",out_data["present"][1])
                sc=set_data_to_corpus(sc,out_data)


def sample_sentence_02(p1,p2,p3,o):
    v={"SFGPL":Verb.none(),"present":"give","present-3":"gives","past":"gave"}

    s=Noun.give(p1["SFGPL"],v["SFGPL"],p2["SFGPL"],Noun.have(p3["SFGPL"],Verb.none(),DeterminerN.stressed(o["SFGPL"])))

    verb_present_str=v["present"] if p1["type"]!=(3,False) else v["present-3"]
    do_not_present_str="don't" if p1["type"]!=(3,False) else "doesn't"

    
    eng_str_present=upperFirstChar("{p1} {v} {p2} {p3} {o}.".format(p1=p1["subject"],v=verb_present_str,p2=p2["object"],p3=p3["own"],o=o["raw"]))
    eng_str_past=upperFirstChar("{p1} {v} {p2} {p3} {o}.".format(p1=p1["subject"],v=v["past"],p2=p2["object"],p3=p3["own"],o=o["raw"]))
    eng_str_future=upperFirstChar("{p1} will {v} {p2} {p3} {o}.".format(p1=p1["subject"],v=v["present"],p2=p2["object"],p3=p3["own"],o=o["raw"]))
    eng_str_present_not=upperFirstChar("{p1} {dn} {v} {p2} {p3} {o}.".format(p1=p1["subject"],dn=do_not_present_str,v=v["present"],p2=p2["object"],p3=p3["own"],o=o["raw"]))
    eng_str_past_not=upperFirstChar("{p1} didn't {v} {p2} {p3} {o}.".format(p1=p1["subject"],v=v["present"],p2=p2["object"],p3=p3["own"],o=o["raw"]))
    eng_str_future_not=upperFirstChar("{p1} will not {v} {p2} {p3} {o}.".format(p1=p1["subject"],v=v["present"],p2=p2["object"],p3=p3["own"],o=o["raw"]))

    return {
        "present":(s,eng_str_present),
        "past":(Phrase.past(s),eng_str_past),
        "future":(Phrase.future(s),eng_str_future),
        "present_not":(Phrase.NOT(s),eng_str_present_not),
        "past_not":(Phrase.past(Phrase.NOT(s)),eng_str_past_not),
        "future_not":(Phrase.future(Phrase.NOT(s)),eng_str_future_not),
        }


print("02")
for p1 in person_list:
    for p2 in person_list:
        if p1!=p2:
            for p3 in person_list:
                for o in object_list:
                    out_data=sample_sentence_02(p1,p2,p3,o)
                    print("02",out_data["present"][1])
                    sc=set_data_to_corpus(sc,out_data)


def sample_sentence_03(p1,p2,p3,v2,p4,o):
    v1={"SFGPL":Verb("tell"),"present":"tell","present-3":"tells","past":"told"}

    s=Noun.give(p1["SFGPL"],v1["SFGPL"],p2["SFGPL"],Phrase.past(Noun.doT(p3["SFGPL"],v2["SFGPL"],Noun.have(p4["SFGPL"],Verb.none(),DeterminerN.stressed(o["SFGPL"])))))

    verb_present_str=v["present"] if p1["type"]!=(3,False) else v1["present-3"]
    do_not_present_str="don't" if p1["type"]!=(3,False) else "doesn't"

    
    eng_str_present=upperFirstChar("{p1} {v1} {p2} that {p3} {v2} {p4} {o}.".format(p1=p1["subject"],v1=verb_present_str,p2=p2["object"],p3=p3["subject"],v2=v2["past"],p4=p4["own"],o=o["raw"]))
    eng_str_past=upperFirstChar("{p1} {v1} {p2} that {p3} {v2} {p4} {o}.".format(p1=p1["subject"],v1=v1["past"],p2=p2["object"],p3=p3["subject"],v2=v2["past"],p4=p4["own"],o=o["raw"]))
    eng_str_future=upperFirstChar("{p1} will {v1} {p2} that {p3} {v2} {p4} {p4} {o}.".format(p1=p1["subject"],v1=v1["present"],p2=p2["object"],p3=p3["subject"],v2=v2["past"],p4=p4["own"],o=o["raw"]))
    eng_str_present_not=upperFirstChar("{p1} {dn} {v1} {p2} that {p3} {v2} {p4} {o}.".format(p1=p1["subject"],dn=do_not_present_str,v1=v1["present"],p2=p2["object"],p3=p3["subject"],v2=v2["past"],p4=p4["own"],o=o["raw"]))
    eng_str_past_not=upperFirstChar("{p1} didn't {v1} {p2} that {p3} {v2} {p4} {o}.".format(p1=p1["subject"],v1=v1["present"],p2=p2["object"],p3=p3["subject"],v2=v2["past"],p4=p4["own"],o=o["raw"]))
    eng_str_future_not=upperFirstChar("{p1} will not {v1} {p2} that {p3} {v2} {p4} {o}.".format(p1=p1["subject"],v1=v1["present"],p2=p2["object"],p3=p3["subject"],v2=v2["past"],p4=p4["own"],o=o["raw"]))

    return {
        "present":(s,eng_str_present),
        "past":(Phrase.past(s),eng_str_past),
        "future":(Phrase.future(s),eng_str_future),
        "present_not":(Phrase.NOT(s),eng_str_present_not),
        "past_not":(Phrase.past(Phrase.NOT(s)),eng_str_past_not),
        "future_not":(Phrase.future(Phrase.NOT(s)),eng_str_future_not),
        }


for p1 in person_list:
    for p2 in person_list:
        if p1!=p2:
            for p3 in person_list:
                for v2 in verb_doT_list:
                    for p4 in person_list:
                        for o in object_list:
                            out_data=sample_sentence_03(p1,p2,p3,v2,p4,o)
                            print("03",out_data["present"][1])
                            sc=set_data_to_corpus(sc,out_data)

tmp_str=sc.toStringSFGPL(opt_str="\n")
print(tmp_str)

sc.saveJson(OUT_DIR+"sample02.json")
json_obj=SFGPLCorpus.readJson(OUT_DIR+"sample02.json")
