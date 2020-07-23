#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import glob
import json
import sys

class Tokenizer:
  """
  Class used for tokenizing purpose
  TODO:
    - special characters support
    - case sensitive or not support
  """

  def __init__(self):
    pass

  def tokenize(self, content):
    return self.remove_stop_words(content.lower().split(), [
      'are',
      'is',
      'i',
      'am',
      'he',
      'she',
      'it',
      'of',
      'at',
      'the',
      'and',
      'want',
      'this',
      'have',
      'self',
      'then',
      'what',
      'much',
      'down'
    ])

  def remove_stop_words(self, tokens, stop_words):
    return list(filter(lambda token: token not in stop_words, tokens))

class Indexer:
  """
    Class used for indexing files
    TODO:
      - index single file and add results 
        to index (e.g. if new file is created)
      - Improve performance for large files
  """
  def __init__(self):
    self.index = {}
    pass

  def create_index(self, files_map, minimal_word_length=1):
    for file, tokens in files_map.items():
      for token in tokens:
        if len(token) > minimal_word_length:
          
          # print(
          #   token, 
          #   tokens.count(token) # O = n^2 -> it has to be improved
          # )

          if token in self.index:
            if file not in self.index[token]:
              self.index[token].append(file)
          else:
            self.index[token] = [file]

  def save_index(self, file_name):
    index_file = io.open(file_name, 'w+', encoding='utf8')
    index_file.write(json.dumps(self.index))
    index_file.close()

  def load_index(self, file_name):
    index_file = io.open(file_name, 'r', encoding='utf8')
    self.index = json.loads(index_file.read())
    index_file.close()

  def add_file_to_index(self):
    # To be implemented
    pass

class Rodent:
  """
  Main class of search engine
  """
  def __init__(self, dir):
    self.tokenizer = Tokenizer()
    self.indexer = Indexer()

    self.dir = dir
    self.files_map = {}

  def create_index(self, minimal_word_length=1):
    self.load_files()
    self.indexer.create_index(self.files_map, minimal_word_length)

  def load_files(self):
    """
      Load files list and its content
    """
    self.files = glob.glob(f'{self.dir}/**/*.txt', recursive=True)

    for file_path in self.files:
      self.read_file(file_path)

  def read_file(self, file_path):
    """
      Open file and map content to given file
    """
    try:
      file = io.open(file_path, 'r', encoding='utf8', errors='ignore')
      file_content = file.read()

      self.files_map[file_path] = self.tokenizer.tokenize(file_content)
    except:
      print("File reading error")

  def search(self, query, output='files'):
    """
      Search words in indexer index
      TODO:
        - try to find better performance
        - ordering files based on how many files contains specific word 
          and how many times word occur in specific file
    """
    query_words = query.lower().split()

    results = {}

    for word in query_words:
      if word in self.indexer.index:
        for file_path in self.indexer.index[word]:
          if file_path in results:
            results[file_path] = results[file_path] + 1
          else:
            results[file_path] = 1

    if output == 'wages':
      return list(sorted(results.items(), key=lambda x: x[1], reverse=True))
    else:
      return list(results.keys())

    

  def save_index(self, file_name):
    self.indexer.save_index(file_name)

  def load_index(self, file_name):
    self.indexer.load_index(file_name)
    
# Usage    

if __name__ == "__main__":
  engine = Rodent('test_files')
  # engine.create_index()

  engine.load_index('index.json')
  # engine.save_index('index.json')

  query = u"exotic spread operator which is great"

  results = engine.search(query, output='wages')

  sys.stdout.buffer.write(f'Results for: "{query}"\n'.encode())
  print(results)