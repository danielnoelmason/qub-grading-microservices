import unittest
import classifygrade

class TestClassifyGrade(unittest.TestCase):
   def test_classifygrade1(self):
       self.assertEqual(classifygrade.classifygrade(39),'Low Fail')
   def test_classifygrade2(self):
       self.assertEqual(classifygrade.classifygrade(40),'Marginal Fail')
   def test_classifygrade3(self):
       self.assertEqual(classifygrade.classifygrade(50),'Fail')
   def test_classifygrade4(self):
       self.assertEqual(classifygrade.classifygrade(60),'Pass')
   def test_classifygrade5(self):
       self.assertEqual(classifygrade.classifygrade(70),'Commendation')
   def test_classifygrade6(self):
       self.assertEqual(classifygrade.classifygrade(80),'Distinction')
   def test_classifygrade6(self):
       self.assertEqual(classifygrade.classifygrade(-1),'Invalid Grade')
   def test_classifygrade7(self):
       self.assertEqual(classifygrade.classifygrade(101),'Invalid Grade')
if __name__ == '__main__':
    unittest.main()
