import unittest
from unittest_line import Test_Line
from unittest_getter_setter import Test_Getter_Setter
from unittest_i_svg import I_SVG

def suite():
  '''test suite'''
  suite = unittest.TestSuite()
  
  suite.addTest(Test_Line('test_length'))
  suite.addTest(Test_Line('test_get'))
  suite.addTest(Test_Line('test_set'))
  
  suite.addTest(Test_Getter_Setter('test_init'))
  suite.addTest(Test_Getter_Setter('test_update_set'))
  suite.addTest(Test_Getter_Setter('test_update_get'))
  suite.addTest(Test_Getter_Setter('test_isuptodate'))

  return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())