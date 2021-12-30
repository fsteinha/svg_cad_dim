'''
Interface for SVG file interpreter

'''
from datetime import date

class I_SVG():
  '''Interface class '''
  
  def __init__(self, s_svg_file, s_author = None, s_description = None, date = None):
      '''Constructor'''
      self.s_svg_file = s_svg_file
      check_type(self.s_svg_file, type("string"), False)

      self.setAutor(s_author)
      self.setDescription(s_description)
      self.setDate(date)
      
      pass
  
  def getSvg_file(self):
    '''getter svg file'''
    return self.s_svg_file
    pass

  def setAutor(self, s_author):
    '''setter autor'''
    self.s_author = s_author
    check_type(self.s_author, type("string"))
    pass

  def getAutor(self):
    '''getter autor'''
    return self.s_author

  def setDescription(self, s_description):
    '''setter description'''
    self.s_description = s_description
    check_type(self.s_description, type("string"))
    pass

  def getDescription(self):
    '''getter description'''
    return self.s_description
    
  def setDate(self, date):
    '''setter date'''
    self.date = date
    check_type(self.date, type(date))
    pass

  def getDate(self):
    '''getter date'''
    return self.date



def check_type (value, s_type, b_None_allowed = True):
  '''helper function '''
  b_raise = False
  
  if ((b_None_allowed == False) and (value == None)) or\
      ((type(value) != s_type) and (value != None)):
    b_raise = True

  if b_raise:
    raise Exception ("Wrong type %s, %s expected" % (type(value), s_type)) 
