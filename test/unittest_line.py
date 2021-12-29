import unittest
import sys
sys.path.append('../')
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
    pass
  
  def test_get(self):
    c_line = C_Line(0,0,0,0)
    self.assertEqual(c_line.getX1(), 0)
    self.assertEqual(c_line.getY1(), 0)
    self.assertEqual(c_line.getX2(), 0)
    self.assertEqual(c_line.getY2(), 0)

    c_line = C_Line(100,0,0,0)
    self.assertEqual(c_line.getX1(), 100)
    self.assertEqual(c_line.getY1(), 0)
    self.assertEqual(c_line.getX2(), 0)
    self.assertEqual(c_line.getY2(), 0)

    c_line = C_Line(0,100,0,0)
    self.assertEqual(c_line.getX1(), 0)
    self.assertEqual(c_line.getY1(), 100)
    self.assertEqual(c_line.getX2(), 0)
    self.assertEqual(c_line.getY2(), 0)

    c_line = C_Line(0,0,100,0)
    self.assertEqual(c_line.getX1(), 0)
    self.assertEqual(c_line.getY1(), 0)
    self.assertEqual(c_line.getX2(), 100)
    self.assertEqual(c_line.getY2(), 0)

    c_line = C_Line(0,0,0,100)
    self.assertEqual(c_line.getX1(), 0)
    self.assertEqual(c_line.getY1(), 0)
    self.assertEqual(c_line.getX2(), 0)
    self.assertEqual(c_line.getY2(), 100)

  def test_set(self):
    c_line = C_Line(0,0,0,0)
    c_line.setX1(100)
    self.assertEqual(c_line.getX1(), 100)
    self.assertEqual(c_line.getY1(), 0)
    self.assertEqual(c_line.getX2(), 0)
    self.assertEqual(c_line.getY2(), 0)

    c_line = C_Line(0,0,0,0)
    c_line.setY1(100)
    self.assertEqual(c_line.getX1(), 0)
    self.assertEqual(c_line.getY1(), 100)
    self.assertEqual(c_line.getX2(), 0)
    self.assertEqual(c_line.getY2(), 0)

    c_line = C_Line(0,0,0,0)
    c_line.setX2(100)
    self.assertEqual(c_line.getX1(), 0)
    self.assertEqual(c_line.getY1(), 0)
    self.assertEqual(c_line.getX2(), 100)
    self.assertEqual(c_line.getY2(), 0)

    c_line = C_Line(0,0,0,100)
    c_line.setY2(100)
    self.assertEqual(c_line.getX1(), 0)
    self.assertEqual(c_line.getY1(), 0)
    self.assertEqual(c_line.getX2(), 0)
    self.assertEqual(c_line.getY2(), 100)

if __name__ == '__main__':
  unittest.main()