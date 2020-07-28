import unittest

from rodent.languages import English

class TestEnglish(unittest.TestCase):
  def test_create_stem(self):
    lang = English()
    result = [
      lang.create_stem("talking"),
      lang.create_stem("talked"),
      lang.create_stem("talks"),
      lang.create_stem("shortly"),
      lang.create_stem("connection")
    ]
    self.assertListEqual(result, [
      "talk",
      "talk",
      "talk",
      "short",
      "connect"
    ])

if __name__ == "__main__":
  unittest.main()