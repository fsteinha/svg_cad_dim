import unittest
from unittest_line import Test_Line
from unittest_getter_setter import Test_Getter_Setter
from unittest_i_svg import Test_I_SVG
from unittest_svg_interpreter import Test_SVG_Interpreter

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

  suite.addTest(Test_I_SVG('test_init'))
  
  suite.addTest(Test_SVG_Interpreter('test_init'))
  suite.addTest(Test_SVG_Interpreter('test_interpreter'))
  
  return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())