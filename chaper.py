__author__="Luiz Felipe C Salgado"
__version__="0.0.1"

class Chaper:
    def __init__(self,title="", text="",style_file=""):
        """Title and text of the chaper requierd to construct the object"""
        self.text = text
        self.title =title
        self.style_file="""<link href="..\\Styles\\{}" rel="stylesheet" type="text/css" />""".format('default.css')

    def set_style(self,file_name):
        self.style_file = """<link href="..\\Styles\\{}" rel="stylesheet" type="text/css" />""".format(file_name+'.css')

