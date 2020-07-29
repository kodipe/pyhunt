import re

class Language:
  def create_stem(token):
    return token

class English(Language):
  STEMMING_REGEX = r'(ed|ion|ing|s|or|ies|ly|\'s)$'
  STOP_WORDS = [
    'are',
    'is',
    'in',
    'i',
    'a',
    'am',
    'he',
    'she',
    'it',
    'of',
    'at',
    'so',
    'to',
    'the',
    'me',
    'my',
    'for',
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

