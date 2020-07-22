import glob

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
      - save index to file
  """
  def __init__(self):
    pass

  def index_files(self, files_map):
    self.index = {}

    for file, tokens in files_map.items():
      for token in tokens:
        if token in self.index:
          self.index[token].append(file)
        else:
          self.index[token] = [file]


class Rodent:
  """
  Main class of search engine
  """
  def __init__(self, dir):
    self.tokenizer = Tokenizer()
    self.indexer = Indexer()

    self.dir = dir
    self.files_map = {}

    self.load_files()

    self.indexer.index_files(self.files_map)

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
        - ordering files based on word occurence
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
    
# Usage    

engine = Rodent('test_files')

query = 'with'

results = engine.search(query)

print(f'Results for: "{query}"')
print(results)