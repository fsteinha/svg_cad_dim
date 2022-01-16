import pprint
from i_svg import I_SVG
from svgpathtools import svg2paths

pp = pprint.PrettyPrinter(indent=4)

class SVG_Interpreter():
  def __init__(self, i_svg: I_SVG):
    self.i_svg = i_svg
    self.file_svg = None

    pass

  def interpret(self):
    l_paths, attributes = svg2paths(self.i_svg.getSvg_file())

    for path in l_paths:
      print(type(path))


    
    pass

  

    