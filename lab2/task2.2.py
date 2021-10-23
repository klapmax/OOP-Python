import re
import os.path
class Process:
    def __init__(self, name_of_file):
        if not isinstance(name_of_file, str):
            raise TypeError("incorrect type")
        elif not os.path.exists(name_of_file):
            raise FileNotFoundError("file not found")
        self.name_of_file = name_of_file

    def for_signs(self):
        file = open(self.name_of_file, "r")
        self.text = file.read()
        __signs = len(self.text)
        file.close()
        return f'Signs: {__signs}'

    def for_words(self):
        file = open(self.name_of_file, "r")
        self.text = file.read()
        __words = len(re.findall(r'[a-zA-Z-\']+', self.text))
        file.close()
        return f'Words: {__words}'

    def for_sentences(self):
        file = open(self.name_of_file, "r")
        self.text = file.read()
        __sentences = len(re.split(r'[.!?]+', self.text)) - 1
        file.close()
        return f'Sentences: {__sentences}'

object1 = Process("text.txt")
try:
    print(object1.for_words())
    print(object1.for_signs())
    print(object1.for_sentences())
except:
    TypeError("Incorrect data!")