import unittest
from rodent.rodent import Tokenizer, Rodent, Indexer
from rodent.languages import English

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
    rodent = Rodent("foo_bar_directory", "foo_index_dir")
    self.assertEqual(rodent.dir, "foo_bar_directory")
    self.assertEqual(rodent.index_dir, "foo_index_dir")
    self.assertIsInstance(rodent.tokenizer, Tokenizer)
    self.assertIsInstance(rodent.indexer, Indexer)

if __name__ == "__main__":
  unittest.main()