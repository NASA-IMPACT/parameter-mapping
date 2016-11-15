# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:29:41 2016
    performing nlp processing
@author: xli
"""

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from create_wordbank import convert_CamelCase2WhiteSpace
from create_wordbank import load_acronym

def nlp_StopStemLemm(phrase):
    
    english_stops = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    
    tok_str = word_tokenize(phrase)
    stop_str = [word for word in tok_str if word not in english_stops]
    
    return_phrase = ''
    for word in stop_str:
        return_phrase = return_phrase + ' ' + stemmer.stem(lemmatizer.lemmatize(word))
            
    return_phrase = return_phrase.lstrip()
    return_phrase = return_phrase.rstrip()
#    return_phrase = convert_CamelCase2WhiteSpace(return_phrase)  #no meaning, all lowercase at this moment
    
    return return_phrase

def nlp_phrasecleaning(phrasestr, dic):
    phrasestr = phrasestr.replace('/', ' ')
    phrasestr = phrasestr.replace('_', ' ')
    phrasestr = phrasestr.replace('\\', ' ')
    phrasestr = phrasestr.replace('\n', ' ')
    phrasestr = phrasestr.lstrip()
    phrasestr = phrasestr.rstrip()
    
    word_list = phrasestr.split()
    #need to camelcase processing here
    tempstr = ''
    for k in range(len(word_list)):
        cstr = convert_CamelCase2WhiteSpace(word_list[k])
        cstrary = cstr.split()
        for m in range(len(cstrary)):
            tempstr = tempstr + ' ' + cstrary[m]
    
    word_list = tempstr.lstrip()
    word_list = word_list.rstrip()
    
    word_list = word_list.split()
    
    result_str = ''
    
    for i in range(len(word_list)):
        cstr = word_list[i]
        result_str = result_str + ' ' + cstr.lower()
        if dic.has_key(cstr.lower()):
            result_str = result_str + ' ' + dic.get(cstr.lower())
    
    result_str.lstrip()
    result_str.rstrip()
    
    return result_str
 
#dic = load_acronym('acronym_list.txt')
#cstr = 'this is_test sst_temperature Microwave\n'   
#res = nlp_phrasecleaning(cstr, dic)
#print res
    
#phr = nlp_processing('sea-air humidity difference')
#print phr