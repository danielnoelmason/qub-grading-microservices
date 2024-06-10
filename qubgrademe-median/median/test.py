import unittest
from medianfunction import getMedianMark

class TestMedian(unittest.TestCase):
   def test_median(self):
       self.assertEqual(getMedianMark(20,22,22,30,40),22)
if __name__ == '__main__':
    unittest.main()
