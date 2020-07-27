import re

class Language:
  def create_stem():
    pass

class English(Language):
  STEMMING_REGEX = r'ed|ion|ing|s|or|ies|ly$'
  STOP_WORDS = [
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
    'many',
    'down'
  ]

  def create_stem(self, token):
    return re.sub(self.STEMMING_REGEX, '', token.lower())

