class ArrayList:
    def __init__(self):
        self.__Array2 = []
        self.__Array = []
        self.__output_str = str()

    def append(self, *strings):
        for string in strings:
            self.__Array.append(string)

    def appstart(self, scores: list):
        for i, key in enumerate(scores):
            self.__Array.insert(i, key)

    def appindex(self, index, score):
        self.__Array.insert(index, score)

    def EditSize(self, size):
        self.__Array2 = list()
        for i in range(size):
            self.__Array2.append(self.__Array[i])
        self.__Array = self.__Array2

    def print(self, index=None):
        if index is None:
            return self.__Array
        else:
            for i in range(index):
                self.__Array2.append(self.__Array[i])
            self.__Array = self.__Array2
            return self.__Array

    def PrintStr(self, index=None):
        self.__output_str = str()
        if index is None:
            self.__output_str = " ".join(self.__Array)
            return self.__output_str
        else:
            for i in range(index):
                self.__output_str += self.__Array[i] + " "
            return self.__output_str

    def DeleteSpace(self, index: int): #замена пробелов на _
        text = self.__Array[index]
        text_new = ""
        for string in text:
            if string == " ":
                text_new += "_"
            else:
                text_new += string
        self.__Array[index] = text_new

    def reverseSlash(self, index: int):
        text = self.__Array[index]
        text_new = ""
        for string in text:
            if string == "/":
                text_new += "\\"
            else:
                text_new += string
        self.__Array[index] = text_new

    def doubleSlash(self, index: int):
        text = self.__Array[index]
        text_new = ""
        for string in text:
            if string == "/":
                text_new += "\\\\"
            else:
                text_new += string
        self.__Array[index] = text_new

    def upper(self, index: int):
        text = self.__Array[index]
        self.__Array[index] = text.upper()
