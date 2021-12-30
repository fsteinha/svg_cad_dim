import unittest
import sys
sys.path.append('../')
from i_svg import I_SVG
from datetime import date

class Test_I_SVG(unittest.TestCase):
  ''' unittest for interface class svg'''

  def test_init(self):
    ''' test init'''
    i_svg  = I_SVG('test.svg')
    self.assertEqual(i_svg.s_svg_file, 'test.svg')
    self.assertEqual(i_svg.s_author, None)
    self.assertEqual(i_svg.s_description, None)
    self.assertEqual(i_svg.date, None)
  
    i_svg  = I_SVG('test.svg', "autor", "description", date(2020,12,23))
    self.assertEqual(i_svg.s_svg_file, 'test.svg')
    self.assertEqual(i_svg.s_author, "autor")
    self.assertEqual(i_svg.s_description, "description")
    self.assertEqual(i_svg.date, date(2020,12,23))

  
    pass

   
  

if __name__ == '__main__':
  unittest.main()