from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO


class PDFParser():
    def __init__(self):
        print("Created PDFParser object.")

    def parsepdf(self, filepath, encoding="utf-8"):
        """
            Parses pdf and returns raw parsed content

            :param filepath: path to pdf file to be parsed
            :param encoding: encoding of the file, defaults to utf-8
            :return: parsed data
            """
        # file = open("pdfs/20120412_ShortHistory_en.pdf", "rb")
        if filepath == "":
            print("No filepath was privded.")
            return 0

        file = open(filepath, "rb", encoding=encoding)

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
