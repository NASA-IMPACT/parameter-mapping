# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:44:05 2015

@author: xli
"""

from create_wordbank import *

def getKeywordList(keywordfile, dic):
    f = open(keywordfile, "r")
    
    result = []
    full_list = []
    for line in f:
        full_list.append(line)
        strlist = line.split('->')
    
        num = len(strlist)
        
        wordlist = ''
        for i in range(num):
            strlist[i] = strlist[i].replace('/', ' ')
            strlist[i] = strlist[i].replace('\n', '')
            strlist[i] = strlist[i].lstrip()
            strlist[i] = strlist[i].rstrip()
            newstring = strlist[i].split()
            for j in range(len(newstring)):
                wordlist = wordlist + ' ' + newstring[j]
        #create word bank
        wordset = create_wordbank(wordlist.lower(), dic)
        result.append(list(wordset))
    f.close()
    
    return result, full_list

def getVariableList(variablefile, dic):
    f = open(variablefile, "r")
    
    full_variable = []
    result = []
    for line in f:
        full_variable.append(line)
        strlist = line.split('|')
        
        num = len(strlist)
        
        wordlist = ''
        for i in range(num):
            strlist[i] = strlist[i].replace('_', ' ')
            strlist[i] = strlist[i].replace('\\', ' ')
            strlist[i] = strlist[i].replace('/', ' ')
            strlist[i] = strlist[i].replace('\n', '')
            strlist[i] = strlist[i].lstrip()
            strlist[i] = strlist[i].rstrip()
            strlist[i] = convert_CamelCase2WhiteSpace(strlist[i])
            varlist = strlist[i].split()
            for j in range(len(varlist)):
                wordlist = wordlist + ' ' + varlist[j]
       
        print wordlist.lower()
        wordset = create_wordbank(wordlist.lower(), dic)
        print wordset
        
        result.append(list(wordset))
        
    f.close()
    
    return result, full_variable

def map_str_list(strlist_var, strlist_key):
    '''
    strlist_var contains a list of strings describing variable
    strlist_key contains a list of strings describing compound keywords
    '''
    var_len = len(strlist_var)
    # mapping each variable str to keyword string accumunate match
    score = 0
    for i in range(var_len):
        cstr = strlist_var[i]
        score += is_string_in_strlist(cstr, strlist_key)
    
    return score

def is_string_in_strlist(strvar, strlist):
    '''
    strvar is one string in variable description
    strlist_key contains a list of strings describing compound keywords
    '''
    
    for i in range(len(strlist)):
        if (strvar == strlist[i]):
            return 1
            
    return 0
   
    
def mapping_variable_2_keyword(variableList, keywordList):
    #variable list is the one returned list from getVariableList
    #keyword lsit is the one returned list from getKeywordList
    numVar = len(variableList)
    numKey = len(keywordList)
    
    #mapping start from the lowest keyword list 
    result = []
    
    for varId in range(numVar):
        varlist = variableList[varId]
    
        lst = []
        #match to each keyword list
        for keyId in range(numKey):
            c_score = map_str_list(varlist, keywordList[keyId])
               
            #better match of the variable to this keyword
            if (c_score > 0):
                clist = [varId, keyId, c_score]
                lst.append(clist)
                
        result.append(lst)
    
    return result


def mapping(filename):           
    dic = load_acronym('acronym_list.txt')   
    
    print dic
    
    keyword_name = filename + '_keyword_original.txt'
    #a, a1 = getKeywordList('MODISAqua Aerosol Cloud Water Vapor Ozone Daily L3 Global 1Deg CMG V005_keyword_original.txt', dic)
    a, a1 = getKeywordList(keyword_name, dic)
    
    print a

    var_name = filename + '_variable.txt'
    
    b, b1 = getVariableList(var_name, dic)
    
    #print b

    c = mapping_variable_2_keyword(b, a)
    
    #output mapping based on collection keywords
    allmatchlist = []
    for i in range(len(a)):
        #get all variables that are mapped to this keyword
        matchlist = []
        for j in range(len(c)):
            clist = c[j]
            if (len(clist) > 0):
                for k in range(len(clist)):
                    if( clist[k][1] == i):
                        cvarlist = [clist[k][0], clist[k][2]]
                        matchlist.append(cvarlist)
        
        allmatchlist.append(matchlist)
    
    
    outname = filename + '_keyword_variable_mapping.txt'
    fo = open(outname, "wb")
    
    dent = '  '
    for i in range(len(a)):
        match = allmatchlist[i]
        match.sort(key=lambda tup: tup[1], reverse=True)
        
        printstr = a1[i]
        
        fo.write(printstr)
        #print rest of line for matched variables
        for j in range(len(match)):
            matchj = match[j]
            printstr = dent + ' score:' + str(matchj[1]) + ' variablename:' + b1[matchj[0]] 
            fo.write(printstr)
    fo.close()
    
    outname = filename + '_variable_keyword_mapping.txt'
    fo = open(outname, "wb")
    
    dent = '  '
    #for each variable
    for i in range(len(c)):
        match = c[i]
        fo.write(b1[i])
        #print b1[i]
        if (len(match) > 0):
            for j in range(len(match)):
                clist = match[j]
                printstr = dent + ' score:' + str(clist[2]) + ' keyword:' + a1[clist[1]]
                #print printstr
                fo.write(printstr)
                
    fo.close()
    

mapping('2A12.20060110.46465.7')
mapping('MERRA300.prod.assim.tavg1_2d_slv_Nx.20141104')


