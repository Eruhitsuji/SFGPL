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
import copy

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
    
    BOOLLIST_FLOAT_ERROR=lambda arg : "[Error 201] : "+"The argument \"a\" of BoolList. Float function must be of type BoolList and must have a length of 32"+SFGPLError.ARG_STRING(arg)
    
    FUNC_NAME_ERROR_DUPLICATION=lambda arg :"[Error 301] : "+"This function name already exists and cannot be defined."+SFGPLError.ARG_STRING(arg)
    FUNC_NAME_ERROR_UNDEFINED=lambda arg:"[Error 302] : "+"This function name is undefined."+SFGPLError.ARG_STRING(arg)

    VAR_NAME_ERROR_UNDEFINED=lambda arg:"[Error 401] : "+"This variable name is undefined."+SFGPLError.ARG_STRING(arg)

    NUMBERLIST_CONTROL_LIST_ERROR=lambda arg:"[Error 501] : "+"After performing arithmetic operations etc., list-related operations cannot be performed."+SFGPLError.ARG_STRING(arg)
    NUMBERLIST_IntNL2BL_FLOAT_ERROR=lambda arg:"[Error 502] : "+"This function (NumberList.IntNL2BL) requires the argument NumberList to be an integer."+SFGPLError.ARG_STRING(arg)

#Class for generic SFGPL word
class LangObj():
    #String between words 
    SPLIT_STR=" "

    #Setting end string
    END_STR=";"

    AUTOCOMPLETION_FLAG=True
    
    @staticmethod
    def _getSelfClass():
        return {"self":LangObj,"self_name":"LangObj","base":LangObj}

    #SFGPL words List
    KEY_LIST=SFGPL.dict.SFGPL_DICT_DATA

    #Print type error in SFGPL syntax
    @staticmethod
    def printTypeError(arg):
        print(SFGPLError.TYPE_ERROR_SYNTAX(arg))

    def __init__(self,arg,bool_value=None,func_mode=False):
        self._setWords([],arg)
        self._bool_value=bool_value
        self._func_mode=func_mode

    def copy(self,arg=None,bool_value=None,func_mode=None):
        if(arg==None):
            arg=self.words
        if(bool_value==None):
            bool_value=self._bool_value
        if(func_mode==None):
            func_mode=self._func_mode
        return (type(self))(arg=arg,bool_value=bool_value,func_mode=func_mode)

    @staticmethod
    def _setWordString(s:str):
        if(LangObj.AUTOCOMPLETION_FLAG):
            if(not(s[0]=="'" and s[-1]=="'")):
                return "'"+s+"'"
        return s
        

    #Set and Objectification words
    def _setWords(self,new_obj_str,arg):
        if(isinstance(arg,list)):
            self.words=arg
        elif(isinstance(arg,str)):
            arg=LangObj._setWordString(arg)
            self.words=[new_obj_str,arg]
        else:
            self.words=None
            print(SFGPLError.ARG_IS_WRONG(arg))

    #Get the original word
    def getWords(self):
        return self.words
    
    def getWordsAll(self):
        l=self.words
        r_l=[]
        for li in l:
            if(isinstance(li,LangObj)):
                l_tmp=li.getWordsAll()
                r_l.append(l_tmp)
            elif(isinstance(li,str)):
                r_l.append(li)
            else:
                r_l.append(None)
        return r_l            
    
    @staticmethod
    def _checkTypeOf2obj(a,b):
        return type(a)._getSelfClass()["base"] == type(b)._getSelfClass()["base"]
    
    @staticmethod
    def _checkTypeOf3obj(a,b,c):
        return type(a)._getSelfClass()["base"] == type(b)._getSelfClass()["base"] and type(a)._getSelfClass()["base"] == type(c)._getSelfClass()["base"]

    @staticmethod
    def _getKeyOfDict(func_str):
        for key in LangObj.KEY_LIST:
            if(LangObj.KEY_LIST[key]["func"]==func_str):
                return key

    def getBool(self):
        return self._bool_value

    def _getFuncMode(self):
        return self._func_mode
    
    @staticmethod
    def _isFuncModeOfArgs(arg):
        for ai in arg:
            if(isinstance(ai,LangObj)):
                if(ai._getFuncMode()):
                    return True
        return False

    #To Strings of SFGPL
    def __str__(self):
        strwords=[str(d) for d in self.words]
        return LangObj.SPLIT_STR.join(strwords)

    @staticmethod
    def NOT(a):
        func_str="LangObj.NOT"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        bool_value=Bool.defNOT(a.getBool())
        return (type(a))(arg,bool_value=bool_value)

    @staticmethod
    def Because(a,b):
        func_str="LangObj.Because"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]

        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf2obj(a,b)):
            return (type(a))(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def IF(a,b):
        func_str="LangObj.IF"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf2obj(a,b)):
            return (type(a))(arg,bool_value=Bool._if_fanc(a,b))
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def So(a,b):
        func_str="LangObj.So"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf2obj(a,b)):
            return (type(a))(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def But(a,b):
        func_str="LangObj.But"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf2obj(a,b)):
            return (type(a))(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def AND(a,b):
        func_str="LangObj.AND"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf2obj(a,b)):
            bool_value=Bool.defAND(a.getBool(),b.getBool())
            return (type(a))(arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def OR(a,b):
        func_str="LangObj.OR"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf2obj(a,b)):
            bool_value=Bool.defOR(a.getBool(),b.getBool())
            return (type(a))(arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def IFELSE(a,b,c):
        func_str="LangObj.IFELSE"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf3obj(a,b,c)):
            return (type(a))(arg,bool_value=Bool._if_fanc(a,b,c))
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def NAND(a,b):
        func_str="LangObj.NAND"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf2obj(a,b)):
            bool_value=Bool.defNAND(a.getBool(),b.getBool())
            return (type(a))(arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def NOR(a,b):
        func_str="LangObj.NOR"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(a))(arg,func_mode=True)
        elif(LangObj._checkTypeOf2obj(a,b)):
            bool_value=Bool.defNOR(a.getBool(),b.getBool())
            return (type(a))(arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def logicIFELSE(a,b,c):
        func_str="LangObj.logicIFELSE"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c]

        if(LangObj._isFuncModeOfArgs(arg)):
            return (type(b))(arg,func_mode=True)
        elif(isinstance(a,Bool) and isinstance(b,LangObj) and isinstance(c,LangObj)):
            if(a.getBool()):
                return b.copy(arg=arg)
            else:
                return c.copy(arg=arg)
        else:
            LangObj.printTypeError(arg)


#Class for nouns in SFGPL
class Noun(LangObj):
    
    @staticmethod
    def _getSelfClass():
        return {"self":Noun,"self_name":"Noun","base":Noun}
    
    def __init__(self,arg,bool_value=None,func_mode=False):
        func_str="Noun"
        key=LangObj._getKeyOfDict(func_str)
        self._setWords(key,arg)
        self._bool_value=bool_value
        self._func_mode=func_mode
        
    @staticmethod
    def borrowed(a,b):
        func_str="Noun.borrowed"
        key=LangObj._getKeyOfDict(func_str)
        a=LangObj._setWordString(a)
        b=LangObj._setWordString(b)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,str) and isinstance(b,str)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def V2N(a):
        func_str="Noun.V2N"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def M2N(a):
        func_str="Noun.M2N"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Modifier)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
    
    @staticmethod
    def none():
        func_str="Noun.none"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Noun(arg)

    @staticmethod
    def eq(a,f,b):
        func_str="Noun.eq"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)
    
    @staticmethod
    def haveP(a,f,b):
        func_str="Noun.haveP"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Modifier)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def have(a,f,b):
        func_str="Noun.have"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def belong(a,f,b):
        func_str="Noun.belong"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def gt(a,f,b,c):
        func_str="Noun.gt"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Modifier) and isinstance(c,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def hearSay(a,f,b,c):
        func_str="Noun.hearSay"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun) and isinstance(c,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def do(a,f):
        func_str="Noun.do"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def doT(a,f,b):
        func_str="Noun.doT"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def give(a,f,b,c):
        func_str="Noun.give"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun) and isinstance(c,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def makeN(a,f,b,c):
        func_str="Noun.makeN"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun) and isinstance(c,Noun)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def makeM(a,f,b,c):
        func_str="Noun.makeM"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,f,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(f,Verb) and isinstance(b,Noun) and isinstance(c,Modifier)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)


#Class for phrases in SFGPL
class Phrase(Noun):
    
    @staticmethod
    def _getSelfClass():
        return {"self":Phrase,"self_name":"Phrase","base":Noun}
    
    def __init__(self,arg,bool_value=None,func_mode=False):
        super().__init__(arg,bool_value=bool_value,func_mode=func_mode)

    @staticmethod
    def interrogative(a):
        func_str="Phrase.interrogative"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Phrase)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)
    
    @staticmethod
    def imperative(a):
        func_str="Phrase.imperative"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Phrase)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)
    
    @staticmethod
    def past(a):
        func_str="Phrase.past"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Phrase)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def future(a):
        func_str="Phrase.future"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Phrase(arg,func_mode=True)
        elif(isinstance(a,Phrase)):
            return Phrase(arg)
        else:
            LangObj.printTypeError(arg)


#Class for verbs in SFGPL
class Verb(LangObj):
    
    @staticmethod
    def _getSelfClass():
        return {"self":Verb,"self_name":"Verb","base":Verb}
    
    def __init__(self,arg,bool_value=None,func_mode=False):
        func_str="Verb"
        key=LangObj._getKeyOfDict(func_str)
        self._setWords(key,arg)
        self._bool_value=bool_value
        self._func_mode=func_mode
        
    @staticmethod
    def borrowed(a,b):
        func_str="Verb.borrowed"
        key=LangObj._getKeyOfDict(func_str)
        a=LangObj._setWordString(a)
        b=LangObj._setWordString(b)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,str) and isinstance(b,str)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def M2V(a):
        func_str="Verb.M2V"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Modifier)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def N2V(a):
        func_str="Verb.N2V"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def none():
        func_str="Verb.none"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)
    
    @staticmethod
    def add(a,b):
        func_str="Verb.add"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb) and isinstance(b,Modifier)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def passive(a):
        func_str="Verb.passive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def progressive(a):
        func_str="Verb.progressive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def perfective(a):
        func_str="Verb.perfective"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
    

#Class for modifiers in SFGPL
class Modifier(LangObj):
    
    @staticmethod
    def _getSelfClass():
        return {"self":Modifier,"self_name":"Modifier","base":Modifier}
    
    def __init__(self,arg,bool_value=None,func_mode=False):
        func_str="Modifier"
        key=LangObj._getKeyOfDict(func_str)
        self._setWords(key,arg)
        self._bool_value=bool_value
        self._func_mode=func_mode
        
    @staticmethod
    def borrowed(a,b):
        func_str="Modifier.borrowed"
        key=LangObj._getKeyOfDict(func_str)
        a=LangObj._setWordString(a)
        b=LangObj._setWordString(b)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Modifier(arg,func_mode=True)
        elif(isinstance(a,str) and isinstance(b,str)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def N2M(a):
        func_str="Modifier.N2M"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Modifier(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def V2M(a):
        func_str="Modifier.V2M"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Modifier(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def none():
        func_str="Modifier.none"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    
    @staticmethod
    def add(a,b):
        func_str="Modifier.add"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Modifier(arg,func_mode=True)
        elif(isinstance(a,Modifier) and isinstance(b,Modifier)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def Neg(a):
        func_str="Modifier.Neg"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Modifier(arg,func_mode=True)
        elif(isinstance(a,Modifier)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def Very(a):
        func_str="Modifier.Very"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Modifier(arg,func_mode=True)
        elif(isinstance(a,Modifier)):
            return Modifier(arg)
        else:
            LangObj.printTypeError(arg)


#Class for determiners of nouns in SFGPL
class DeterminerN():

    @staticmethod
    def _getSelfClass():
        return {"self":DeterminerN,"self_name":"DeterminerN"}
        
    @staticmethod
    def biology(a):
        func_str="DeterminerN.biology"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def thing(a):
        func_str="DeterminerN.thing"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def time(a):
        func_str="DeterminerN.time"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def place(a):
        func_str="DeterminerN.place"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def reason(a):
        func_str="DeterminerN.reason"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def method(a):
        func_str="DeterminerN.method"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def human(a):
        func_str="DeterminerN.human"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def animal(a):
        func_str="DeterminerN.animal"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def plant(a):
        func_str="DeterminerN.plant"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def material(a):
        func_str="DeterminerN.material"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def start(a):
        func_str="DeterminerN.start"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def end(a):
        func_str="DeterminerN.end"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def section(a):
        func_str="DeterminerN.section"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def In(a):
        func_str="DeterminerN.In"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def Out(a):
        func_str="DeterminerN.Out"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def above(a):
        func_str="DeterminerN.above"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def below(a):
        func_str="DeterminerN.below"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def on(a):
        func_str="DeterminerN.on"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def right(a):
        func_str="DeterminerN.right"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def left(a):
        func_str="DeterminerN.left"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def affect(a):
        func_str="DeterminerN.affect"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def affected(a):
        func_str="DeterminerN.affected"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def near(a):
        func_str="DeterminerN.near"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def move(a):
        func_str="DeterminerN.move"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def stop(a):
        func_str="DeterminerN.stop"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def all(a):
        func_str="DeterminerN.all"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def many(a):
        func_str="DeterminerN.many"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def some(a):
        func_str="DeterminerN.some"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def one(a):
        func_str="DeterminerN.one"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def plural(a):
        func_str="DeterminerN.plural"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def stressed(a):
        func_str="DeterminerN.stressed"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def possessive(a):
        func_str="DeterminerN.possessive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def reflexive(a):
        func_str="DeterminerN.reflexive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def etc(a):
        func_str="DeterminerN.etc"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def abstract(a):
        func_str="DeterminerN.abstract"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def front(a):
        func_str="DeterminerN.front"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def behind(a):
        func_str="DeterminerN.behind"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)
            
    @staticmethod
    def future(a):
        func_str="DeterminerN.future"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def past(a):
        func_str="DeterminerN.past"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def male(a):
        func_str="DeterminerN.male"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def female(a):
        func_str="DeterminerN.female"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def every(a):
        func_str="DeterminerN.every"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def each(a):
        func_str="DeterminerN.each"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def other(a):
        func_str="DeterminerN.other"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            return Noun(arg)
        else:
            LangObj.printTypeError(arg)


#Class for determiners of verbs in SFGPL
class DeterminerV():

    @staticmethod
    def _getSelfClass():
        return {"self":DeterminerV,"self_name":"DeterminerV"}
        
    @staticmethod
    def Estimation100(a):
        func_str="DeterminerV.Estimation100"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Estimation75(a):
        func_str="DeterminerV.Estimation75"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Estimation50(a):
        func_str="DeterminerV.Estimation50"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Estimation25(a):
        func_str="DeterminerV.Estimation25"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Estimation0(a):
        func_str="DeterminerV.Estimation0"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Frequency100(a):
        func_str="DeterminerV.Frequency100"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Frequency75(a):
        func_str="DeterminerV.Frequency75"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Frequency50(a):
        func_str="DeterminerV.Frequency50"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Frequency25(a):
        func_str="DeterminerV.Frequency25"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Frequency0(a):
        func_str="DeterminerV.Frequency0"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Start(a):
        func_str="DeterminerV.Start"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Condition(a):
        func_str="DeterminerV.Condition"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Complete(a):
        func_str="DeterminerV.Complete"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Continue(a):
        func_str="DeterminerV.Continue"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def End(a):
        func_str="DeterminerV.End"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def past(a):
        func_str="DeterminerV.past"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def present(a):
        func_str="DeterminerV.present"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def future(a):
        func_str="DeterminerV.future"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Possible(a):
        func_str="DeterminerV.Possible"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Ability(a):
        func_str="DeterminerV.Ability"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Will(a):
        func_str="DeterminerV.Will"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Obligation(a):
        func_str="DeterminerV.Obligation"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Necessary(a):
        func_str="DeterminerV.Necessary"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Duty(a):
        func_str="DeterminerV.Duty"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def forced(a):
        func_str="DeterminerV.forced"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def want(a):
        func_str="DeterminerV.want"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def dare(a):
        func_str="DeterminerV.dare"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def allow(a):
        func_str="DeterminerV.allow"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def easy(a):
        func_str="DeterminerV.easy"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def hard(a):
        func_str="DeterminerV.hard"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def habit(a):
        func_str="DeterminerV.habit"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Polite(a):
        func_str="DeterminerV.Polite"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Respect(a):
        func_str="DeterminerV.Respect"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def volitional(a):
        func_str="DeterminerV.volitional"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def nonVolitional(a):
        func_str="DeterminerV.nonVolitional"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Requests(a):
        func_str="DeterminerV.Requests"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Permission(a):
        func_str="DeterminerV.Permission"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)
        
    @staticmethod
    def Suggestion(a):
        func_str="DeterminerV.Suggestion"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Verb(arg,func_mode=True)
        elif(isinstance(a,Verb)):
            return Verb(arg)
        else:
            LangObj.printTypeError(arg)


#Class for pronouns in SFGPL
class Pronoun(Noun):
    
    @staticmethod
    def _getSelfClass():
        return {"self":Pronoun,"self_name":"Pronoun","base":Noun}
    
    def __init__(self,arg,bool_value=None,func_mode=False):
        super().__init__(arg,bool_value=bool_value,func_mode=func_mode)

    @staticmethod
    def I():
        func_str="Pronoun.I"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)

    @staticmethod
    def you():
        func_str="Pronoun.you"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    @staticmethod
    def he():
        func_str="Pronoun.he"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    @staticmethod
    def proximal():
        func_str="Pronoun.proximal"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    @staticmethod
    def distal():
        func_str="Pronoun.distal"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    @staticmethod
    def interrogative():
        func_str="Pronoun.interrogative"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)
    
    @staticmethod
    def indefinite():
        func_str="Pronoun.indefinite"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Pronoun(arg)


#Class for words of Verb in SFGPL
class WordV():

    @staticmethod
    def create():
        func_str="WordV.create"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    @staticmethod
    def destroy():
        func_str="WordV.destroy"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    @staticmethod
    def act():
        func_str="WordV.act"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    @staticmethod
    def turn():
        func_str="WordV.turn"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    @staticmethod
    def receive():
        func_str="WordV.receive"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    @staticmethod
    def stimulate():
        func_str="WordV.stimulate"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    @staticmethod
    def exist():
        func_str="WordV.exist"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    @staticmethod
    def use():
        func_str="WordV.use"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)

    @staticmethod
    def change():
        func_str="WordV.change"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Verb(arg)
    

#Class for words of Modifier in SFGPL
class WordM():
    
    @staticmethod
    def big():
        func_str="WordM.big"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    
    @staticmethod
    def near():
        func_str="WordM.near"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    
    @staticmethod
    def good():
        func_str="WordM.good"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    
    @staticmethod
    def bright():
        func_str="WordM.bright"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Modifier(arg)
    

#Class for Bool in SFGPL
class Bool(LangObj):
    
    @staticmethod
    def _getSelfClass():
        return {"self":Bool,"self_name":"Bool","base":Bool}
    
    def __init__(self,arg,bool_value=None,func_mode=False):
        super().__init__(arg,bool_value=bool_value,func_mode=func_mode)

    @staticmethod
    def defNAND(bool_a:bool,bool_b:bool):
        if((not isinstance(bool_a,bool)) or (not isinstance(bool_b,bool))):
            return None
        elif(bool_a and bool_b):
            return False
        else:
            return True

    @staticmethod
    def defNOT(a:bool):
        return Bool.defNAND(a,a)

    @staticmethod
    def defAND(a:bool,b:bool):
        return Bool.defNOT(Bool.defNAND(a,b))

    @staticmethod
    def defOR(a:bool,b:bool):
        return Bool.defNAND(Bool.defNOT(a),Bool.defNOT(b))

    @staticmethod
    def defNOR(a:bool,b:bool):
        return Bool.defNOT(Bool.defOR(a,b))

    @staticmethod
    def _if_fanc(a:LangObj,b:LangObj,c:LangObj=LangObj([])):
        bool_a=a.getBool()
        bool_b=b.getBool()
        bool_c=c.getBool()
        return bool_b if bool_a else bool_c

    @staticmethod
    def false():
        func_str="Bool.false"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Bool(arg,False)

    @staticmethod
    def true():
        func_str="Bool.true"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Bool(arg,True)

    @staticmethod
    def B2N(a,b):
        func_str="Bool.B2N"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Noun(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(b,Bool)):
            return Noun(arg,bool_value=b.getBool())
        else:
            LangObj.printTypeError(arg)
        

#Base class for list-based classes in SFGPL
class _BaseList(Noun):

    @staticmethod
    def __getFuncObj(func_str):
        if(func_str=="BoolList"):
            return BoolList
        elif(func_str=="LangList"):
            return LangList

    def __init__(self,arg=None,lang_list=[],bool_value=None,func_mode=False,func_str=""):
        self._func_str=func_str
        self._funcObj=(_BaseList.__getFuncObj(self._func_str))
        
        key=LangObj._getKeyOfDict(self._func_str)

        if(arg==None):
            arg_tmp=[key]
        else:
            arg_tmp=arg
        self._setWords([],arg_tmp)
        self._bool_value=bool_value
        self._func_mode=func_mode
        self._lang_list=lang_list

    def copy(self,arg=None,lang_list=None,bool_value=None,func_mode=None):
        if(arg==None):
            arg=self.words
        if(lang_list==None):
            lang_list=self._lang_list
        if(bool_value==None):
            bool_value=self._bool_value
        if(func_mode==None):
            func_mode=self._func_mode

        return (type(self))(arg=arg,lang_list=lang_list,bool_value=bool_value,func_mode=func_mode)

    def _ListLen(self):
        return len(self._lang_list)

    def _ListGet(self):
        return self._lang_list
        

#Class for BoolList in SFGPL
class BoolList(_BaseList):
    CLASS_TYPE_NATURAL_NUM="NaturalNum"
    CLASS_TYPE_INT="Int"
    CLASS_TYPE_FLOAT="Float"
    CLASS_TYPE_ASCII="ASCII"


    @staticmethod
    def _getSelfClass():
        return {"self":BoolList,"self_name":"BoolList","base":Noun}
    
    def __init__(self,arg=None,lang_list=[],bool_value=None,class_type=None,func_mode=False):
        super().__init__(arg=arg,lang_list=lang_list,bool_value=bool_value,func_mode=func_mode,func_str="BoolList")
        self.__class_type=class_type

    def copy(self,arg=None,lang_list=None,bool_value=None,class_type=None,func_mode=None):
        if(arg==None):
            arg=self.words
        if(lang_list==None):
            lang_list=self._lang_list
        if(bool_value==None):
            bool_value=self._bool_value
        if(class_type==None):
            class_type=self.__class_type
        if(func_mode==None):
            func_mode=self._func_mode

        return (type(self))(arg=arg,lang_list=lang_list,bool_value=bool_value,class_type=class_type,func_mode=func_mode)

    def boolLen(self):
        return self._ListLen()

    def __boolList2NaturalInt(bl):
        sum=0
        for i in range(len(bl)):
            sum+=(2**(len(bl)-1-i))*(1 if bl[i] else 0)
        return sum

    def getBoolList(self):
        return self._ListGet()
    
    def getBinStr(self):
        tmp_list=["1" if b else "0" for b in self.getBoolList()]
        return "".join(tmp_list)
    
    def getBytes(self,byteorder="big"):
        l=math.floor(self.boolLen()/8)
        n=self.getNaturalNumber()
        return n.to_bytes(l,byteorder=byteorder)
    
    def getNaturalNumber(self):
        return BoolList.__boolList2NaturalInt(self.getBoolList())
    
    def __getInt(self):
        tmp_bl=self._lang_list[1:]
        if(self._lang_list[0]==False):
            return BoolList.__boolList2NaturalInt(tmp_bl)
        else:
            new_tmp_bl=[not(b) for b in tmp_bl]
            return -1*(BoolList.__boolList2NaturalInt(new_tmp_bl)+1)
    
    def __getFloat32(self):
        bl=self._lang_list
        sign=bl[0]
        exponent=bl[1:9]
        fraction=bl[9:]

        e_num=BoolList.__boolList2NaturalInt(exponent)
        
        len_fraction=len(fraction)
        bn_sum=0
        for i in range(len_fraction):
            bn_sum+=(2**(-1*(i+1)))*fraction[i]

        return (-1 if sign else 1)*(1+bn_sum)*(2**(e_num-127))
    
    @staticmethod
    def _binStr2BLList(bin_str:str):
        return [x=="1" for x in bin_str]

    @staticmethod
    def _int2binStr(n:int):
        p=4
        while(True):
            if(-2**(p-1)<=n<2**(p-1)):
                break
            p*=2

        if(n>=0):
            return ("{{:0{}b}}".format(p)).format(n)
        else:
            return "{:0b}".format(n & 2**p-1)
        
    @staticmethod
    def _int2BLList(n:int):
        bin_str=BoolList._int2binStr(n)
        return BoolList._binStr2BLList(bin_str)

    @staticmethod
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
    
    @staticmethod
    def __dec2bin(num:int):
        r=[]
        while num>0:
            a=num%2
            num=num//2
            r.append(a==1)
        r.reverse()
        return r

    @staticmethod
    def dec2BoolList(num:int,msb_false_flag:bool=False):
        if(num>0):
            bl=BoolList()
            if(msb_false_flag):
                bl=BoolList.append(bl,Bool.false())
            bin_l=BoolList.__dec2bin(num)
            
            for li in bin_l:
                if(li):
                    bl=BoolList.append(bl,Bool.true())
                else:
                    bl=BoolList.append(bl,Bool.false())
            return bl
        elif(num==0):
            return BoolList.append(BoolList(),Bool.false())
        else:
            return None

    def getData(self):
        if(self.__class_type==None):
            return self.getBoolList()
        elif(self.__class_type==BoolList.CLASS_TYPE_NATURAL_NUM):
            return self.getNaturalNumber()
        elif(self.__class_type==BoolList.CLASS_TYPE_INT):
            return self.__getInt()
        elif(self.__class_type==BoolList.CLASS_TYPE_FLOAT):
            return self.__getFloat32()
        elif(self.__class_type==BoolList.CLASS_TYPE_ASCII):
            return chr(self.getNaturalNumber())

    @staticmethod
    def get(a,b):
        func_str="BoolList.get"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Bool(arg,func_mode=True)
        elif(isinstance(a,BoolList) and isinstance(b,BoolList)):
            bool_value=a.getBoolList()[b.getNaturalNumber()]
            return Bool(arg=arg,bool_value=bool_value)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def append(a,b):
        func_str="BoolList.append"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,BoolList) and isinstance(b,Bool)):
            lang_list=a.getBoolList()+[b.getBool()]
            return BoolList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def slice(a,b,c):
        func_str="BoolList.slice"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,BoolList) and isinstance(b,BoolList) and isinstance(c,BoolList)):
            lang_list=a.getBoolList()[b.getNaturalNumber():c.getNaturalNumber()+1]
            return BoolList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def add(a,b):
        func_str="BoolList.add"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,BoolList) and isinstance(b,BoolList)):
            lang_list=a.getBoolList()+b.getBoolList()
            return BoolList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def len(a):
        func_str="BoolList.len"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,BoolList)):
            tmp_bl=BoolList.dec2BoolList(a._ListLen())
            return BoolList(arg=arg,lang_list=tmp_bl.getBoolList())
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def twoBit(a,b):
        func_str="BoolList.twoBit"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,Bool) and isinstance(b,Bool)):
            lang_list=[a.getBool(),b.getBool()]
            return BoolList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def fourBit(a,b,c,d):
        func_str="BoolList.fourBit"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c,d]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,Bool) and isinstance(b,Bool) and isinstance(c,Bool) and isinstance(d,Bool)):
            lang_list=[a.getBool(),b.getBool(),c.getBool(),d.getBool()]
            return BoolList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def byte(x1,x2,x3,x4,x5,x6,x7,x8):
        func_str="BoolList.byte"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,x1,x2,x3,x4,x5,x6,x7,x8]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(x1,Bool) and isinstance(x2,Bool) and isinstance(x3,Bool) and isinstance(x4,Bool) and isinstance(x5,Bool) and isinstance(x6,Bool) and isinstance(x7,Bool) and isinstance(x8,Bool)):
            lang_list=[x1.getBool(),x2.getBool(),x3.getBool(),x4.getBool(),x5.getBool(),x6.getBool(),x7.getBool(),x8.getBool()]
            return BoolList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def NaturalNum(a):
        func_str="BoolList.NaturalNum"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,BoolList)):
            lang_list=a.getBoolList()
            class_type=BoolList.CLASS_TYPE_NATURAL_NUM
            return BoolList(arg=arg,lang_list=lang_list,class_type=class_type)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def Int(a):
        func_str="BoolList.Int"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,BoolList)):
            lang_list=a.getBoolList()
            class_type=BoolList.CLASS_TYPE_INT
            return BoolList(arg=arg,lang_list=lang_list,class_type=class_type)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def Float(a):
        func_str="BoolList.Float"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,BoolList)):
            if(a.boolLen()==32):
                lang_list=a.getBoolList()
                class_type=BoolList.CLASS_TYPE_FLOAT
                return BoolList(arg=arg,lang_list=lang_list,class_type=class_type)
            else:
                print(SFGPLError.BOOLLIST_FLOAT_ERROR(arg))
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def ASCII(a):
        func_str="BoolList.ASCII"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,BoolList)):
            lang_list=a.getBoolList()
            class_type=BoolList.CLASS_TYPE_ASCII
            return BoolList(arg=arg,lang_list=lang_list,class_type=class_type)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def IntBL2NL(a):
        func_str="BoolList.IntBL2NL"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,BoolList)):
            number=a.__getInt()
            return NumberList(arg=arg,number=number)
        else:
            LangObj.printTypeError(arg)


#Class for LangFunc in SFGPL
class LangFunc(Noun):

    _FUNC_LIST={}

    @staticmethod
    def _getSelfClass():
        return {"self":LangFunc,"self_name":"LangFunc","base":Noun}

    @staticmethod
    def clearDict():
        LangFunc._FUNC_LIST={}
    
    def __init__(self,arg,bool_value=None,func_mode=False):
        super().__init__(arg,bool_value=bool_value,func_mode=func_mode)

    @staticmethod
    def __createFuncObjAtRuntime(a_str:str,b_str:str):
        arg_str=LangObj._getKeyOfDict("LangFunc.arg")
        raw_str=LangFunc._FUNC_LIST[a_str]
        raw_str_split_list=raw_str.split()
        
        func_str_list=[]
        for rssli in raw_str_split_list:
            tmp_str=""
            if(rssli==arg_str):
                tmp_str=b_str
            else:
                tmp_str=rssli
            func_str_list.append(tmp_str)
        func_str=" ".join(func_str_list)

        r_obj=SFGPLLib.str2CMD(func_str)
        return r_obj

    @staticmethod
    def setFunc(a,b):
        func_str="LangFunc.setFunc"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(isinstance(a,Noun) and isinstance(b,LangList)):
            a_str=str(a)
            if(a_str not in LangFunc._FUNC_LIST):
                LangFunc._FUNC_LIST[a_str]=str(b)
                return LangFunc(arg)
            else:
                print(SFGPLError.FUNC_NAME_ERROR_DUPLICATION(arg))
        else:
            LangObj.printTypeError(arg)
    
    @staticmethod
    def arg():
        func_str="LangFunc.arg"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return LangList(arg,func_mode=True)

    @staticmethod
    def runFunc(a,b):
        func_str="LangFunc.runFunc"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return LangList(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(b,LangList)):
            a_str=str(a)
            b_str=str(b)
            if(a_str not in LangFunc._FUNC_LIST):
                print(SFGPLError.FUNC_NAME_ERROR_UNDEFINED(arg))
            else:
                func_result=LangFunc.__createFuncObjAtRuntime(a_str,b_str)
                return LangList(arg,bool_value=func_result.getBool(),lang_list=func_result.getLangList())
        else:
            LangObj.printTypeError(arg)

#Class for LangVar in SFGPL
class LangVar(Noun):

    _VAR_LIST={}

    @staticmethod
    def _getSelfClass():
        return {"self":LangVar,"self_name":"LangVar","base":Noun}

    @staticmethod
    def clearDict():
        LangVar._VAR_LIST={}
    
    def __init__(self,arg,bool_value=None,func_mode=False):
        super().__init__(arg,bool_value=bool_value,func_mode=func_mode)
    
    @staticmethod
    def set(a,b):
        func_str="LangVar.set"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return LangList(arg,func_mode=True)
        elif(isinstance(a,Noun) and isinstance(b,LangList)):
            a_str=str(a)
            LangVar._VAR_LIST[a_str]=b.copy()
            return LangVar(arg)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def get(a):
        func_str="LangVar.get"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]

        if(LangObj._isFuncModeOfArgs(arg)):
            return LangList(arg,func_mode=True)
        elif(isinstance(a,Noun)):
            a_str=str(a)
            if(a_str not in LangVar._VAR_LIST):
                print(SFGPLError.VAR_NAME_ERROR_UNDEFINED(arg))
            else:
                var_val=LangVar._VAR_LIST[a_str]
                return LangList(arg,bool_value=var_val.getBool(),lang_list=var_val.getLangList())
        else:
            LangObj.printTypeError(arg)

#Class for LangList in SFGPL
class LangList(_BaseList):

    @staticmethod
    def _getSelfClass():
        return {"self":LangList,"self_name":"LangList","base":Noun}
    
    def __init__(self,arg=None,lang_list=[],bool_value=None,func_mode=False):
        super().__init__(arg=arg,lang_list=lang_list,bool_value=bool_value,func_mode=func_mode,func_str="LangList")

    def LangListLen(self):
        return self._ListLen()

    def getLangList(self):
        return self._ListGet()

    @staticmethod
    def get(a,b):
        func_str="LangList.get"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]

        if(LangObj._isFuncModeOfArgs(arg)):
            return LangObj(arg,func_mode=True)
        elif(isinstance(a,LangList) and isinstance(b,BoolList)):
            tmp_obj=a.getLangList()[b.getNaturalNumber()]
            r_obj=None
            if(isinstance(tmp_obj,LangList)):
                r_obj=LangList(arg,bool_value=tmp_obj.getBool(),lang_list=tmp_obj.getLangList())
            elif(isinstance(tmp_obj,BoolList)):
                r_obj=BoolList(arg,bool_value=tmp_obj.getBool(),lang_list=tmp_obj.getBoolList())
            elif(isinstance(tmp_obj,NumberList)):
                r_obj=NumberList(arg,bool_value=tmp_obj.getBool(),lang_list=tmp_obj.getNumberList(),number=tmp_obj.getNumber())
            else:
                r_obj=type(tmp_obj)(arg,bool_value=tmp_obj.getBool())
            
            return r_obj
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def append(a,b):
        func_str="LangList.append"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return LangList(arg,func_mode=True)
        elif(isinstance(a,LangList) and isinstance(b,LangObj)):
            lang_list=a.getLangList()+[b]
            return LangList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def slice(a,b,c):
        func_str="LangList.slice"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return LangList(arg,func_mode=True)
        elif(isinstance(a,LangList) and isinstance(b,BoolList) and isinstance(c,BoolList)):
            lang_list=a.getLangList()[b.getNaturalNumber():c.getNaturalNumber()+1]
            return LangList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def add(a,b):
        func_str="LangList.add"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return LangList(arg,func_mode=True)
        elif(isinstance(a,LangList) and isinstance(b,LangList)):
            lang_list=a.getLangList()+b.getLangList()
            return LangList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def len(a):
        func_str="LangList.len"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,LangList)):
            tmp_bl=BoolList.dec2BoolList(a._ListLen())
            return BoolList(arg=arg,lang_list=tmp_bl.getBoolList())
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def While(a,b,c):
        func_str="LangList.While"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return LangList(arg,func_mode=True)
        elif(isinstance(a,LangList) and isinstance(b,Noun) and isinstance(c,Noun)):
            x=a.copy()
            condition=LangFunc.runFunc(b,x)
            i=0
            while(condition.getLangList()[0].getBool()):
                if(False):
                    print(i)
                x=LangFunc.runFunc(c,x)
                condition=LangFunc.runFunc(b,x)
                i+=1
            return x.copy(arg=arg)
        else:
            LangObj.printTypeError(arg)

#Class for Number in SFGPL
class Number(LangObj):

    @staticmethod
    def _getSelfClass():
        return {"self":Number,"self_name":"Number","base":Number}
    
    def __init__(self,arg,num:int,bool_value=None,func_mode=False):
        super().__init__(arg,bool_value=bool_value,func_mode=func_mode)
        self.__num=num

    def copy(self,arg=None,num=None,bool_value=None,func_mode=None):
        if(arg==None):
            arg=self.words
        if(num==None):
            num=self.__num
        if(bool_value==None):
            bool_value=self._bool_value
        if(func_mode==None):
            func_mode=self._func_mode

        return (type(self))(arg=arg,num=num,bool_value=bool_value,func_mode=func_mode)

    def getNumber(self):
        return self.__num
    
    @staticmethod
    def _getNumberObjList():
        return [
            Number.zero(),
            Number.one(),
            Number.two(),
            Number.three(),
            Number.four(),
            Number.five(),
            Number.six(),
            Number.seven(),
            Number.eight(),
            Number.nine()
        ]
    
    @staticmethod
    def zero():
        func_str="Number.zero"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,0)

    @staticmethod
    def one():
        func_str="Number.one"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,1)

    @staticmethod
    def two():
        func_str="Number.two"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,2)

    @staticmethod
    def three():
        func_str="Number.three"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,3)

    @staticmethod
    def four():
        func_str="Number.four"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,4)

    @staticmethod
    def five():
        func_str="Number.five"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,5)

    @staticmethod
    def six():
        func_str="Number.six"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,6)

    @staticmethod
    def seven():
        func_str="Number.seven"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,7)

    @staticmethod
    def eight():
        func_str="Number.eight"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,8)

    @staticmethod
    def nine():
        func_str="Number.nine"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key]
        return Number(arg,9)


#Class for NumberList in SFGPL
class NumberList(_BaseList):

    @staticmethod
    def _getSelfClass():
        return {"self":NumberList,"self_name":"NumberList","base":Noun}
    
    def __init__(self,arg=None,lang_list=[],number=None,bool_value=None,func_mode=False):
        super().__init__(arg=arg,lang_list=lang_list,bool_value=bool_value,func_mode=func_mode,func_str="NumberList")
        
        self._number=number
        self._list_flag=(self._lang_list!=[] or self._number==None)
        if(self._number==None):
            self._number=NumberList._calcNumberObjList(self._lang_list)

    def copy(self,arg=None,lang_list=None,number=None,bool_value=None,func_mode=None):
        if(arg==None):
            arg=copy.deepcopy(self.words)
        if(lang_list==None):
            lang_list=copy.deepcopy(self._lang_list)
        if(number==None):
            number=self._number
        if(bool_value==None):
            bool_value=self._bool_value
        if(func_mode==None):
            func_mode=self._func_mode

        return (type(self))(arg=arg,lang_list=lang_list,number=number,bool_value=bool_value,func_mode=func_mode)
        
    def NumberListLen(self):
        return self._ListLen()

    def getNumberList(self):
        return self._ListGet()
    
    def getNumber(self):
        return self._number
    
    @staticmethod
    def _calcNumberObjList(nol:list):
        l_len=len(nol)
        sum=0
        for i,li in enumerate(nol):
            if(isinstance(li,Number)):
                sum+=li.getNumber()*(10**(l_len-i-1))
            else:
                return None
        return sum

    @staticmethod
    def _intNumber2NumberObjList(i_num:int):
        number_obj_list=Number._getNumberObjList()
        return [number_obj_list[int(n)] for n in str(i_num)]
        
    @staticmethod
    def get(a,b):
        func_str="NumberList.get"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]

        if(LangObj._isFuncModeOfArgs(arg)):
            return LangObj(arg,func_mode=True)
        elif(isinstance(a,NumberList) and isinstance(b,BoolList)):
            if(a._list_flag):
                tmp_obj=a.getNumberList()[b.getNaturalNumber()]
                r_obj=None
                if(isinstance(tmp_obj,Number)):
                    r_obj=NumberList(arg,bool_value=tmp_obj.getBool(),lang_list=[tmp_obj])
                else:
                    r_obj=type(tmp_obj)(arg,bool_value=tmp_obj.getBool())
                
                return r_obj
            else:
                print(SFGPLError.NUMBERLIST_CONTROL_LIST_ERROR(arg))
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def append(a,b):
        func_str="NumberList.append"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList) and isinstance(b,LangObj)):
            if(a._list_flag):
                lang_list=a.getNumberList()+[b]
                return NumberList(arg=arg,lang_list=lang_list)
            else:
                print(SFGPLError.NUMBERLIST_CONTROL_LIST_ERROR(arg))
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def slice(a,b,c):
        func_str="NumberList.slice"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList) and isinstance(b,BoolList) and isinstance(c,BoolList)):
            if(a._list_flag):
                lang_list=a.getNumberList()[b.getNaturalNumber():c.getNaturalNumber()+1]
                return NumberList(arg=arg,lang_list=lang_list)
            else:
                print(SFGPLError.NUMBERLIST_CONTROL_LIST_ERROR(arg))
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def add(a,b):
        func_str="NumberList.add"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList) and isinstance(b,NumberList)):
            if(a._list_flag):
                lang_list=a.getNumberList()+b.getNumberList()
                return NumberList(arg=arg,lang_list=lang_list)
            else:
                print(SFGPLError.NUMBERLIST_CONTROL_LIST_ERROR(arg))
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def len(a):
        func_str="NumberList.len"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,NumberList)):
            tmp_bl=BoolList.dec2BoolList(a._ListLen())
            return BoolList(arg=arg,lang_list=tmp_bl.getBoolList())
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def digit1(a):
        func_str="NumberList.digit1"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,Number)):
            lang_list=[a]
            return NumberList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def digit2(a,b):
        func_str="NumberList.digit2"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,Number) and isinstance(b,Number)):
            lang_list=[a,b]
            return NumberList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def digit3(a,b,c):
        func_str="NumberList.digit3"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,Number) and isinstance(b,Number) and isinstance(c,Number)):
            lang_list=[a,b,c]
            return NumberList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def digit4(a,b,c,d):
        func_str="NumberList.digit4"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c,d]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,Number) and isinstance(b,Number) and isinstance(c,Number) and isinstance(d,Number)):
            lang_list=[a,b,c,d]
            return NumberList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def digit5(a,b,c,d,e):
        func_str="NumberList.digit5"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b,c,d,e]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,Number) and isinstance(b,Number) and isinstance(c,Number) and isinstance(d,Number) and isinstance(e,Number)):
            lang_list=[a,b,c,d,e]
            return NumberList(arg=arg,lang_list=lang_list)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def calcAdd(a,b):
        func_str="NumberList.calcAdd"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList) and isinstance(b,NumberList)):
            number=a.getNumber()+b.getNumber()
            return NumberList(arg=arg,number=number)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def calcSub(a,b):
        func_str="NumberList.calcSub"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList) and isinstance(b,NumberList)):
            number=a.getNumber()-b.getNumber()
            return NumberList(arg=arg,number=number)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def calcMul(a,b):
        func_str="NumberList.calcMul"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList) and isinstance(b,NumberList)):
            number=a.getNumber()*b.getNumber()
            return NumberList(arg=arg,number=number)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def calcDiv(a,b):
        func_str="NumberList.calcDiv"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a,b]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList) and isinstance(b,NumberList)):
            number=a.getNumber()/b.getNumber()
            return NumberList(arg=arg,number=number)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def IntNL2BL(a):
        func_str="NumberList.IntNL2BL"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return BoolList(arg,func_mode=True)
        elif(isinstance(a,NumberList)):
            number=a.getNumber()
            if(myLib.isInt(number)):
                lang_list=BoolList._int2BLList(int(number))
                return BoolList(arg=arg,lang_list=lang_list)
            else:
                print(SFGPLError.NUMBERLIST_IntNL2BL_FLOAT_ERROR(arg))
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def isPN(a):
        func_str="NumberList.isPN"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return Bool(arg,func_mode=True)
        elif(isinstance(a,NumberList)):
            number=a.getNumber()
            return Bool(arg=arg,bool_value=number>=0)
        
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def minus(a):
        func_str="NumberList.minus"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList)):
            number=a.getNumber()*-1
            return NumberList(arg=arg,number=number)
        else:
            LangObj.printTypeError(arg)

    @staticmethod
    def abs(a):
        func_str="NumberList.abs"
        key=LangObj._getKeyOfDict(func_str)
        arg=[key,a]
        
        if(LangObj._isFuncModeOfArgs(arg)):
            return NumberList(arg,func_mode=True)
        elif(isinstance(a,NumberList)):
            number=abs(a.getNumber())
            return NumberList(arg=arg,number=number)
        else:
            LangObj.printTypeError(arg)


class appendixGrammar():
    @staticmethod
    def Superlative(a:Noun,v:Verb,b:Modifier,c:Noun):
        return Noun.haveP(a,v,Modifier.add(Modifier.Very(b),Modifier.N2M(DeterminerN.In(c))))
    
    @staticmethod
    def EquivalentClass(a:Noun,v:Verb,b:Modifier,c:Noun):
        return Noun.haveP(Noun.AND(a,c),v,Modifier.add(b,WordM.near()))

class myLib():
    @staticmethod
    def isInt(n):
        ni=int(n)
        if(isinstance(n,int)):
            return True
        elif(ni==n):
            return True
        else:
            return False


#A class with a collection of functions to support generation, display, etc.
class SFGPLLib():

    #Preset config for FuncStr
    FUNC_STR_CONFIG_A={"func":"word","before_cmd":"","end_cmd":"","begin":"(","end":")","split":"\n","word_begin":"","word_end":"","zero_args_begin_and_end_flag":False}
    FUNC_STR_CONFIG_MAKE_DICT={"func":"word","before_cmd":"{\"","end_cmd":"\"","begin":":[","end":"]}","split":",","word_begin":"\"","word_end":"\"","zero_args_begin_and_end_flag":True}

    #Preset config for indentString
    INDENT_STRING_CONFIG_DEFAULT={"before_char":"","indent_base":" ","indent_num":2,"need_add_indent":["("],"need_del_indent":[")"]}
    INDENT_STRING_CONFIG_MD_OUT={"before_char":"- ","indent_base":" ","indent_num":2,"need_add_indent":["("],"need_del_indent":[")"]}


    #Convert SFGPL strings to Python objects or commands
    @staticmethod
    def str2CMD(str,toObj=True,result_str_config=stackcmd.StackCMD.result_str_config_defalut):
        cmdstr=stackcmd.StackCMD.stackCMD(cmdlist=LangObj.KEY_LIST,cmdline=str,result_str_config=result_str_config,splitstr=LangObj.SPLIT_STR)
        return  eval(cmdstr) if toObj else cmdstr

    #Output strings according to config
    @staticmethod
    def FuncStr(obj:LangObj,result_str_config={}):
        return SFGPLLib.str2CMD(str(obj),toObj=False,result_str_config=result_str_config)
        
    #Output structured strings in SFGPL syntax in JSON format, and the return type is str when mode=="s", and dict when mode="o"
    @staticmethod
    def structuredDict(obj:LangObj,mode:str="s"):
        s=SFGPLLib.FuncStr(obj,result_str_config=SFGPLLib.FUNC_STR_CONFIG_MAKE_DICT)
        if(mode=="s"):
            return s
        elif(mode=="o"):
            return dict(json.loads(s))

    #Output structured strings in SFGPL syntax in Markdown list format
    @staticmethod
    def structuredStrMDList(obj:LangObj):
        return SFGPLLib.delSpaceLine(SFGPLLib.indentString(SFGPLLib.FuncStr(obj,result_str_config=SFGPLLib.FUNC_STR_CONFIG_A),config=SFGPLLib.INDENT_STRING_CONFIG_MD_OUT).replace("(","").replace(")",""))
        
    #Save structured strings in SFGPL syntax in Markdown list format
    @staticmethod
    def SaveMDListFile(output_path:str,obj:LangObj):
        outstr=SFGPLLib.structuredStrMDList(obj)
        with open(output_path,mode='w',encoding="utf-8") as f:
            f.write(outstr)
        
    #Function to delete lines with only blank spaces
    @staticmethod
    def delSpaceLine(in_str):
        return str(re.sub("(\n\s*\n)","\n",in_str)).strip()

    #Function for indenting a string
    @staticmethod
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
    @staticmethod
    def eqSFGPL(obj1:LangObj,obj2:LangObj):
        return str(obj1)==str(obj2)

    #Functions for validating SFGPL objects
    @staticmethod
    def checkObjOfSFGPL(obj:LangObj):
        converted_obj=SFGPLLib.str2CMD(str(obj))
        return (obj,converted_obj)

    #Convert Python objects to SFGPL strings of multi-lines
    @staticmethod
    def toMultiLineString(*objs,opt_str=""):
        rstr=""
        for obj in objs:
            if(isinstance(obj,Noun)):
                rstr+=str(obj)+LangObj.END_STR+opt_str
            else:
                return None
        return rstr
    
    #Convert SFGPL strings of multi-lines to Python objects or commands
    @staticmethod
    def multiLineStr2CMD(instr,toObj=True,result_str_config=stackcmd.StackCMD.result_str_config_defalut):
        instr=instr.strip()
        split_str_list=instr.split(LangObj.END_STR)
        robj=[]
        
        for s in split_str_list:
            s=s.strip()
            if(s!=""):
                robj.append(SFGPLLib.str2CMD(s,toObj=toObj,result_str_config=result_str_config))
        return robj

    #The function that checks for grammatical errors (i.e., whether the right part of speech is placed in the right place).
    @staticmethod
    def checkType(arg):
        if(isinstance(arg,str)):
            try:
                return True,SFGPLLib.str2CMD(arg)
            except Exception as e:
                return False,e
        elif(isinstance(arg,LangObj)):
            return True,arg
        else:
            return None,None

    class LangListLib:

        #Convert Python List to LangList Object
        @staticmethod
        def pyList2LangList(l:list,func=BoolList.NaturalNum):
            s_bl=[func(BoolList.dec2BoolList(li)) for li in l]
            so=LangList()
            for s_bli in s_bl:
                so=LangList.append(so,s_bli)
            return so

        #Convert LangList Object to Python List
        @staticmethod
        def LangList2PyList(ll:LangList):
            tmp_ll=[]
            for x in ll.getLangList():
                if(isinstance(x,BoolList)):
                    tmp_ll.append(x.getData())
                else:
                    return None
            return tmp_ll

        #Convert Python String to LangList Object
        @staticmethod
        def str2LangList(s:str):
            return SFGPLLib.LangListLib.pyList2LangList([ord(si) for si in s],func=BoolList.ASCII)

        #Convert LangList Object to Python String
        @staticmethod
        def LangList2str(ll:LangList):
            return "".join(SFGPLLib.LangListLib.LangList2PyList(ll))


#Class for SFGPL Corpus
class SFGPLCorpus():

    DEFAULT_ENSURE_ASCII=False
    
    def __init__(self,sfgpl_obj_list:list=[],translation_str_list:list=[]):
        self.__sfgpl_obj_list=[]
        self.__translation_str_list=[]
        if(isinstance(sfgpl_obj_list,list) and isinstance(translation_str_list,list)):
            if(len(sfgpl_obj_list)==len(translation_str_list)):
                self.__sfgpl_obj_list=sfgpl_obj_list
                self.__translation_str_list=translation_str_list

    def __str__(self):
        return self.toStringSFGPL()
    
    def __len__(self):
        return len(self.__sfgpl_obj_list)
    
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

    #Copy SFGPL corpus object
    def copy(self):
        sol=copy.deepcopy(self.__sfgpl_obj_list)
        tsl=copy.deepcopy(self.__translation_str_list)
        return SFGPLCorpus(sfgpl_obj_list=sol,translation_str_list=tsl)

    #Clear SFGPL corpus information
    def clearCorpus(self):
        self.__sfgpl_obj_list=[]
        self.__translation_str_list=[]

    #Get all data
    def getAll(self,mode="ostv"):
        rlist={}

        #version
        if("v" in mode):
            rlist["version"]=SFGPL_VERSION

        #object mode
        if("o" in mode):
            rlist["sfgpl_obj_list"]=self.__sfgpl_obj_list

        #structured dictionary mode
        if("d" in mode):
            rlist["sfgpl_structured_dict_list"]=self.getStructuredDict()
        
        #string mode
        if("s" in mode):
            rlist["sfgpl_str_list"]=list(map(str,self.__sfgpl_obj_list))
        
        #translation mode
        if("t" in mode):
            rlist["translation_str_list"]=self.__translation_str_list
        
        return rlist 
    
    #Get data of index
    def getIndex(self,index):
        if(index<0):
            self.__len__()+index
        return {"sfgpl_obj":self.__sfgpl_obj_list[index],"translation_str":self.__translation_str_list[index]}

    #Get Parallel translation (SFGPL String / Translation String)
    def getParaTranslationString(self,index):
        return (str(self.__sfgpl_obj_list[index]),self.__translation_str_list[index])
    
    #Get a structured dictionary of SFGPL statements
    def getStructuredDict(self):
        dict_func=lambda x:SFGPLLib.structuredDict(x,mode="o")
        return list(map(dict_func,self.__sfgpl_obj_list))

    #Append a sentence
    def append(self,sfgpl_obj:LangObj,translation_str:str):
        self.__sfgpl_obj_list.append(sfgpl_obj)
        self.__translation_str_list.append(translation_str)

    #Insert a sentence
    def insert(self,index:int,sfgpl_obj:LangObj,translation_str:str):
        self.__sfgpl_obj_list.insert(index,sfgpl_obj)
        self.__translation_str_list.insert(index,translation_str)

    #Extend a sentence
    def extend(self,obj):
        d=self.__sub_add(obj)
        self.__sfgpl_obj_list=d["sfgpl_obj_list"]
        self.__translation_str_list=d["translation_str_list"]

    #Convert SFGPL object list to SFGPL string
    def toStringSFGPL(self,opt_str=""):
        return SFGPLLib.toMultiLineString(*self.__sfgpl_obj_list,opt_str=opt_str)

    #Convert translation string  list to string
    def toStringTranslation(self,opt_str=""):
        return opt_str.join(self.__translation_str_list)
    
    #Save json file of SFGPL
    def saveJson(self,path:str,indent:int=4):
        with open(path,mode="w",encoding="utf-8") as f:
            json.dump(self.getAll(mode="stv"),f,indent=indent,ensure_ascii=SFGPLCorpus.DEFAULT_ENSURE_ASCII)

    #Read json file of SFGPL
    @staticmethod
    def readJson(path:str):
        with open(path,mode="r",encoding="utf-8") as f:
            json_data=json.load(f)
            obj_str=list(map(SFGPLLib.str2CMD,json_data["sfgpl_str_list"]))
            trans_str=json_data["translation_str_list"]

            return SFGPLCorpus(sfgpl_obj_list=obj_str,translation_str_list=trans_str)
        
    #Save JSON file of structured SFGPL statements for confirmation.
    def saveStructureJSON(self,path:str,indent:int=4):
        with open(path,mode="w",encoding="utf-8") as f:
            json.dump(self.getStructuredDict(),f,indent=indent,ensure_ascii=SFGPLCorpus.DEFAULT_ENSURE_ASCII)
    
    #Save csv file of SFGPL
    def saveCSV(self,path:str,split_str=",",newline_str="\n"):
        with open(path,mode="w",encoding="utf-8") as f:
            for i in range(self.__len__()):
                tmp_str="\""+str(self.__sfgpl_obj_list[i])+"\""+split_str+"\""+self.__translation_str_list[i]+"\""+newline_str
                f.write(tmp_str)

    #Save text file of SFGPL
    def saveTextFileOfSFGPL(self,path:str,opt_str:str=""):
        with open(path,mode="w",encoding="utf-8") as f:
            f.write(self.toStringSFGPL(opt_str=opt_str))

    #add a sentence of Corpus 
    def setCorpus(self,sfgpl_obj:LangObj,translation_str:str,print_flag:bool=False,md_out_path:str=None):
        self.append(sfgpl_obj=sfgpl_obj,translation_str=translation_str)
        if(print_flag):
            print(sfgpl_obj)
        if(md_out_path!=None):
            SFGPLLib.SaveMDListFile(md_out_path,sfgpl_obj)
            
    #The function to count the number of words in a corpus
    def corpusWordCount(self,SPLIT_WORD=" ",BEFORE_REPLACE_WORD=[";"],include_word_func=lambda x: x!=""):
        sc_str=self.toStringSFGPL()
        for brw_i in BEFORE_REPLACE_WORD:
            sc_str=sc_str.replace(brw_i,SPLIT_WORD)
        sc_str=sc_str.split(SPLIT_WORD)
        sc_str=[li for li in sc_str if include_word_func(li)]
        return collections.Counter(sc_str)
    
    @staticmethod
    def __pyCodeSpaceReplace(tmp_str:str):
        pre_space_chars=[]
        post_space_chars=["(","{","[",","]
        pre_and_post_space_chars=[")","}","]"]

        pre_space_chars_r=[" "+c for c in pre_space_chars]
        post_space_chars_r=[c+" " for c in post_space_chars]
        pre_and_post_space_chars_r=[" "+c+" " for c in pre_and_post_space_chars]

        before_replace_chars=pre_space_chars+post_space_chars+pre_and_post_space_chars
        after_replace_chars=pre_space_chars_r+post_space_chars_r+pre_and_post_space_chars_r

        for i in range(len(before_replace_chars)):
            tmp_str=tmp_str.replace(before_replace_chars[i],after_replace_chars[i])
        return tmp_str

    #Converts the information in the corpus to a string in a Markdown table
    def corpus2MDtableStr(self,header:list=[("s","sfgpl_str_list","SFGPL"),("o","sfgpl_obj_list","Python"),("t","translation_str_list","Translation")],SPLIT_STR="|",TABLE_HEAD_STR=":-:",NEW_LINE_STR="\n",py_code_space_flag=False,py_code_md_code_flag=True):
        mode=""
        for key in header:
            mode+=key[0]
        
        corpus_gets=self.getAll(mode=mode)
        r_str=""

        #header
        r_str+=SPLIT_STR
        for key in header:
            r_str+=key[2]+SPLIT_STR
        r_str+=NEW_LINE_STR

        r_str+=SPLIT_STR
        for key in header:
            r_str+=TABLE_HEAD_STR+SPLIT_STR
        r_str+=NEW_LINE_STR

        #contents
        for i in range(len(self)):
            r_str+=SPLIT_STR
            for key in header:
                tmp_str=str(corpus_gets[key[1]][i])
                if(key[1]=="sfgpl_obj_list"):
                    tmp_str=SFGPLLib.str2CMD(tmp_str,toObj=False)
                    if(py_code_space_flag):
                        tmp_str=SFGPLCorpus.__pyCodeSpaceReplace(tmp_str)
                    if(py_code_md_code_flag):
                        tmp_str=f"```{tmp_str}```"
                
                r_str+=tmp_str+SPLIT_STR
            r_str+=NEW_LINE_STR
        return r_str

