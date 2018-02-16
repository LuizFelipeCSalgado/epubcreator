__author__="Luiz Felipe C Salgado"
__version__="0.0.1"

import text_fomatter as tf
import docx
from chaper import Chaper
from book_struct import Book


def split_into_pages(text):
    """
    The character to split page is <pg>. Where it is on the docx file
    will be the limit of one chaper (.html page) to another.\n
    :param text: text (string) with all pages\n
    :return: list of texts of each page
    """
    return text.split('<pg>')


def format(paragraph):
    """"
    Function recieves a list of docx.textoparagraph.Paragraph and returns
    a text with HTML tags of:\n
        <b> bold </b>
        <i> italic </i>
        <u> underline </u>
        <p> paragraph </p>
    :param paragraph: docx.textoparagraph.Paragraph list.
    :returns: A string with the whole text given with the the format tags.
    """
    text_final = ''
    for par in paragraph:
        txt=''
        txt2=''
        for run in par.runs:
            txt = run.text
            if par.runs.__len__==0:
                break
            if run.bold or run.italic or run.underline:
                if run.bold:
                    txt = tf.bold(txt)
                if run.italic:
                    txt = tf.italic(txt)
                if run.underline:
                    txt = tf.underline(txt)
            else:
                if '\n' in run.text:
                    run.text.replace('\n', '<br \>')
            txt2 += txt
        text_final += tf.paragraph(txt2) + '\n'


    text_final += text_final
    text_final.replace('<p></p>','')
    return text_final

def read_doc(path):
    doc_document = docx.Document(path)
    return doc_document.paragraphs

def create_html_chaper(chaper_HTML,path):
    """
    Create a single HTML file with a Chaper object.
    :param chaper_HTML: Chaper object.
    """
    if not (chaper_HTML is None or isinstance(chaper_HTML, Chaper)):
        raise Exception('error', 'type of chapers list must be of chaper class')

    with open('html_models/chaper.html','r') as model:
        temp_text=''
        for i in model.readlines():
            temp_text +=i
        temp_text = temp_text.replace("??MAIN TEXT??", chaper_HTML.text)
        temp_text=temp_text.replace("??TITLE??", chaper_HTML.title)
        if chaper_HTML.style_file is not None:
            temp_text=temp_text.replace("??CSS FILE??", chaper_HTML.style_file)
        else:
            temp_text=temp_text.replace("??CSS FILE??",'<link href="..\\Styles\\default.css" rel="stylesheet" type="text/css" />')
        # DEFINIR DIRETÓRIO DE CRIAÇÃO DE PÁGINAS
        new_file = open(path+'\\OEBPS\\Text\\'+chaper_HTML.title + '.html', 'w')
        new_file.write(temp_text)
        new_file.close()

def make_chapers(title,chapers,style=None):
    """
    :param title: List of Titles of the chapers (List of Strings)
    :param chapers: List of text of Chapers (List of Strings)
    :param style: List of paths of css file.
    :return: List of Chaper objects.
    """

    chap = []
    if style==None:
        style = ['' for a in range(len(chapers))]
    for i,c in enumerate(chapers):
        chap.append(Chaper(title[i],c,style[i]))
    return chap

def create_HTML_chapers(path,chaper_Chaper=None, chaper_Book=None):
    """
    Create HTML files from a list of Chapers or a Book object, or both.
    :param path:
    :param chaper_Chaper: A list of Chapers object.
    :param chaper_Book:  A Book object.
    """

    if chaper_Chaper is not None:
        if not(isinstance(chaper_Chaper,list) or all([isinstance(c,Chaper) for c in chaper_Chaper])):
            raise Exception('error','chaper_Chaper must be a list of Chaper objects')
        for c in chaper_Chaper:
            create_html_chaper(c,path)

    if chaper_Book is not None:
        if not isinstance(chaper_Book,Book):
            raise Exception ('error', 'chaper_Book must be a Book object')
        for c in chaper_Book.chapers:
            create_html_chaper(c,path)

