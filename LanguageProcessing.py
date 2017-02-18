import operator


class LanguageProcessing():
    def __init__(self):
        print("Create LanguageProcessing object.")

    def wordfrequency(self, data):
        """

        :param data:
        :return:
        """
        dict = {}
        for word in data.split():
            count = dict.get(word, 0)
            dict[word] = count + 1
        listdict = dict.items()
        print(sorted(listdict, key=operator.itemgetter(1)))

        return dict