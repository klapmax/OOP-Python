import re
import os.path
class Process:
    def __init__(self, name_of_file):
        if not isinstance(name_of_file, str):
            raise TypeError("incorrect type")
        elif not os.path.exists(name_of_file):
            raise FileNotFoundError("file not found")
        self.name_of_file = name_of_file

    def function(self):
        file = open(self.name_of_file, "r")
        self.text = file.read()
        __signs = len(self.text) 
        __words = len(re.findall(r'[a-zA-Z-\']+', self.text))
        __sentences = len(re.split(r'[.!?]+', self.text)) - 1
        file.close()
        return f'Signs: {__signs}\nWords: {__words}\nSentences: {__sentences}' 
    
object = Process("text.txt")
try:
    print(object.function())
except:
    print("Incorrect data!")