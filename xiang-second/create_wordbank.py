# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:36:06 2015

@author: xli
"""
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

#this function creates a word bank given a sentence.
def create_wordbank(sentence, dic):
    #first thing to do is to expand acronym, assuming white space separated
    wordlist = sentence.split()
    
    wlist = []
    for i in range(len(wordlist)):
        wlist.append(wordlist[i])
    
    for id in range(len(wordlist)):
        if dic.has_key(wordlist[id].lower()):
            new_value = dic.get(wordlist[id].lower())
            wlist.remove(wordlist[id])
            strlist = new_value.split()
            for i in range(len(strlist)):
                wlist.append(strlist[i])
            
    
    new_sentence = ''
    if (len(wlist) > 0):
        for i in range(len(wlist)):
            new_sentence = new_sentence + wlist[i].lower() + ' '

    wsentence = new_sentence.rstrip()
    
    #tokenize the sentence into words
    tok_str = word_tokenize(wsentence)
    
    english_stops = set(stopwords.words('english'))
    
    #remove stop words
    stop_str = [word for word in tok_str if word not in english_stops]

    #print stop_str
    #expand acronym if exist
    '''
    for id in range(len(stop_str)):
        if dic.has_key(stop_str[id]):
            new_value = dic.get(stop_str[id])
            stop_str.remove(stop_str[id])
            strlist = new_value.split()
            for i in range(len(strlist)):
                stop_str.append(strlist[i])
    '''
    
    #print stop_str

    #define local limmatizer and stemmer
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    res = []
    for word in stop_str:
        if (len(word) > 2):
            res.append(stemmer.stem(lemmatizer.lemmatize(word)))
            
    return set(res)
    
def load_acronym(filename):
    f = open(filename, "r")
    
    dic = {}
    
    for line in f:
        strlist = line.split('->')
        for i in range(len(strlist)):
            strlist[i] = strlist[i].replace('\n', '')
            strlist[i] = strlist[i].lstrip()
            strlist[i] = strlist[i].rstrip()
        dic.update({strlist[0] : strlist[1]})        
    
    f.close()
    
    return dic

def convert_CamelCase2WhiteSpace(string):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).lower()
    
def convert_CamelCase2UnderScore(string):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

'''
dic = load_acronym('acronym_list.txt')   

sentence = 'r_reflct_1064od_1hz_cor|1 Hz 1064nm total column optical depth'

a = create_wordbank(sentence, dic)
print a

sentence = 'ATMOSPHERE->CLOUDS->CLOUD OPTICAL DEPTH/THICKNESS'
a = create_wordbank(sentence, dic)
print a

sentence = 'ATMOSPHERE->AEROSOLS->AEROSOL OPTICAL DEPTH/THICKNESS'
a = create_wordbank(sentence, dic)
print a
'''

string = 'SeaSurfaceTemperature test'
a = convert_CamelCase2WhiteSpace(string)
