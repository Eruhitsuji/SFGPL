import sys
sys.path.append("")

from SFGPL import *

s01=Noun.eq(Pronoun.I(),Verb.none(),Noun("student"))

print(s01)
print(SFGPL.SFGPLLib.checkType(str(s01)))
print(SFGPL.SFGPLLib.checkType(str(s01)+" abc"))

