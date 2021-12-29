"""
  Provides a base getter setter class of mangeing the status
"""

class C_Getter_Setter():
  """Base class for inhertiance

     When getter is called the copmparision between setter count and getter 
     count could aware unneed calucloation of the returned value 
  """
  def __init__(self) -> None:
    """constructor """
    self.set_cnt = 0
    self.get_cnt = None
    pass

  def update_set(self):
    """ update setter count (should called with ervery set)"""
    self.set_cnt = self.set_cnt + 1
    pass

  def update_get(self):
    """ update getter count (should called with ervery set)"""
    if (self.get_cnt != None) and (self.set_cnt > self.get_cnt): 
      self.get_cnt = self.set_cnt
    pass

  def is_uptodate(self):
    """ return uptodate status"""
    return (self.set_cnt == self.get_cnt)
    pass
