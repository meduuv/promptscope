import unittest
from promptscope import length,words
class Tests(unittest.TestCase):
 def test_metrics(self): self.assertEqual(length("hello"),5);self.assertEqual(words("hello world"),2)
if __name__=="__main__":unittest.main()
