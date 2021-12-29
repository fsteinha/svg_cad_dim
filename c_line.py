import math
from c_getter_setter import C_Getter_Setter

class C_Line():
  def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0) -> None:
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2
      self.getset_sat = C_Getter_Setter()
      self.length = None
      pass
  
  def getX1(self):
    return self.x1
    pass

  def getX2(self):
    return self.x2
    pass
  
  def getY1(self):
    return self.y1
    pass

  def getY2(self):
    return self.y2
    pass
  
  def setX1(self, value):
    self.x1 = value
    self.getset_sat.update_set()
    pass
  
  def setX2(self, value):
    self.x2 = value
    self.getset_sat.update_set()
    pass

  def setY1(self, value):
    self.y1 = value
    self.getset_sat.update_set()
    pass

  def setY2(self, value):
    self.y2 = value
    self.getset_sat.update_set()
    pass

  def getLength(self):
    if self.getset_sat.is_uptodate() == False:
      self.length = math.sqrt((abs(self.x2-self.x1) ** 2) + (abs(self.y2-self.y1) ** 2))
    self.getset_sat.update_get()
    return self.length
    pass
