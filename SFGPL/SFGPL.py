import SFGPL.stackcmd as stackcmd
import SFGPL.dict
import SFGPL.__version__
import re
import json
import csv
import math
import sys
import os
import collections

#SFGPL version
SFGPL_VERSION=SFGPL.__version__.__version__

#If your code gives the error 'RecursionError: maximum recursion depth exceeded in comparison', you may be able to solve this by increasing the value here.
RECURSION_LIMIT=5000
sys.setrecursionlimit(RECURSION_LIMIT)

#Class for error statements

class SFGPLError():
    ARG_STRING=lambda arg : "\n\t=> "+str(arg)

    TYPE_ERROR_SYNTAX=lambda arg : "[Error 101] : "+"There are type error in SFGPL syntax"+SFGPLError.ARG_STRING(arg)
    ARG_IS_WRONG=lambda arg : "[Error 102] : "+"Arg is wrong"+SFGPLError.ARG_STRING(arg)
    BOOLLIST_FLOAT_ERROR=lambda arg : "[Error 103] : "+"The argument \"a\" of BoolList.Folat function must be of type BoolList and must have a length of 32"+SFGPLError.ARG_STRING(arg)


#Class for generic SFGPL word
class LangObj():
    #String between words 
    SPLIT_STR=" "

    #Setting end string
    END_STR=";"

    AUTOCOMPLETION_FLAG=True
    
    def _getSelfClass():
        return {"self":LangObj,"self_name":"LangObj","base":LangObj}

    #SFGPL words List
    KEY_LIST=SFGPL.dict.SFGPL_DICT_DATA

    #Print type error in SFGPL syntax
    def printTypeError(arg):
        print(SFGPLError.TYPE_ERROR_SYNTAX(arg))

    def __init__(self,arg,bool_value=None):
        self._setWords([],arg)
        self._bool_value=bool_value

    #Set and Objectification words
    def _setWords(self,new_obj_str,arg):
        if(isinstance(arg,list)):
            self.words=arg
        elif(isinstance(arg,str)):
            if(LangObj.AUTOCOMPLETION_FLAG):
                if(not(arg[0]=="'" and arg[-1]=="'")):
                    arg="'"+arg+"'"
            self.words=[new_obj_str,arg]
        else:
            self.words=None
            print(SFGPLError.ARG_IS_WRONG(arg))

    #Get the original word
    def getWords(self):
        return self.words
    
    def _checkTypeOf2obj(a,b):
        return type(a)._getSelfClass()["base"] == type(b)._getSelfClass()["base"]
    
    def _checkTypeOf3obj(a,b,c):
        return type(a)._getSelfClass()["base"] == type(b)._getSelfClass()["base"] and type(a)._getSelfClass()["base"] == type(c)._getSelfClass()["base"]

    def _getKeyOfDict(func_str):
        for key in LangObj.KEY_LIST:
            if(LangObj.KEY_LIST[key]["func"]==func_str):
                return key

    def getBool(self):
        return self._bool_value

    #To Strings of SFGPL
    def __str__(self):
        strwords=[str(d) for d in self.words]
        return LangObj.SPLIT_STR.join(strwords)

    def NOT(a):
        func_str="LangObj.NOT"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        bool_value=Bool.defNOT(a.getBool())
        return (type(a))(arg,bool_value=bool_value)

    def Because(a,b):
        func_str="LangObj.Because"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(LangObj._checkTypeOf2obj(a,b)):
            return (type(a))(arg)
        else:
            LangObj.printTypeError(arg)

    def IF(a,b):
        func_str="LangObj.IF"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(LangObj._checkTypeOf2obj(a,b)):
            return (type(a))(arg)
        else:
            LangObj.printTypeError(arg)

    def So(a,b):
        func_str="LangObj.So"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(LangObj._checkTypeOf2obj(a,b)):
            return (type(a))(arg)
        else:
            LangObj.printTypeError(arg)
            
    def But(a,b):
        func_str="LangObj.But"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(LangObj._checkTypeOf2obj(a,b)):
            return (type(a))(arg)
        else:
            LangObj.printTypeError(arg)

    def AND(a,b):
        func_str="LangObj.AND"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(LangObj._checkTypeOf2obj(a,b)):
            bool_value=Bool.defAND(a.getBool(),b.getBool())
            return (type(a))(arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)

    def OR(a,b):
        func_str="LangObj.OR"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(LangObj._checkTypeOf2obj(a,b)):
            bool_value=Bool.defOR(a.getBool(),b.getBool())
            return (type(a))(arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)

    def IFELSE(a,b,c):
        func_str="LangObj.IFELSE"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c]
        if(LangObj._checkTypeOf3obj(a,b,c)):
            return (type(a))(arg)
        else:
            LangObj.printTypeError(arg)

    def NAND(a,b):
        func_str="LangObj.NAND"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(LangObj._checkTypeOf2obj(a,b)):
            bool_value=Bool.defNAND(a.getBool(),b.getBool())
            return (type(a))(arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)

    def NOR(a,b):
        func_str="LangObj.NOR"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(LangObj._checkTypeOf2obj(a,b)):
            bool_value=Bool.defNOR(a.getBool(),b.getBool())
            return (type(a))(arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)


#Class for nouns in SFGPL
class Noun(LangObj):
    
    def _getSelfClass():
        return {"self":Noun,"self_name":"Noun","base":Noun}
    
    def __init__(self,arg,bool_value=None):
        func_str="Noun"
        key=LangObj._getKeyOfDict(func_str)
        self._setWords(key,arg)
        self._bool_value=bool_value
        
    def V2N(a):
        func_str="Noun.V2N"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Verb)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def M2N(a):
        func_str="Noun.M2N"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Modifier)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
    
    def none():
        func_str="Noun.none"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Noun(arg)

    def eq(a,f,b):
        func_str="Noun.eq"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)
    
    def haveP(a,f,b):
        func_str="Noun.haveP"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Modifier)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def have(a,f,b):
        func_str="Noun.have"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def belong(a,f,b):
        func_str="Noun.belong"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def gt(a,f,b,c):
        func_str="Noun.gt"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Modifier) and isinstance(c,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def do(a,f):
        func_str="Noun.do"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f]
        if(isinstance(a,Noun) and isinstance(f,Verb)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def doT(a,f,b):
        func_str="Noun.doT"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def give(a,f,b,c):
        func_str="Noun.give"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun) and isinstance(c,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def makeN(a,f,b,c):
        func_str="Noun.makeN"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun) and isinstance(c,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def makeM(a,f,b,c):
        func_str="Noun.makeM"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        if(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun) and isinstance(c,Modifier)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    def Hearsay(a,b):
        func_str="Noun.Hearsay"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(isinstance(a,Noun) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)


#Class for phrases in SFGPL
class Phrase(Noun):
    
    def _getSelfClass():
        return {"self":Phrase,"self_name":"Phrase","base":Noun}
    
    def __init__(self,arg,bool_value=None):
        super().__init__(arg)
        self._bool_value=bool_value

    def interrogative(a):
        func_str="Phrase.interrogative"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Phrase)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)
    
    def imperative(a):
        func_str="Phrase.imperative"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Phrase)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)
    
    def past(a):
        func_str="Phrase.past"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Phrase)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)
        
    def future(a):
        func_str="Phrase.future"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Phrase)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)


#Class for verbs in SFGPL
class Verb(LangObj):
    
    def _getSelfClass():
        return {"self":Verb,"self_name":"Verb","base":Verb}
    
    def __init__(self,arg,bool_value=None):
        func_str="Verb"
        key=LangObj._getKeyOfDict(func_str)
        self._setWords(key,arg)
        self._bool_value=bool_value
        
    def M2V(a):
        func_str="Verb.M2V"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Modifier)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)

    def N2V(a):
        func_str="Verb.N2V"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)

    def none():
        func_str="Verb.none"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)
    
    def add(a,b):
        func_str="Verb.add"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(isinstance(a,Verb) and isinstance(b,Modifier)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    def passive(a):
        func_str="Verb.passive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    def progressive(a):
        func_str="Verb.progressive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    def perfective(a):
        func_str="Verb.perfective"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
    

#Class for modifiers in SFGPL
class Modifier(LangObj):
    
    def _getSelfClass():
        return {"self":Modifier,"self_name":"Modifier","base":Modifier}
    
    def __init__(self,arg,bool_value=None):
        func_str="Modifier"
        key=LangObj._getKeyOfDict(func_str)
        self._setWords(key,arg)
        self._bool_value=bool_value
        
    def N2M(a):
        func_str="Modifier.N2M"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)
        
    def V2M(a):
        func_str="Modifier.V2M"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Verb)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)

    def none():
        func_str="Modifier.none"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    
    def add(a,b):
        func_str="Modifier.add"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(isinstance(a,Modifier) and isinstance(b,Modifier)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)

    def Neg(a):
        func_str="Modifier.Neg"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Modifier)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)


#Class for determiners of nouns in SFGPL
class DeterminerN():

    def _getSelfClass():
        return {"self":DeterminerN,"self_name":"DeterminerN"}
        
    def biology(a):
        func_str="DeterminerN.biology"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def thing(a):
        func_str="DeterminerN.thing"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def time(a):
        func_str="DeterminerN.time"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def place(a):
        func_str="DeterminerN.place"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def reason(a):
        func_str="DeterminerN.reason"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def method(a):
        func_str="DeterminerN.method"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def human(a):
        func_str="DeterminerN.human"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def animal(a):
        func_str="DeterminerN.animal"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def plant(a):
        func_str="DeterminerN.plant"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def material(a):
        func_str="DeterminerN.material"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def start(a):
        func_str="DeterminerN.start"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def end(a):
        func_str="DeterminerN.end"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def section(a):
        func_str="DeterminerN.section"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def In(a):
        func_str="DeterminerN.In"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def Out(a):
        func_str="DeterminerN.Out"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def above(a):
        func_str="DeterminerN.above"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def below(a):
        func_str="DeterminerN.below"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def on(a):
        func_str="DeterminerN.on"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def right(a):
        func_str="DeterminerN.right"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def left(a):
        func_str="DeterminerN.left"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def affect(a):
        func_str="DeterminerN.affect"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def affected(a):
        func_str="DeterminerN.affected"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def near(a):
        func_str="DeterminerN.near"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def move(a):
        func_str="DeterminerN.move"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def stop(a):
        func_str="DeterminerN.stop"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def all(a):
        func_str="DeterminerN.all"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def many(a):
        func_str="DeterminerN.many"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def some(a):
        func_str="DeterminerN.some"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def one(a):
        func_str="DeterminerN.one"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def plural(a):
        func_str="DeterminerN.plural"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def stressed(a):
        func_str="DeterminerN.stressed"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def possessive(a):
        func_str="DeterminerN.possessive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def reflexive(a):
        func_str="DeterminerN.reflexive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def etc(a):
        func_str="DeterminerN.etc"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def abstract(a):
        func_str="DeterminerN.abstract"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def front(a):
        func_str="DeterminerN.front"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def behind(a):
        func_str="DeterminerN.behind"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    def future(a):
        func_str="DeterminerN.future"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def past(a):
        func_str="DeterminerN.past"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def now(a):
        func_str="DeterminerN.now"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def male(a):
        func_str="DeterminerN.male"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    def female(a):
        func_str="DeterminerN.female"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)


#Class for pronouns in SFGPL
class Pronoun(Noun):
    
    def _getSelfClass():
        return {"self":Pronoun,"self_name":"Pronoun","base":Noun}
    
    def __init__(self,arg,bool_value=None):
        super().__init__(arg)
        self._bool_value=bool_value

    def I():
        func_str="Pronoun.I"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)

    def you():
        func_str="Pronoun.you"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    def he():
        func_str="Pronoun.he"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    def proximal():
        func_str="Pronoun.proximal"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    def distal():
        func_str="Pronoun.distal"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    def interrogative():
        func_str="Pronoun.interrogative"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    def indefinite():
        func_str="Pronoun.indefinite"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)


#Class for words of Verb in SFGPL
class WordV():

    def create():
        func_str="WordV.create"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    def destroy():
        func_str="WordV.destroy"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    def act():
        func_str="WordV.act"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    def turn():
        func_str="WordV.turn"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    def receive():
        func_str="WordV.receive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    def stimulate():
        func_str="WordV.stimulate"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    def exist():
        func_str="WordV.exist"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    def use():
        func_str="WordV.use"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    def change():
        func_str="WordV.change"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)
    

#Class for words of Modifier in SFGPL
class WordM():
    
    def big():
        func_str="WordM.big"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    
    def near():
        func_str="WordM.near"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    
    def good():
        func_str="WordM.good"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    
    def bright():
        func_str="WordM.bright"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    

#Class for Bool in SFGPL
class Bool(LangObj):
    
    def _getSelfClass():
        return {"self":Bool,"self_name":"Bool","base":Bool}
    
    def __init__(self,arg,bool_value=None):
        super().__init__(arg)
        self._bool_value=bool_value

    def defNAND(bool_a:bool,bool_b:bool):
        if((not isinstance(bool_a,bool)) or (not isinstance(bool_b,bool))):
            return None
        elif(bool_a and bool_b):
            return False
        else:
            return True

    def defNOT(a:bool):
        return Bool.defNAND(a,a)

    def defAND(a:bool,b:bool):
        return Bool.defNOT(Bool.defNAND(a,b))

    def defOR(a:bool,b:bool):
        return Bool.defNAND(Bool.defNOT(a),Bool.defNOT(b))

    def defNOR(a:bool,b:bool):
        return Bool.defNOT(Bool.defOR(a,b))


    def false():
        func_str="Bool.false"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Bool(arg,False)

    def true():
        func_str="Bool.true"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Bool(arg,True)

    def B2N(a,b):
        func_str="Bool.B2N"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(isinstance(a,Noun) and isinstance(b,Bool)):
            return Noun(arg,bool_value=b.getBool())
        else:
            LangObj.printTypeError(arg)
        

#Class for BoolList in SFGPL
class BoolList(Noun):
    CLASS_TYPE_NATURAL_NUM="NaturalNum"
    CLASS_TYPE_INT="Int"
    CLASS_TYPE_FLOAT="Float"
    CLASS_TYPE_ASCII="ASCII"


    def _getSelfClass():
        return {"self":BoolList,"self_name":"BoolList","base":Noun}
    
    def __init__(self,arg=None,bool_list=[],bool_value=None,class_type=None):
        func_str="BoolList"
        key=LangObj._getKeyOfDict(func_str)

        if(arg==None):
            arg_tmp=[key]
        else:
            arg_tmp=arg            
        self._setWords([],arg_tmp)
        self._bool_value=bool_value
        self.__class_type=class_type
        self.__bool_list=bool_list

    def boolLen(self):
        return len(self.__bool_list)

    def __boolList2NaturalInt(bl):
        sum=0
        for i in range(len(bl)):
            sum+=(2**(len(bl)-1-i))*(1 if bl[i] else 0)
        return sum

    def getBoolList(self):
        return self.__bool_list
    
    def getBinStr(self):
        tmp_list=["1" if b else "0" for b in self.getBoolList()]
        return "".join(tmp_list)
    
    def __getNaturalInt(self):
        return BoolList.__boolList2NaturalInt(self.getBoolList())
    
    def __getInt(self):
        tmp_bl=self.__bool_list[1:]
        if(self.__bool_list[0]==False):
            return BoolList.__boolList2NaturalInt(tmp_bl)
        else:
            new_tmp_bl=[not(b) for b in tmp_bl]
            return -1*(BoolList.__boolList2NaturalInt(new_tmp_bl)+1)
    
    def __getFloat32(self):
        bl=self.__bool_list
        sign=bl[0]
        exponent=bl[1:9]
        fraction=bl[9:]

        e_num=BoolList.__boolList2NaturalInt(exponent)
        
        len_fraction=len(fraction)
        bn_sum=0
        for i in range(len_fraction):
            bn_sum+=(2**(-1*(i+1)))*fraction[i]

        return (-1 if sign else 1)*(1+bn_sum)*(2**(e_num-127))

    def binstr32ToBoolList(bin_str:str):
        if(len(bin_str)==32):
            counter=1
            bl_list=[]
            bl_tmp_list=[]
            for bi in bin_str:
                bl_tmp_list.append(Bool.true() if bi=="1" else Bool.false())
                if(counter%8==0):
                    bl_list.append(bl_tmp_list)
                    bl_tmp_list=[]
                counter+=1

            bl_byte_i=[BoolList.byte(*bli) for bli in bl_list]

            return BoolList.add(BoolList.add(bl_byte_i[0],bl_byte_i[1]),BoolList.add(bl_byte_i[2],bl_byte_i[3]))
        else:
            return None
    
    def get(self):
        if(self.__class_type==None):
            return self.getBoolList()
        elif(self.__class_type==BoolList.CLASS_TYPE_NATURAL_NUM):
            return self.__getNaturalInt()
        elif(self.__class_type==BoolList.CLASS_TYPE_INT):
            return self.__getInt()
        elif(self.__class_type==BoolList.CLASS_TYPE_FLOAT):
            return self.__getFloat32()
        elif(self.__class_type==BoolList.CLASS_TYPE_ASCII):
            return chr(self.__getNaturalInt())

    def append(a,b):
        func_str="BoolList.append"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(isinstance(a,BoolList) and isinstance(b,Bool)):
            bool_list=a.getBoolList()+[b.getBool()]
            return BoolList(arg=arg,bool_list=bool_list)
        else:
            LangObj.printTypeError(arg)

    def add(a,b):
        func_str="BoolList.add"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(isinstance(a,BoolList) and isinstance(b,BoolList)):
            bool_list=a.getBoolList()+b.getBoolList()
            return BoolList(arg=arg,bool_list=bool_list)
        else:
            LangObj.printTypeError(arg)

    def twoBit(a,b):
        func_str="BoolList.twoBit"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        if(isinstance(a,Bool) and isinstance(b,Bool)):
            bool_list=[a.getBool(),b.getBool()]
            return BoolList(arg=arg,bool_list=bool_list)
        else:
            LangObj.printTypeError(arg)

    def fourBit(a,b,c,d):
        func_str="BoolList.fourBit"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c,d]
        if(isinstance(a,Bool) and isinstance(b,Bool) and isinstance(c,Bool) and isinstance(d,Bool)):
            bool_list=[a.getBool(),b.getBool(),c.getBool(),d.getBool()]
            return BoolList(arg=arg,bool_list=bool_list)
        else:
            LangObj.printTypeError(arg)

    def byte(x1,x2,x3,x4,x5,x6,x7,x8):
        func_str="BoolList.byte"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,x1,x2,x3,x4,x5,x6,x7,x8]
        if(isinstance(x1,Bool) and isinstance(x2,Bool) and isinstance(x3,Bool) and isinstance(x4,Bool) and isinstance(x5,Bool) and isinstance(x6,Bool) and isinstance(x7,Bool) and isinstance(x8,Bool)):
            bool_list=[x1.getBool(),x2.getBool(),x3.getBool(),x4.getBool(),x5.getBool(),x6.getBool(),x7.getBool(),x8.getBool()]
            return BoolList(arg=arg,bool_list=bool_list)
        else:
            LangObj.printTypeError(arg)

    def NaturalNum(a):
        func_str="BoolList.NaturalNum"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,BoolList)):
            bool_list=a.getBoolList()
            class_type=BoolList.CLASS_TYPE_NATURAL_NUM
            return BoolList(arg=arg,bool_list=bool_list,class_type=class_type)
        else:
            LangObj.printTypeError(arg)

    def Int(a):
        func_str="BoolList.Int"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,BoolList)):
            bool_list=a.getBoolList()
            class_type=BoolList.CLASS_TYPE_INT
            return BoolList(arg=arg,bool_list=bool_list,class_type=class_type)
        else:
            LangObj.printTypeError(arg)

    def Float(a):
        func_str="BoolList.Float"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,BoolList)):
            if(a.boolLen()==32):
                bool_list=a.getBoolList()
                class_type=BoolList.CLASS_TYPE_FLOAT
                return BoolList(arg=arg,bool_list=bool_list,class_type=class_type)
            else:
                print(SFGPLError.BOOLLIST_FLOAT_ERROR(arg))
        else:
            LangObj.printTypeError(arg)

    def ASCII(a):
        func_str="BoolList.ASCII"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        if(isinstance(a,BoolList)):
            bool_list=a.getBoolList()
            class_type=BoolList.CLASS_TYPE_ASCII
            return BoolList(arg=arg,bool_list=bool_list,class_type=class_type)
        else:
            LangObj.printTypeError(arg)



#A class with a collection of functions to support generation, display, etc.
class SFGPLLib():

    #Preset config for FuncStr
    FUNC_STR_CONFIG_A={"func":"word","before_cmd":"","begin":"(","end":")","split":"\n","word_begin":"","word_end":"","zero_args_begin_and_end_flag":False}

    #Preset config for indentString
    INDENT_STRING_CONFIG_DEFAULT={"before_char":"","indent_base":" ","indent_num":2,"need_add_indent":["("],"need_del_indent":[")"]}
    INDENT_STRING_CONFIG_MD_OUT={"before_char":"- ","indent_base":" ","indent_num":2,"need_add_indent":["("],"need_del_indent":[")"]}


    #Convert SFGPL strings to Python objects or commands
    def str2CMD(str,toObj=True,result_str_config=stackcmd.StackCMD.result_str_config_defalut):
        cmdstr=stackcmd.StackCMD.stackCMD(cmdlist=LangObj.KEY_LIST,cmdline=str,result_str_config=result_str_config,splitstr=LangObj.SPLIT_STR)
        return  eval(cmdstr) if toObj else cmdstr

    #Output strings according to config
    def FuncStr(obj:LangObj,result_str_config={}):
        return SFGPLLib.str2CMD(str(obj),toObj=False,result_str_config=result_str_config)
        
    #Output structured strings in SFGPL syntax in Markdown list format
    def structuredStrMDList(obj:LangObj):
        return SFGPLLib.delSpaceLine(SFGPLLib.indentString(SFGPLLib.FuncStr(obj,result_str_config=SFGPLLib.FUNC_STR_CONFIG_A),config=SFGPLLib.INDENT_STRING_CONFIG_MD_OUT).replace("(","").replace(")",""))
        
    #Save structured strings in SFGPL syntax in Markdown list format
    def SaveMDListFile(output_path:str,obj:LangObj):
        outstr=SFGPLLib.structuredStrMDList(obj)
        with open(output_path,mode='w',encoding="utf-8") as f:
            f.write(outstr)
        
    #Function to delete lines with only blank spaces
    def delSpaceLine(in_str):
        return str(re.sub("(\n\s*\n)","\n",in_str)).strip()

    #Function for indenting a string
    def indentString(input_str,config=INDENT_STRING_CONFIG_DEFAULT):
        indent=""
        result=""+config["before_char"]
        
        for char in input_str:
            if(char in config["need_add_indent"]):
                result+="\n"+indent+char
                indent+=config["indent_base"]*config["indent_num"]
                result+="\n"+indent+config["before_char"]
            elif(char in config["need_del_indent"]):
                indent=indent[:-1*config["indent_num"]]
                result+="\n"+indent
                if(char not in config["need_del_indent"]):
                    result+=config["before_char"]
                result+=char
            elif(char=="\n"):
                result+=char+indent+config["before_char"]
            else:
                result+=char
        return SFGPLLib.delSpaceLine(result)
    
    #Function to check if SFPGL objects are equal
    def eqSFGPL(obj1:LangObj,obj2:LangObj):
        return str(obj1)==str(obj2)

    #Functions for validating SFGPL objects
    def checkObjOfSFGPL(obj:LangObj):
        converted_obj=SFGPLLib.str2CMD(str(obj))
        return (obj,converted_obj)

    #Convert Python objects to SFGPL strings of multi-lines
    def toMultiLineString(*objs,opt_str=""):
        rstr=""
        for obj in objs:
            if(isinstance(obj,Noun)):
                rstr+=str(obj)+LangObj.END_STR+opt_str
            else:
                return None
        return rstr
    
    #Convert SFGPL strings of multi-lines to Python objects or commands
    def multiLineStr2CMD(instr,toObj=True,result_str_config=stackcmd.StackCMD.result_str_config_defalut):
        instr=instr.strip()
        split_str_list=instr.split(LangObj.END_STR)
        robj=[]
        
        for s in split_str_list:
            s=s.strip()
            if(s!=""):
                robj.append(SFGPLLib.str2CMD(s,toObj=toObj,result_str_config=result_str_config))
        return robj

#Class for SFGPL Corpus
class SFGPLCorpus():
    
    def __init__(self,sfgpl_obj_list:list=[],translation_str_list:list=[]):
        self.sfgpl_obj_list=[]
        self.translation_str_list=[]
        if(isinstance(sfgpl_obj_list,list) and isinstance(translation_str_list,list)):
            if(len(sfgpl_obj_list)==len(translation_str_list)):
                self.sfgpl_obj_list=sfgpl_obj_list
                self.translation_str_list=translation_str_list

    def __str__(self):
        return self.toStringSFGPL()
    
    def __len__(self):
        return len(self.sfgpl_obj_list)
    
    def __sub_add(self,obj):
        if(isinstance(obj,SFGPLCorpus)):
            s=self.getAll()
            o=obj.getAll()
            return {"sfgpl_obj_list":s["sfgpl_obj_list"]+o["sfgpl_obj_list"],"translation_str_list":s["translation_str_list"]+o["translation_str_list"]}
        else:
            return s
    
    def __add__(self,obj):
        d=self.__sub_add(obj)
        return SFGPLCorpus(sfgpl_obj_list=d["sfgpl_obj_list"],translation_str_list=d["translation_str_list"])

    #Get all data
    def getAll(self,mode="ostv"):
        rlist={}

        #version
        if("v" in mode):
            rlist["version"]=SFGPL_VERSION

        #object mode
        if("o" in mode):
            rlist["sfgpl_obj_list"]=self.sfgpl_obj_list
        
        #string mode
        if("s" in mode):
            rlist["sfgpl_str_list"]=list(map(str,self.sfgpl_obj_list))
        
        #translation mode
        if("t" in mode):
            rlist["translation_str_list"]=self.translation_str_list
        
        return rlist 

    #Get data of index
    def getIndex(self,index):
        if(index<0):
            self.__len__()+index
        return {"sfgpl_obj":self.sfgpl_obj_list[index],"translation_str":self.translation_str_list[index]}

    #Get Parallel translation (SFGPL String / Translation String)
    def getParaTranslationString(self,index):
        return (str(self.sfgpl_obj_list[index]),self.translation_str_list[index])
    
    #Append a sentence
    def append(self,sfgpl_obj:LangObj,translation_str:str):
        self.sfgpl_obj_list.append(sfgpl_obj)
        self.translation_str_list.append(translation_str)

    #Insert a sentence
    def insert(self,index:int,sfgpl_obj:LangObj,translation_str:str):
        self.sfgpl_obj_list.insert(index,sfgpl_obj)
        self.translation_str_list.insert(index,translation_str)

    #Extend a sentence
    def extend(self,obj):
        d=self.__sub_add(obj)
        self.sfgpl_obj_list=d["sfgpl_obj_list"]
        self.translation_str_list=d["translation_str_list"]

    #Convert SFGPL object list to SFGPL string
    def toStringSFGPL(self,opt_str=""):
        return SFGPLLib.toMultiLineString(*self.sfgpl_obj_list,opt_str=opt_str)

    #Convert translation string  list to string
    def toStringTranslation(self,opt_str=""):
        return opt_str.join(self.translation_str_list)
    
    #Save json file of SFGPL
    def saveJson(self,path:str,indent:int=4):
        with open(path,mode="w",encoding="utf-8") as f:
            json.dump(self.getAll(mode="stv"),f,indent=indent)

    #Read json file of SFGPL
    def readJson(path:str):
        with open(path,mode="r",encoding="utf-8") as f:
            json_data=json.load(f)
            os=list(map(SFGPLLib.str2CMD,json_data["sfgpl_str_list"]))
            ts=json_data["translation_str_list"]

            return SFGPLCorpus(sfgpl_obj_list=os,translation_str_list=ts)
        
    #Save csv file of SFGPL
    def saveCSV(self,path:str,split_str=",",newline_str="\n"):
        with open(path,mode="w",encoding="utf-8") as f:
            for i in range(self.__len__()):
                tmp_str="\""+str(self.sfgpl_obj_list[i])+"\""+split_str+"\""+self.translation_str_list[i]+"\""+newline_str
                f.write(tmp_str)

    #Save text file of SFGPL
    def saveTextFileOfSFGPL(self,path:str,opt_str:str=""):
        with open(path,mode="w",encoding="utf-8") as f:
            f.write(self.toStringSFGPL(opt_str=opt_str))

    #add a sentence of Corpus 
    def setCorpus(corpus,sfgpl_obj:LangObj,translation_str:str,print_flag:bool=False,md_out_path:str=None):
        corpus.append(sfgpl_obj=sfgpl_obj,translation_str=translation_str)
        if(print_flag):
            print(sfgpl_obj)
        if(md_out_path!=None):
            SFGPLLib.SaveMDListFile(md_out_path,sfgpl_obj)
            
    #The function to count the number of words in a corpus
    def corpusWordCount(corpus,SPLIT_WORD=" ",BEFORE_REPLACE_WORD=[";"],include_word_func=lambda x: x!=""):
        sc_str=corpus.toStringSFGPL()
        for brw_i in BEFORE_REPLACE_WORD:
            sc_str=sc_str.replace(brw_i,SPLIT_WORD)
        sc_str=sc_str.split(SPLIT_WORD)
        sc_str=[li for li in sc_str if include_word_func(li)]
        return collections.Counter(sc_str)
