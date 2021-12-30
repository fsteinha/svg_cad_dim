
from typing import Annotated


def check_type (value, s_type, b_None_allowed = True):
  b_raise = False
  
  if (b_None_allowed == False) and (value == None):
    b_raise = True
  elif (type(value) != s_type):
    b_raise = True

  if b_raise:
    raise Exception ("Wrong type %s (%s)" % (f'{value=}'.split('=')[0], type(value))) 
  

class I_SVG():
  def __init__(self, s_svg_file, s_author = None, s_description = None, date = None) -> None:
      self.s_svg_file = s_svg_file
      check_type(self.s_svg_file, 'str', False)
      

      self.setAutor(s_author)
      self.setDescription(s_description)
      self.setDate(date)
      
      pass
  
  def getSvg_file(self):
    return self.s_svg_file
    pass

  def setAutor(self, s_author):
    self.s_author = s_author
    check_type(self.s_author, 'str')
    pass

  def getAutor(self):
    return self.s_author

  def setDescription(self, s_description):
    self.s_description = s_description
    check_type(self.s_description, 'str')
    pass

  def getDescription(self):
    return self.s_description

  def setDate(self, date):
      self.date = date
      check_type(self.date, 'datetime')
      pass

  def getDate(self):
    return self.date
