# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:31:33 2016
    this program loads GCMD science keywords
@author: xli
"""

import csv
#from nltk.stem import PorterStemmer
#from nltk.stem import WordNetLemmatizer
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
from nlp_processing import nlp_StopStemLemm
from nlp_processing import nlp_phrasecleaning
from create_wordbank import load_acronym
#from create_wordbank import convert_CamelCase2WhiteSpace
import math

def load_all_GCMD_Keywords(filename):
    keywords = []
    fullkeyword = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            rec = []
            for i in range(7):
                if len(row[i]) > 0:
                    rec.append(row[i])
                else:
                    break
            keywords.append(rec)

            ckey = row[1]
            for i in range(2, 7):
                if len(row[i]) > 0:
                    ckey = ckey + '->' + row[i]
                else:
                    break
            fullkeyword.append(ckey)

    del keywords[0]
    del keywords[0]
    del fullkeyword[0]
    del fullkeyword[0]

    return keywords, fullkeyword

def parse_GCMD_Keywords(keywordfile):
    dic = load_acronym('acronym_list.txt')

    #assuming keywords for a data set from a file such as xxx_keyword_original.txt
    with open(keywordfile, 'rb') as f:
        keylist = f.read().splitlines()

    keylist = list(set(keylist))

    org_keywordlist = []

    #get a set of keywords for this dataset
    fullkeywordlist = []
    partialkeywordlist = []
    for i in range(len(keylist)):
        ckeylist = keylist[i]
        ckeylist = ckeylist.rstrip()
        ckeylist = ckeylist.lstrip()
        org_keywordlist.append(ckeylist)

        strlist = ckeylist.split('->')
        for j in range(len(strlist)):
            slist = strlist[j].split('/')
            for k in range(len(slist)):
                fullkeywordlist.append(slist[k])
                plist = slist[k].split()
                for m in range(len(plist)):
                    partialkeywordlist.append(plist[m])

    #nlp processing (removing stop word, stem and lemmatize)
    fullkeywordlist = list(set(fullkeywordlist))
    partialkeywordlist = list(set(partialkeywordlist))

    fullwordlist = []
    for i in range(len(fullkeywordlist)):
        cstr = nlp_phrasecleaning(fullkeywordlist[i], dic)
        fullwordlist.append(nlp_StopStemLemm(cstr))

    partialwordlist = []
    for i in range(len(partialkeywordlist)):
        cstr = nlp_phrasecleaning(partialkeywordlist[i], dic)
        partialwordlist.append(nlp_StopStemLemm(cstr))

	#cleaning original keywordlist for duplicate
	org_keywordlist = list(set(org_keywordlist))

    print "FF: ", fullwordlist
    print "JJ: ", partialwordlist
    print "KK: ", org_keywordlist

    return list(set(fullwordlist)), list(set(partialwordlist)), org_keywordlist

def parse_GCMD_Keywords_by_list(keylist):
    dic = load_acronym('acronym_list.txt')

    org_keywordlist = []

    #get a set of keywords for this dataset
    fullkeywordlist = []
    partialkeywordlist = []
    for i in range(len(keylist)):
        ckeylist = keylist[i]
        org_keywordlist.append(ckeylist)

        strlist = ckeylist.split('->')
        for j in range(len(strlist)):
            slist = strlist[j].split('/')
            for k in range(len(slist)):
                fullkeywordlist.append(slist[k])
                plist = slist[k].split()
                for m in range(len(plist)):
                    partialkeywordlist.append(plist[m])

    #nlp processing (removing stop word, stem and lemmatize)
    fullkeywordlist = list(set(fullkeywordlist))
    partialkeywordlist = list(set(partialkeywordlist))

    fullwordlist = []
    for i in range(len(fullkeywordlist)):
        cstr = nlp_phrasecleaning(fullkeywordlist[i], dic)
        fullwordlist.append(nlp_StopStemLemm(cstr))

    partialwordlist = []
    for i in range(len(partialkeywordlist)):
        cstr = nlp_phrasecleaning(partialkeywordlist[i], dic)
        partialwordlist.append(nlp_StopStemLemm(cstr))

    return list(set(fullwordlist)), list(set(partialwordlist)), org_keywordlist

def parse_variable_metadata(varfile):
    dic = load_acronym('acronym_list.txt')
    with open(varfile, 'rb') as f:
        varcontent = f.read().splitlines()

    varnamelist = []
    varfieldlist = []
    orgvarlist = []

    for i in range(len(varcontent)):
        #print varcontent[i]
        orgvarlist.append(varcontent[i])
        cstr = varcontent[i].split('|||')
        #process varname info
        namestr = cstr[0].split('/')
        cname = []
        for j in range(len(namestr)):
            #cstr = convert_CamelCase2WhiteSpace(namestr[j])
            namestr[j] = nlp_phrasecleaning(namestr[j], dic)
            cname.append(nlp_StopStemLemm(namestr[j]))
        varnamelist.append(cname)

        #process description info
        cstr[1] = nlp_phrasecleaning(cstr[1], dic)
        varfieldlist.append(nlp_StopStemLemm(cstr[1]))

    return varnamelist, varfieldlist, orgvarlist

def extend_keywords(keywordlist, allkeywordslist):
    res = []

    for i in range(len(keywordlist)):
        ckey = keywordlist[i]
#        print ckey
        for j in range(len(allkeywordslist)):
            if ckey in allkeywordslist[j] and (ckey != allkeywordslist[j]):
                res.append(allkeywordslist[j])
#                print '    ' + allkeywordslist[j]

    return res

#keylist1: collection keywords of phrases, keylist2: colleciton keywords of words
def cal_idf_dic(keylist1, keylist2, varnamelist, varfieldlist):

    num_var = len(varnamelist)

    idf_var_k1 = {}
    for i in range(len(keylist1)):
        ckey = keylist1[i]
        ct = 0.0
        for j in range(len(varnamelist)):
            clist = varnamelist[j]
            flag = 0
            for k in range(len(clist)):
                if ckey in clist[k]:
                    flag = 1
                    break
            if flag == 1:
                ct = ct + 1.0
        if ct > 0.0:
            idf_var_k1.update({ckey : math.log10(num_var/ct)})
        else:
            idf_var_k1.update({ckey : ct})

    idf_field_k1 = {}
    for i in range(len(keylist1)):
        ckey = keylist1[i]
        ct = 0.0
        for j in range(len(varfieldlist)):
            if ckey in varfieldlist[j]:
                ct = ct + 1.0

        if ct > 0.0:
            print ckey
            idf_field_k1.update({ckey : math.log10(num_var/ct)})
        else:
            idf_field_k1.update({ckey : ct})

    idf_var_k2 = {}
    for i in range(len(keylist2)):
        ckey = keylist2[i]
        ct = 0.0
        for j in range(len(varnamelist)):
            clist = varnamelist[j]
            flag = 0
            for k in range(len(clist)):
                if ckey in clist[k]:
                    flag = 1
                    break
            if flag == 1:
                ct = ct + 1.0
        if ct > 0.0:
            idf_var_k2.update({ckey : math.log10(num_var/ct)})
        else:
            idf_var_k2.update({ckey : ct})

    idf_field_k2 = {}
    for i in range(len(keylist2)):
        ckey = keylist2[i]
        ct = 0.0
        for j in range(len(varfieldlist)):
            if ckey in varfieldlist[j]:
                ct = ct + 1.0

        if ct > 0.0:
            idf_field_k2.update({ckey : math.log10(num_var/ct)})
        else:
            idf_field_k2.update({ckey : ct})

    return idf_var_k1, idf_field_k1, idf_var_k2, idf_field_k2

def cal_idf(keylist1, keylist2, varnamelist, varfieldlist):

    num_var = len(varnamelist)

    idf_varlist_k1 = []
    for i in range(len(keylist1)):
        ckey = keylist1[i]
        ct = 0.0
        for j in range(len(varnamelist)):
            if ckey in varnamelist[j]:
                ct = ct + 1.0
        if ct > 0.0:
            idf_varlist_k1.append(math.log10(num_var/ct))
        else:
            idf_varlist_k1.append(ct)

#    for i in range(len(keylist1)):
#        print keylist1[i], idf_varlist_k1[i]
#
#    print ' '
    idf_fieldlist_k1 = []
    for i in range(len(keylist1)):
        ckey = keylist1[i]
        ct = 0.0
        for j in range(len(varfieldlist)):
            if ckey in varfieldlist[j]:
                ct = ct + 1.0

        if ct > 0.0:
            idf_fieldlist_k1.append(math.log10(num_var/ct))
        else:
            idf_fieldlist_k1.append(ct)

#    for i in range(len(keylist1)):
#        print keylist1[i], idf_fieldlist_k1[i]
#
##   for keylist 2 (break-down individual words instead of phrases)
#    print '**************'
    idf_varlist_k2 = []
    for i in range(len(keylist2)):
        ckey = keylist2[i]
        ct = 0.0
        for j in range(len(varnamelist)):
            if ckey in varnamelist[j]:
                ct = ct + 1.0
        if ct > 0.0:
            idf_varlist_k2.append(math.log10(num_var/ct))
        else:
            idf_varlist_k2.append(ct)

#    for i in range(len(keylist2)):
#        print keylist2[i], idf_varlist_k2[i]
#
#    print ' '
    idf_fieldlist_k2 = []
    for i in range(len(keylist2)):
        ckey = keylist2[i]
        ct = 0.0
        for j in range(len(varfieldlist)):
            if ckey in varfieldlist[j]:
                ct = ct + 1.0

        if ct > 0.0:
            idf_fieldlist_k2.append(math.log10(num_var/ct))
        else:
            idf_fieldlist_k2.append(ct)

    return idf_varlist_k1, idf_fieldlist_k1, idf_varlist_k2, idf_fieldlist_k2

#keylist1: collection keyword containing 'phrase' (or compound word')
#keylist2: collection keywords composed of words (phrase decomposed)
#keywordlist: original collection keywords (fullpath)
#var_meta: variable name list drawn from file
#field_meta: variable field text drawn from file
#idf_varlist_k1, idf_fieldlist_k1: idf calculated for keylist1 based on
#   variable name and variable field, respectively
#idf_varlist_k2, idf_fieldlist_k2: idf calculated for keylist2 based on
#   variable name and variable field, respectively
def map_var_2_keyword(keywordlist, varfield, keylist1, keylist2, var_meta, field_meta, \
    idf_varlist_k1, idf_fieldlist_k1, idf_varlist_k2, idf_fieldlist_k2):

    dic = load_acronym('acronym_list.txt')

    num_var = len(var_meta)

    num_keywords = len(keywordlist)
    ovreall_score = []

    #process each keywords
    for i in range(num_keywords):   #each original science keywords
        #print keywordlist[i]
        cscorelist = []         #score of each variable matched to this keyword
        ckey = keywordlist[i]   #current keyword
        keylist = ckey.split('->')  #split current keyword, on various levels of hierarchy
        #print keylist

        kwd = []    #keep hierarchy of keywords (as indexed in list), processed by nlp
                    #as does earlier for variable text for consistency

        for j in range(len(keylist)):
            cstr = nlp_phrasecleaning(keylist[j], dic)
            cstr = nlp_StopStemLemm(cstr)
            kwd.append(cstr)
        #print kwd
        nkwd = float(len(kwd))

        #now score each variable based on text matching using tf-idf scheme
        var_k1_score = []       #score based on variable name and science keyword k1
        for k in range(num_var):    #scoring for each variable
            cvar = var_meta[k]      #variable text for
            #print cvar
            nlev = float(len(cvar)) #number of levels of this variable, the lowest set weight of 1.0
            cscore = 0.0            #score
            for m in range(len(cvar)):  #for each level of variable (possible from nc4, hdf5)
                cstr = cvar[m]      #current level of variable name component
                for n in range(len(kwd)):   #try to match to each keyword with hierarchy
                    tf = cstr.count(kwd[n])    #count number of current keyword in the varname
                    idf = idf_varlist_k1.get(kwd[n], 0.0) #get idf for kwd[n] word, default 0.0
                    cscore = cscore + tf*idf*(m+1)*(n+1)/(nkwd*nlev)  #tf-idf is weighted by the hierarchy level of keyword and variable
            var_k1_score.append(cscore)

        #print var_k1_score

        #now score each variable field based on text matching using tf-idf scheme
        field_k1_score = []       #score based on variable name and science keyword k1
        for k in range(num_var):    #scoring for each variable field, same number as variable name
            fvar = field_meta[k]      #field text for
            #print fvar

            cscore = 0.0            #score
            for n in range(len(kwd)):   #try to match to each keyword with hierarchy
                tf = fvar.count(kwd[n])    #count number of current keyword in the varname
                idf = idf_fieldlist_k1.get(kwd[n], 0.0) #get idf for kwd[n] word, default 0.0
                cscore = cscore + tf*idf*(n+1)/nkwd  #tf-idf is weighted by the hierarchy level of keyword and variable
            field_k1_score.append(cscore)

        #print field_k1_score

        #now score each variable based on text matching using tf-idf scheme using keyword 2 list
        #need to regenerate current keyword list by decomposing keyword phrase into words

        elem_kwd = []       #element words (not phrase)
        for kk in range(len(kwd)):
            cstr = kwd[kk]
            carray = cstr.split()
            for mm in range(len(carray)):
                elem_kwd.append(carray[mm])

        elem_kwd = list(set(elem_kwd))


        var_k2_score = []       #score based on variable name and science keyword k1
        for k in range(num_var):    #scoring for each variable
            cvar = var_meta[k]      #variable text for

            nlev = float(len(cvar)) #number of levels of this variable, the lowest set weight of 1.0
            cscore = 0.0            #score
            for m in range(len(cvar)):  #for each level of variable (possible from nc4, hdf5)
                cstr = cvar[m]      #current level of variable name component
                for n in range(len(elem_kwd)):   #try to match to each keyword with hierarchy
                    tf = cstr.count(elem_kwd[n])    #count number of current keyword in the varname
                    idf = idf_varlist_k2.get(elem_kwd[n], 0.0) #get idf for kwd[n] word, default 0.0
                    cscore = cscore + tf*idf*(m+1)/nlev  #tf-idf is weighted by the hierarchy level of variable
            var_k2_score.append(cscore)

        #print var_k2_score

        field_k2_score = []       #score based on variable name and science keyword k1
        for k in range(num_var):    #scoring for each variable field, same number as variable name
            fvar = field_meta[k]      #field text for
            #print fvar

            cscore = 0.0            #score
            for n in range(len(elem_kwd)):   #try to match to each keyword with hierarchy
                tf = fvar.count(elem_kwd[n])    #count number of current keyword in the varname
                idf = idf_fieldlist_k2.get(elem_kwd[n], 0.0) #get idf for kwd[n] word, default 0.0
                cscore = cscore + tf*idf  #tf-idf
            field_k2_score.append(cscore)


        #now need to combine scores from the 4 categories by assigning weights(significance)
        #set wt1 = 0.5, (subjectively), meaning score from field metadata is half-credited of from variable name
        #set wt2 = 0.1, (subjectively), meaning score from phrase (exact match) gives 10 times credit as much as from words
        wt1 = 0.5
        wt2 = 0.1

        for kk in range(num_var):
            f_score = var_k1_score[kk] + wt1 * field_k1_score[kk] + \
                wt2*var_k2_score[kk] + wt1 * wt2* field_k2_score[kk]
            cscorelist.append(f_score)

        ovreall_score.append(cscorelist)

        #print cscorelist
        rank = sorted(range(len(cscorelist)), key=lambda k: cscorelist[k])
        rank.reverse()

#        for kk in range(num_var):
#            idx = rank[kk]
#            if cscorelist[idx] > 0.0:
#                print '  ' + varfield[idx], cscorelist[idx]
        #print out variables that have score > 0.0

    return ovreall_score

def combine_ranking(keywordlist, extkeywordlist, varfield, score, ext_score):
    var_score = []
    print '****************** final ranking ***************'
    print '****************** variable to keyword mapping ***************'
    for i in range(len(keywordlist)):   #for each original keyword
        ckey = keywordlist[i]
        print ckey
        ct = 1.0  #current keyword
        cscore = score[i]

        #check if extended keyword extend this keyword
        for j in range(len(extkeywordlist)):
            ekey = extkeywordlist[j]
            if ckey in ekey:    #this is one child
                for k in range(len(varfield)):
                    cscore[k] = cscore[k] + ext_score[j][k]
                ct = ct + 1.0

        for k in range(len(varfield)):
            cscore[k] = cscore[k] / ct

        var_score.append(cscore)
        #print out matched variable based on score in descending order
        rank = sorted(range(len(cscore)), key=lambda k: cscore[k])
        rank.reverse()

        for kk in range(len(varfield)):
            idx = rank[kk]
            if cscore[idx] > 0.0:
                print '  ' + varfield[idx], cscore[idx]

    print '****************** keyword to variable mapping ***************'
    keyword_score = []
    for i in range(len(varfield)):
        vscore = []
        print varfield[i]
        for j in range(len(keywordlist)):
            vscore.append(var_score[j][i])
        keyword_score.append(vscore)

        #print out matched variable based on score in descending order
        rank = sorted(range(len(vscore)), key=lambda k: vscore[k])
        rank.reverse()

        for kk in range(len(keywordlist)):
            idx = rank[kk]
            if vscore[idx] > 0.0:
                print '  ' + keywordlist[idx], vscore[idx]

    return var_score, keyword_score

allkeywords, allfullkeywords = load_all_GCMD_Keywords('sciencekeywords.csv')
#keylist1, keylist2, keywordlist = parse_GCMD_Keywords('GSSTF.2c.1987.07.09.he5_keyword_original.txt')
#var_meta, field_meta, varfield = parse_variable_metadata('GSSTF.2c.1987.07.09.he5_variable.txt')
#keylist1, keylist2, keywordlist = parse_GCMD_Keywords('SBUV2-NOAA18_L2-SBUV2N18L2_2005m0605_v01-02-2013m0829t074100.h5_keyword_original.txt')
#var_meta, field_meta, varfield = parse_variable_metadata('SBUV2-NOAA18_L2-SBUV2N18L2_2005m0605_v01-02-2013m0829t074100.h5_variable.txt')
keylist1, keylist2, keywordlist = parse_GCMD_Keywords('2A.GPM.Ku.V6-20160118.20140308-S220950-E234217.000144.V04A.HDF5_keyword_original.txt')
var_meta, field_meta, varfield = parse_variable_metadata('2A.GPM.Ku.V6-20160118.20140308-S220950-E234217.000144.V04A.HDF5_variable.txt')
ext_keywordlist = extend_keywords(keywordlist, allfullkeywords)

extkeylist1, extkeylist2, extkeywordlist = parse_GCMD_Keywords_by_list(ext_keywordlist)

idf_var_k1, idf_field_k1, idf_var_k2, idf_field_k2 = cal_idf_dic(keylist1, keylist2, var_meta, field_meta)
idf_var_k1_ext, idf_field_k1_ext, idf_var_k2_ext, idf_field_k2_ext = cal_idf_dic(extkeylist1, extkeylist2, var_meta, field_meta)

score = map_var_2_keyword(keywordlist, varfield, keylist1, keylist2, var_meta, field_meta, \
   idf_var_k1, idf_field_k1, idf_var_k2, idf_field_k2)

ext_score = map_var_2_keyword(extkeywordlist, varfield, extkeylist1, extkeylist2, var_meta, field_meta, \
   idf_var_k1_ext, idf_field_k1_ext, idf_var_k2_ext, idf_field_k2_ext)

v_score, k_score = combine_ranking(keywordlist, extkeywordlist, varfield, score, ext_score)



