import re
class Process:
    def __init__(self, name_of_file):
        file = open(name_of_file, "r")
        self.text = file.read()
        file.close()

    def function(self):
        signs = len(self.text) 
        words = len(re.findall(r'[a-zA-Z-\']+', self.text))
        sentences = len(re.split(r'[.!?]+', self.text)) - 1
        return f'Signs: {signs} \nWords: {words} \nSentences: {sentences}' 
    
object = Process("text.txt")

try:
    print(object.function())
except:
    print("Incorrect data!")
