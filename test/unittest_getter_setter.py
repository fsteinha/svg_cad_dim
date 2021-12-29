import unittest
import sys
sys.path.append('../')
from c_getter_setter import C_Getter_Setter

class Test_Getter_Setter(unittest.TestCase):
  ''' unittest for c_getter_setter class'''

  def test_init(self):
    ''' test init'''
    c_cetter_setter = C_Getter_Setter()
    self.assertEqual(c_cetter_setter.set_cnt, 0)
    self.assertEqual(c_cetter_setter.get_cnt, None)
    pass
  
  def test_update_set(self):
    ''' test set cnat update'''
    c_cetter_setter = C_Getter_Setter()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    self.assertEqual(c_cetter_setter.set_cnt, 4)
    
  def test_update_get(self):
    ''' test get cnt update'''
    c_cetter_setter = C_Getter_Setter()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    self.assertEqual(c_cetter_setter.get_cnt, None)
    c_cetter_setter.update_get()
    self.assertEqual(c_cetter_setter.get_cnt, c_cetter_setter.set_cnt)
    c_cetter_setter.update_set()
    self.assertEqual(c_cetter_setter.get_cnt, (c_cetter_setter.set_cnt - 1))
    c_cetter_setter.update_get()
    self.assertEqual(c_cetter_setter.get_cnt, c_cetter_setter.set_cnt)

  def test_isuptodate(self):
    ''' test get cnt update'''
    c_cetter_setter = C_Getter_Setter()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    c_cetter_setter.update_set()
    self.assertEqual(c_cetter_setter.is_uptodate(), False)
    c_cetter_setter.update_get()
    self.assertEqual(c_cetter_setter.is_uptodate(), True)
    c_cetter_setter.update_set()
    self.assertEqual(c_cetter_setter.is_uptodate(), False)
    


if __name__ == '__main__':
  unittest.main()