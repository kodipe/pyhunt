import glob
import json

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
    return content.lower().split()

class Indexer:
  """
    Class used for indexing files
    TODO:
      - index single file and add results 
        to index (e.g. if new file is created)
  """
  def __init__(self):
    self.index = {}
    pass

  def create_index(self, files_map):
    for file, tokens in files_map.items():
      for token in tokens:
        if token in self.index:
          if file not in self.index[token]:
            self.index[token].append(file)
        else:
          self.index[token] = [file]

  def save_index(self, file_name):
    index_file = open(file_name, 'w+')
    index_file.write(json.dumps(self.index))
    index_file.close()

  def load_index(self, file_name):
    index_file = open(file_name, 'r')
    self.index = json.loads(index_file.read())
    index_file.close()



class Rodent:
  """
  Main class of search engine
  """
  def __init__(self, dir):
    self.tokenizer = Tokenizer()
    self.indexer = Indexer()

    self.dir = dir
    self.files_map = {}

  def create_index(self):
    self.load_files()
    self.indexer.create_index(self.files_map)

  def load_files(self):
    """
      Load files list and its content
    """
    self.files = glob.glob('test_files/*')

    for file_path in self.files:
      self.read_file(file_path)

  def read_file(self, file_path):
    """
      Open file and map content to given file
    """
    file = open(file_path, 'r')
    file_content = file.read()

    self.files_map[file_path] = self.tokenizer.tokenize(file_content)

  def search(self, query):
    """
      Search words in indexer index
      TODO:
        - try to find better performance
        - ordering files based on how many files contains specific word 
          and how many times word occur in specific file
    """
    query_words = query.split()

    results = {}

    for word in query_words:
      if word in self.indexer.index:
        for file_path in self.indexer.index[word]:
          if file_path in results:
            results[file_path] = results[file_path] + 1
          else:
            results[file_path] = 1
      else:
        print([])

    return list(results.keys())

  def save_index(self, file_name):
    self.indexer.save_index(file_name)

  def load_index(self, file_name):
    self.indexer.load_index(file_name)
    
# Usage    

if __name__ == "__main__":
  engine = Rodent('test_files')
  engine.create_index()

  # engine.load_index('index.json')
  # engine.save_index('index.json')

  query = 'with nulla'

  results = engine.search(query)

  print(f'Results for: "{query}"')
  print(results)