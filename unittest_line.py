import unittest
from c_line import C_Line

class Test_Line(unittest.TestCase):
  
  def test_length(self):
    c_line = C_Line(0,0,0,0)
    self.assertEqual(c_line.getLength(), 0)

    c_line = C_Line(0,0,10,0)
    self.assertEqual(c_line.getLength(), 10)
    
    c_line = C_Line(0,0,10,10)
    self.assertEqual(round(c_line.getLength(),2), 14.14)

    c_line = C_Line(10,0,10,0)
    self.assertEqual(c_line.getLength(), 0)

    c_line = C_Line(0,10,10,0)
    self.assertEqual(round(c_line.getLength(),2), 14.14)

    c_line = C_Line(10,0,10,10)
    self.assertEqual(round(c_line.getLength(),2), 10)

if __name__ == '__main__':
  unittest.main()