import sys
sys.path.append("")

from SFGPL import *
import os

OUT_DIR="out/"

void_func=lambda a:a

os.makedirs(OUT_DIR,exist_ok=True)

sc=SFGPLCorpus()

#Double quotation marks (") and one-byte spaces ( ) cannot be used. Care must also be taken when using single quotation marks (') at the beginning and end.
symbols=["'",":",";","_","　"]

format_texts=[
    "{x}",
    "A{x}",
    "{x}A",
    "A{x}A",

    "{x}{x}",
    "A{x}{x}",
    "{x}A{x}",
    "{x}{x}A",
    "A{x}A{x}",
    "A{x}{x}A",
    "{x}A{x}A",
    "A{x}A{x}A",
]

for s in symbols:
    for f in format_texts:
        t=f.format(x=s)
        sc.setCorpus(
            Noun.eq(Noun(t),Verb.none(),Noun("B")),
            t,
        )

tmp_str=sc.toStringSFGPL(opt_str="\n")
#print(tmp_str)

sc.saveJson(OUT_DIR+"testSymbol.json")

#Clear defined functions
LangFunc.clearDict()

json_obj=SFGPLCorpus.readJson(OUT_DIR+"testSymbol.json")

json_str=json_obj.toStringSFGPL(opt_str="\n")
print(json_str)

print(len(json_obj))
