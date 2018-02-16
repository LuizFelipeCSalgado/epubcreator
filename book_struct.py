__author__="Luiz Felipe C Salgado"
__version__="0.0.1"

from chaper import Chaper

class Book:
    """Chapers dict is an list of objects Chaper."""
    chapers = []
    name = ''
    path_root=''

    def __init__(self,name='',chapers=None,path=''):
        if not (
                chapers is None or
                (isinstance(chapers, list) and
                 all([isinstance(c, Chaper) for c in chapers]))):
            raise Exception('error','type of chapers list must be of chaper class')
        self.name = name
        self.chapers = chapers
        self.path_root=path

    def create_cover(self,path=''):
        # TODO: função que pega uma imagem e cria capa a partir do modelo capa.html
        pass

    def create_contet(self):
        # TODO: função que cria o sumário
        pass

    def set_chapers(self,chapers):
        self.chapers = chapers

    def style_to_all(self,path):
        """
        path: path to css file to
        Puts into html file a call to a css file for all the chapers.
        """
        path = """<link href="..\\Styles\\{}" rel="stylesheet" type="text/css" />""".format(path)
        for chaper in self.chapers:
            chaper.style_file = path

    def set_style(self,chaper,file_name):

        if isinstance(chaper,int):
            self.chapers[chaper].style_file = """<link href="..\\Styles\\{}" rel="stylesheet" type="text/css" />""".format(file_name+'.css')

        if isinstance(chaper,str):
            for i,d in enumerate(self.chapers):
                if d.title == chaper:
                    n = i
                    self.chapers[n].style_file = """<link href="..\\Styles\\{}" rel="stylesheet" type="text/css" />""".format(file_name+'.css')
