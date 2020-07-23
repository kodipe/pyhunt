import unittest
from rodent import Tokenizer, Rodent, Indexer

class TestTokenizer(unittest.TestCase):
  def test_tokenize(self):
    tokenizer = Tokenizer()
    result = tokenizer.tokenize("This is Foo bar")
    self.assertListEqual(result, ["this", "is", "foo", "bar"])

class TestRodent(unittest.TestCase):
  def test_tokenize(self):
    rodent = Rodent('foo_bar_directory')
    self.assertEqual(rodent.dir, 'foo_bar_directory')
    self.assertIsInstance(rodent.tokenizer, Tokenizer)
    self.assertIsInstance(rodent.indexer, Indexer)

if __name__ == "__main__":
  unittest.main()