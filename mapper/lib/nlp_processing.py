# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-08-23 11:51:18
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-08-24 01:11:49

"""
    performing nlp processing
	reference: @author: xli
"""

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from create_wordbank import convert_CamelCase2WhiteSpace
from create_wordbank import load_acronym
from acronyms import DISCARDS, ACRONYMS

def discards_and_acronyms(wordlower):
	if wordlower not in DISCARDS:
		acronymlower = ACRONYMS.get(wordlower, '')
		return wordlower + ' ' + acronymlower
	return ''

def nlp_StopStemLemm(phrase):

    english_stops = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()

    tok_str = word_tokenize(phrase)
    stop_str = [word for word in tok_str if word not in english_stops]

    return_phrase = ''
    for word in stop_str:
        return_phrase = return_phrase + ' ' + stemmer.stem(lemmatizer.lemmatize(word))

    return return_phrase.strip()

def nlp_cleaning(phrasestr):
    phrasestr = phrasestr.replace('/', ' ')
    phrasestr = phrasestr.replace('_', ' ')
    phrasestr = phrasestr.replace('\\', ' ')
    phrasestr = phrasestr.replace('\n', ' ')
    phrasestr = phrasestr.strip()

    word_list = phrasestr.split()
    #need to camelcase processing here

    tempstr = ' '.join(item for item in list(set(map(convert_CamelCase2WhiteSpace, word_list))))
    word_list = tempstr.strip().lower().split()

    acronymed_list = list(set(map(discards_and_acronyms, word_list)))
    result_str = ' '.join(item for item in list(set(map(nlp_StopStemLemm, acronymed_list))))

    return result_str.strip()

def main():
	#dic = load_acronym('acronym_list.txt')
	cstr = 'this is_test sst_temperature Microwave time\n'
	res = nlp_cleaning(cstr)
	print res

	#phr = nlp_processing('sea-air humidity difference')
	#print phr
	pass

if __name__ == '__main__':
	main()
