import json
import requests
import re

class KeywordsExtractor:
  CMR_META_URL = "https://cmr.earthdata.nasa.gov/search/collections?short_name={}"
  def __init__(self, short_names):
    self.short_names = short_names
    self.respone_list = list()

  def fetch_meta_files(self):
    for short_name in self.short_names:
      self.respone_list.append(self.extract_info(short_name))

  def extract_keywords(self, metafile):
    keywords = list()
    for elem in metafile['ScienceKeywords']:
      keywords.append('->'.join(elem.values()))
    return keywords

  def extract_version(self, url):
    return url.split('/')[-1]


  def extract_longname(self, metafile):
    long_name = re.findall('<LongName>([\w\W\s]*?)(?=\n?<\/LongName>)', metafile)
    if(len(long_name) > 0):
      return long_name[0]
    else:
      return re.findall('<Entry_Title>([\w\W\s]*?)(?=\n?<\/Entry_Title>)', metafile)[0]


  def extract_dataset_id(self, metafile):
    dataset_id = re.findall('<DataSetId>([\w\W\s]*?)(?=\n?<\/DataSetId>)', metafile)
    if(len(dataset_id) > 0):
      return dataset_id[0]
    else:
      return re.findall('<Entry_Title>([\w\W\s]*?)(?=\n?<\/Entry_Title>)', metafile)[0]

  def extract_daac(self, metafile):
    dataset_id = re.findall('<ArchiveCenter>([\w\W\s]*?)(?=\n?<\/ArchiveCenter>)', metafile)
    if(len(dataset_id) > 0):
      return dataset_id[0]
    else:
      dataset_id = re.findall('<ProcessingCenter>([\w\W\s]*?)(?=\n?<\/ProcessingCenter>)', metafile)
      if(len(dataset_id) > 0):
        return dataset_id[0]
    return ''

  def extract_info(self, short_name):
    info = {}
    print 'for shortname:', short_name
    response = str(requests.get(self.CMR_META_URL.format(short_name)).text)
    url = str(re.findall('<location>([\w\W\s]*?)(?=\n?<\/location>)', response)[0])
    metafile = requests.get(url + '.umm_json').text
    keyword_list = self.extract_keywords(json.loads(metafile))
    metafile   = requests.get(url + '.native').text

    return {
      'short_name': short_name,
      'version': self.extract_version(url),
      'dataset_id': self.extract_dataset_id(metafile),
      'long_name': self.extract_longname(metafile),
      'keyword_list': keyword_list,
      'daac': self.extract_daac(metafile)
    }
