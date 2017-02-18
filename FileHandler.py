import re

class FileHandler():

    def __init__(self):
        print("Created a FileHandler object.")

    def load(self, filepath, encoding='utf-8'):

        file = open(filepath, "r", encoding=encoding)
        output = file.read()
        file.close()
        return output

    # filepath or filename how
    def write(self, filename, content):
        name = "{}.txt".format(filename)
        outfile = open(name, "w", encoding="utf-8")
        # TODO: A better way to strip special characters
        data = re.sub(r"[\(\)\-\–\%\|\,\.\"]", "", content)
        outfile.write(data)
        outfile.close()
        return 0