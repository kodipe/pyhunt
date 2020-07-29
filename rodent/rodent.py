#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import glob
import json
import sys
import re
import os

from rodent.languages import English

RODENT_OUTPUT_WAGES = 'wages'
RODENT_OUTPUT_FILES = 'files'
RODENT_NORMALIZE_REGEX = r'[^A-Za-z0-9 \-]+'

class TokenizerInterface:
  def tokenize():
    pass

class Tokenizer(TokenizerInterface):
  """
  Class used for tokenizing purpose
  TODO:
    - case sensitive or not support
  """

  def __init__(self):
    pass

  def tokenize(self, content):
    return self.remove_stop_words(re.sub(RODENT_NORMALIZE_REGEX, '', content.lower()).split(), English.STOP_WORDS)

  def remove_stop_words(self, tokens, stop_words):
    return list(filter(lambda token: token not in stop_words, tokens))

class Indexer:
  """
    Class used for indexing files
    TODO:
      - Improve performance for large files
  """
  def __init__(self, index_dir):
    self.index = {}
    self.files_index = {}
    self.index_dir = index_dir
    self.lang = English()
    pass

  def create_index(self, files_map, minimal_word_length=1):
    for file, tokens in files_map.items():
      self.add_file_to_index(file, tokens, minimal_word_length)

  def create_files_index(self, files):
    for file in files:
      self.files_index[len(self.files_index.keys()) + 1] = file

  def save_index(self, file_name):
    files_index_file = io.open(os.path.join(self.index_dir, 'files_index.json'), 'w+', encoding='utf8')
    files_index_file.write(json.dumps(self.files_index))
    files_index_file.close()

    index_file = io.open(file_name, 'w+', encoding='utf8')
    index_file.write(json.dumps(self.index))
    index_file.close()

  def load_index(self, file_name):
    files_index_file = io.open(os.path.join(self.index_dir, 'files_index.json'), 'r', encoding='utf8')
    self.files_index = json.loads(files_index_file.read())
    files_index_file.close()

    index_file = io.open(file_name, 'r', encoding='utf8')
    self.index = json.loads(index_file.read())
    index_file.close()

  def add_file_to_index(self, file, tokens, minimal_word_length=1):
    for token in tokens:
      if len(token) > minimal_word_length:
        for file_id, file_name in self.files_index.items():
          if file_name == file:
            if self.lang.create_stem(token) in self.index:
              if file_id not in self.index[self.lang.create_stem(token)]:
                self.index[self.lang.create_stem(token)].append(file_id)
            else:
              self.index[self.lang.create_stem(token)] = [file_id]
            break
    pass

class Rodent:
  """
  Main class of search engine
  """

  def __init__(self, content_dir, index_dir):
    self.files = []
    self.dir = content_dir
    self.index_dir = index_dir
    self.files_map = {}
    
    self.tokenizer = Tokenizer()
    self.indexer = Indexer(index_dir=self.index_dir)
    self.lang = English()

  def create_index(self, persist=False, minimal_word_length=1):
    self.load_files()
    self.indexer.create_files_index(self.files)
    self.indexer.create_index(self.files_map, minimal_word_length)

    if persist:
      self.indexer.save_index(os.path.join(self.index_dir, 'index.json'))

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

  def search(self, query, output=RODENT_OUTPUT_FILES):
    """
      Search words in indexer index
      TODO:
        - try to find better performance
        - ordering files based on how many files contains specific word 
          and how many times word occur in specific file
    """
    query_words = re.sub(RODENT_NORMALIZE_REGEX, '', query.lower()).split()

    results = {}

    for word in query_words:
      if self.lang.create_stem(word) in self.indexer.index:
        for file_path in self.indexer.index[self.lang.create_stem(word)]:
          if file_path in results:
            results[file_path] = results[file_path] + 1
          else:
            results[file_path] = 1

    if output == RODENT_OUTPUT_WAGES:
      return list(sorted(results.items(), key=lambda x: x[1], reverse=True))
    else:
      return list(results.keys())

  def save_index(self, file_name):
    self.indexer.save_index(file_name)

  def load_index(self, file_name):
    self.indexer.load_index(file_name)

  def add_file_to_index(self, index_file, file_path):
    self.indexer.load_index(index_file)
    self.read_file(file_path)
    self.indexer.create_files_index([
      file_path
    ])
    self.indexer.add_file_to_index(file_path, self.files_map[file_path])
    self.indexer.save_index(os.path.join(self.index_dir, 'index.json'))