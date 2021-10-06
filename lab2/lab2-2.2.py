class Process:
    def __init__(self, name_of_file):
        self.name_of_file = name_of_file

    def count_words(self): #рахує к-сть слів у текстовому файлі
        try:
            file = open(self.name_of_file, 'r')
            line = file.read()
            wordslist = line.split()
            words = len(wordslist)
            file.close()
            return f'Words: {words}'
        except FileNotFoundError:
            return None

    def count_sentences(self): #рахує к-сть речень 
        try:
            file = open(self.name_of_file, 'r')
            line = file.read()
            sentences = 0
            flag = 0
            for i in range(len(line)):
                if line[i] != '.' and flag == 0:
                    sentences +=1
                    flag = 1
                else:
                    if line[flag] == ".":
                        flag = 0
            file.close()
            return f'Sentences: {sentences}'            
        except FileNotFoundError:
            return None

    def count_of_characters(self):
        return f'Characters: {len(self.name_of_file)}'

object = Process("text.txt")
print(object.count_words())
print(object.count_sentences())
print(object.count_of_characters())