import unittest
from pyhunt.pyhunt import Tokenizer, PyHunt, Indexer
from pyhunt.languages import English

class TestTokenizer(unittest.TestCase):
  def test_tokenize(self):
    tokenizer = Tokenizer()
    result = tokenizer.tokenize("Collaborative online platform")
    self.assertListEqual(result, ["collaborative", "online", "platform"])

  def test_tokenize_with_stop_words(self):
    tokenizer = Tokenizer()
    result = tokenizer.tokenize("This is Foo bar")
    self.assertListEqual(result, ["foo", "bar"])

  def test_remove_stop_words(self):
    tokenizer = Tokenizer()
    result = tokenizer.remove_stop_words(["test", "in", "the", "file"], English.STOP_WORDS)
    self.assertListEqual(result, ["test", "file"])

  def test_tokenize_with_lines_break(self):
    tokenizer = Tokenizer()
    result = tokenizer.tokenize(
      """Solutions to net security fears

Fake"""
    )
    self.assertListEqual(result, ["solutions", "net", "security", "fears", "fake"])

class TestRodent(unittest.TestCase):
  def test_tokenize(self):
    pyhunt = PyHunt("foo_bar_directory", "foo_index_dir")
    self.assertEqual(pyhunt.dir, "foo_bar_directory")
    self.assertEqual(pyhunt.index_dir, "foo_index_dir")
    self.assertIsInstance(pyhunt.tokenizer, Tokenizer)
    self.assertIsInstance(pyhunt.indexer, Indexer)

if __name__ == "__main__":
  unittest.main()