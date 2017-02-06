# -*- coding: utf-8 -*-

from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO


def parsePDF():
    # file = open("pdfs/20120412_ShortHistory_en.pdf", "rb")
    file = open("pdfs/document.pdf", "rb")


    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    for page in PDFPage.get_pages(file):
        interpreter.process_page(page)

    result = output.getvalue()

    # Close
    file.close()
    converter.close()
    output.close()

    return result


def tofile(filename, data):

    outfile = open(filename + ".txt", "w", encoding="utf-8")
    outfile.write(data)
    outfile.close()

    return 0

def main():
    result = parsePDF()
    print(result)
    print(len(result.split(".")))
    tofile("testfile", result)

if __name__ == "__main__":
    main()
