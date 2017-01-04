# -*- coding: utf-8 -*-
# @Author: Ritesh Pradhan
# @Date:   2016-08-22 16:07:09
# @Last Modified by:   Ritesh Pradhan
# @Last Modified time: 2016-08-25 00:37:49

import math

import libmongo
from nlp_processing import nlp_cleaning
import libchemspipy
# from libchemspipy import get_common_name

db = libmongo.get_db()

def sanitize(name, delim="_"):
  return name.replace("/", delim).replace(".", delim).replace("->", delim)

def diff(a, b):
  b = set(b)
  return [aa for aa in a if aa not in b]


def generate_bag_k(keywords):
  """
  @input: list of keyword
  @return: phrase_bag, wrod_bag
  """
  phrase_bag = list()
  word_bag = list()

  for each_keyword in keywords:
    sanitized_keyword = sanitize(each_keyword.replace("_", " "))  #replace "_" with spaces for phrase and sanitize
    phrases = sanitized_keyword.split("_")
    words = sanitized_keyword.replace("_", " ").split(" ")      #replace "_" with space and split for words
    phrase_bag.extend(phrases)
    word_bag.extend(words)

  phrase_bag_k = list(set(map(nlp_cleaning, phrase_bag)))
  word_bag_k = list(set(map(nlp_cleaning, word_bag)))

  # "molecular formula expansion to common name"
  # common_names = map(libchemspipy.get_common_name, word_bag_k)
  # for i, common_name in enumerate(common_names):
  #   if common_name is not None:
  #     db.molecular_to_commonname.update({"molecular_formula":word_bag_k[i]}, {"molecular_formula":word_bag_k[i], "common_name": common_name}, upsert=True)
  #     word_bag_k.extend(common_name.split())

  return phrase_bag_k, word_bag_k

def generate_bag_v(variables):
  """
  @input: dict of var: description
  """
  var_name_bag = list()
  var_descrip_bag = list()

  for var_name, var_descrip in variables.iteritems():
    sanitized_varname = sanitize(var_name).split("_")
    var_name_bag.append(list(set(map(nlp_cleaning, sanitized_varname))))
    var_descrip_bag.append(nlp_cleaning(var_descrip))

  "molecular formula expansion to common name"
  # common_names = map(libchemspipy.get_common_name, var_name_bag)
  # for i, common_name in enumerate(common_names):
  #   if common_name is not None:
  #     db.molecular_to_commonname.update({"molecular_formula":var_name_bag[i]}, {"molecular_formula":var_name_bag[i], "common_name": common_name}, upsert=True)
  #     var_name_bag.extend(common_name.split())

  return var_name_bag, var_descrip_bag

def subfinder(sublist, parent_list):
  sublist = sublist if type(sublist) == list else sublist.split()
  parent_list = extract_phrases(parent_list) if type(parent_list) == list else parent_list.split()
  for elem in sublist:
    if elem not in parent_list:
      return False
  return True

def sublist_count(sublist, parent_list):
  if subfinder(sublist, parent_list):
    count = list()
    for str in sublist:
      count.append(parent_list.count(str))
    return max(count)
  else:
    return 0


def extract_phrases(parent_list):
  results = list()
  for phrase in parent_list:
    results.extend(word for word in phrase.split())
  return results

def cal_idf_dict(phrase_bag_k, word_bag_k, varname_bag_v, descrip_v):
  idf_phrase_varname = dict()
  idf_phrase_vardescrip = dict()
  idf_word_varname = dict()
  idf_word_vardescrip = dict()

  var_num = len(varname_bag_v)

  for phrase in phrase_bag_k:
    ct = 1.0
    for varname_items in varname_bag_v:
      if subfinder(phrase, varname_items):
        ct += 1.0
        break
    if ct > 1:
      idf_phrase_varname[phrase] = abs(math.log10(var_num/ct))
    else:
      idf_phrase_varname[phrase] = ct

    ct = 1.0
    for vardescrip_items in descrip_v:
      if subfinder(phrase, vardescrip_items):
        ct += 1.0
    if ct > 1:
      idf_phrase_vardescrip[phrase] = abs(math.log10(var_num/ct))
    else:
      idf_phrase_vardescrip[phrase] = ct


  for word in word_bag_k:
    ct = 1.0
    for varname_items in varname_bag_v:
      if subfinder(word, varname_items):
        ct += 1.0
        break
    if ct > 1:
      idf_word_varname[word] = abs(math.log10(var_num/ct))
    else:
      idf_word_varname[word] = ct

    ct = 1.0
    for vardescrip_items in descrip_v:
      if subfinder(word, vardescrip_items):
        ct += 1.0
    if ct > 1:
      idf_word_vardescrip[word] = abs(math.log10(var_num/ct))
    else:
      idf_word_vardescrip[word] = ct


  return idf_phrase_varname, idf_phrase_vardescrip, idf_word_varname, idf_word_vardescrip


def generate_score_matrix(keywords, variables, phrase_bag_k, word_bag_k, var_bag_v, descrip_v, idf_phrase_varname, idf_phrase_vardescrip, idf_word_varname, idf_word_vardescrip):
  """
  @return matrix of size n_keys * n_vars
  """
  print "Generating score matrix ...... "
  n_keys = len(keywords)
  n_vars = len(variables)

  score_matrix = list()
  # print keywords, n_keys
  # print variables, n_vars, len(variables.keys())

  for i, keyword in enumerate(keywords):
    this_key_all_vars_score = list()

    """ keyword level, phrase, varname """
    keyword = keyword.replace("_", " ").replace("/", " ")
    keylevels = keyword.split("->")
    keylevels = list(map(nlp_cleaning, keylevels)) #maintain hierarchy but process with nlp

    score_phrase_varname = list()
    for var_l in var_bag_v:
      pvn_score = 0.0
      for vidx, var in enumerate(var_l):
        for kidx, keylevel in enumerate(keylevels):
          keylevel_list = keylevel.split(' ')
          tf = sublist_count(keylevel_list, var)

          # tf = var.count(keylevel)
          idf = idf_phrase_varname.get(keylevel, 0.0)
          pvn_score += tf*idf*(vidx+1)*(kidx+1)/(len(keylevels)*len(var_l))
      score_phrase_varname.append(pvn_score)


    """ keyword level, phrase, var descrip """
    score_phrase_vardescrip = list()
    for var in descrip_v:
      pvd_score = 0.0
      for kidx, keylevel in enumerate(keylevels):
        keylevel_list = keylevel.split(' ')
        tf = sublist_count(keylevel_list, var)
        # tf = var.count(keylevel)
        idf = idf_phrase_vardescrip.get(keylevel, 0.0)
        pvd_score += tf*idf*(kidx+1)/len(keylevels)
      score_phrase_vardescrip.append(pvd_score)


    """ keyword words, word bag, varname """
    keyword_words = list()
    for keylevel in keylevels:
      keyword_words.extend(keylevel.split())
    keyword_words = list(set(keyword_words))

    score_word_varname = list()       #score based on variable name and science keyword words
    for var_l in var_bag_v:
      wvn_score = 0.0
      for vidx, var in enumerate(var_l):
        for kidx, kword in enumerate(keyword_words):
          # var = var.split(' ')
          keyword_list = keyword.split(' ')
          tf = sublist_count(keyword_list, var)
          # tf = var.count(kword)
          idf = idf_word_varname.get(kword, 0.0)
          wvn_score += tf*idf*(vidx+1)/len(var_l)
      score_word_varname.append(wvn_score)

    """ keyword words, word bag, var descrip """
    score_word_vardescrip = list()        #score based on variable name and science keyword words
    for var in descrip_v:
      wvd_score = 0.0
      for kidx, kword in enumerate(keyword_words):
        # var = var.split(' ')
        keyword_list = keyword.split(' ')
        tf = sublist_count(keyword_list, var)
        # tf = var.count(kword)
        idf = idf_word_vardescrip.get(kword, 0.0)
        wvn_score += tf*idf
      score_word_vardescrip.append(wvd_score)

    #now need to combine scores from the 4 categories by assigning weights(significance)
    #set wt1 = 0.5, (subjectively), meaning score from field metadata is half-credited of from variable name
    #set wt2 = 0.1, (subjectively), meaning score from phrase (exact match) gives 10 times credit as much as from words
    wt1 = 0.5
    wt2 = 0.1

    for vidx in xrange(n_vars):
      f_score = score_phrase_varname[vidx] + wt1 * score_phrase_vardescrip[vidx] + \
        wt2*score_word_varname[vidx] + wt1 * wt2* score_word_vardescrip[vidx]
      this_key_all_vars_score.append(f_score)

    # print i, this_key_all_vars_score
    score_matrix.append(this_key_all_vars_score)
  return score_matrix



def kv_generator(keywords, variables, score_matrix):
  variable_names = variables.keys()
  kv = dict()
  for i, keyword in enumerate(keywords):
    kvd = dict()
    mapped = dict()
    ranked = dict()
    for j, v_score in enumerate(score_matrix[i]):
      if v_score > 0.3:
        mapped[variable_names[j].replace(".", "_")] = "%.5f" %(v_score)
      # else:
      #   ranked[variable_names[j].replace(".", "_")] = 0.0
    kvd["mapped"] = mapped
    kvd["ranked"] = ranked
    if (len(kvd['mapped'].keys()) > 0 or len(kvd['ranked'].keys()) > 0):
      kv[keyword.replace(".", "_").title().replace("->", " > ").replace("_", " ")] = kvd
  return kv

def vk_generator(variables, keywords, score_matrix):
  variable_names = variables.keys()
  vk = dict()
  for i, variable in enumerate(variable_names):
    vkd = dict()
    mapped = dict()
    ranked = dict()

    for j in xrange(len(keywords)):
      if score_matrix[j][i] > 0.3:
        mapped[keywords[j].replace(".", "_").title().replace("->", " > ").replace("_", " ")] = "%.5f" %(score_matrix[j][i])
      # else:
      #   ranked[keywords[j].replace(".", "_").title().replace("->", " > ").replace("_", " ")] = 0.0

    vkd["mapped"] = mapped
    vkd["ranked"] = ranked
    if (len(vkd['mapped'].keys()) > 0 or len(vkd['ranked'].keys()) > 0):
      vk[variable.replace(".", "_")] = vkd
  return vk


def doc_generator(keywords, variables, score_matrix):
  kv = kv_generator(keywords, variables, score_matrix)
  # print "--- Printing kv generated ---"
  # print kv

  vk = vk_generator(variables, keywords, score_matrix)
  # print "--- Printing vk generated ---"
  # print vk

  return kv, vk



def populate_tf_idf(to_map_colls):
  for coll in to_map_colls:
    print "Updating %s Collection" %(coll)
    ## for matching only specific datasets.
    ks_find = db.ks.find_one({"unique_name": coll}, {"keyword_list":1, "dataset_id": 1, "_id": 0}) or {}
    vs_find = db.vs.find_one({"unique_name": coll}, {"variable_list":1, "meta_filename": 1, "dataset_id": 1, "ways": 1, "cfk": 1, "cfu": 1, "all_vars": 1, "_id": 0})
    if vs_find is None:
      print "No %s in vs..." %(coll)
    else:
      ## for matching across all datasets.
      keywords = db.ks.find({}, {"keyword_list":1, "dataset_id": 1, "_id": 0})
      keywords = [keyword for keyword_list in keywords for keyword in keyword_list['keyword_list']]
      variables = vs_find["variable_list"]
      # keywords = # ks_find["keyword_list"]
      dataset_id = ks_find.get('dataset_id', vs_find["meta_filename"])
      ways = dict(vs_find["ways"])
      cfk = dict(vs_find["cfk"])
      cfu = dict(vs_find["cfu"])
      all_vars = list(vs_find["all_vars"])

      # if len(variables) <= 0:
      #   print "\tVariables set empty. Mapping cannot be done."
      #   continue
      # if len(keywords) <= 0:
      #   print "\tKeywords set empty. Mapping cannot be done."
      #   continue
      phrase_bag_k, word_bag_k = generate_bag_k(keywords)
      var_bag_v, descrip_v = generate_bag_v(variables)

      # print phrase_bag_k, word_bag_k
      # print var_bag_v, descrip_v
      # print len(phrase_bag_k), len(word_bag_k), len(var_bag_v), len(descrip_v)

      idf_phrase_varname, idf_phrase_vardescrip, idf_word_varname, idf_word_vardescrip = cal_idf_dict(phrase_bag_k, word_bag_k, var_bag_v, descrip_v)

      # print '+++++++++++++++++++++++++++++++++'
      # print idf_phrase_varname, idf_phrase_vardescrip, idf_word_varname, idf_word_vardescrip

      score_matrix = generate_score_matrix(keywords, variables, \
        phrase_bag_k, word_bag_k, var_bag_v, descrip_v, \
        idf_phrase_varname, idf_phrase_vardescrip, idf_word_varname, idf_word_vardescrip)

      # print score_matrix

      kv, vk = doc_generator(keywords, variables, score_matrix)
      # print "this is kv ", kv
      doc = {
          "unique_name": coll, "kv": kv, "vk": vk, "dataset_id": dataset_id, \
          "ways": ways, "cfk": cfk, "cfu": cfu, \
          "all_vars": all_vars, "all_keys": [k.replace("_", " ") for k in kv.keys()]
        }
      # print doco
      # break
      result = db.ms.insert_one(doc)
      if result:
        print "Successfully Inserted '%s' collection maps" %(coll)



def main():
  ## Doing this because we want to match all vs we have.
  #
  colls_in_ks = [] #[k["unique_name"] for k in db.ks.find({}, {"unique_name":1, "_id": 0})]
  colls_in_vs = [v["unique_name"] for v in db.vs.find({}, {"unique_name":1, "_id": 0})]
  colls_in_ms = [m["unique_name"] for m in db.ms.find({}, {"unique_name":1, "_id": 0})]

  super_colls = colls_in_ks if len(set(colls_in_ks)) >= len(set(colls_in_vs)) else colls_in_vs
  to_map_colls = diff(super_colls, colls_in_ms)
  # print len(colls_in_ks)
  # print len(to_map_colls)
  # print len(super_colls), len(to_map_colls)
  # to_map_colls = ["ADVANCED MICROWAVE SOUNDING UNIT-A (AMSU-A) SWATH FROM NOAA-15 V1"]
  # to_map_colls = ["MOPITT Gridded Monthly CO Retrievals (Thermal Infrared Radiances) V006"]
  # to_map_colls = ['AMSR-E_Aqua Daily L3 Global Snow Water Equivalent EASE-Grids V002']
  populate_tf_idf(to_map_colls)

  # print "This: ", "GHRSST Level 2P European Medspiration TMI SST:1" in colls_in_ks
  # print "This: ", "GHRSST Level 2P European Medspiration TMI SST:1" in colls_in_vs
  # print "This: ", "GHRSST Level 2P European Medspiration TMI SST:1" in to_map_colls

  db.ms.create_index([("unique_name", 1)])
  print "Job Completed.\n"

if __name__ == '__main__':
  main()
