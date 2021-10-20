from operator import methodcaller

class Student:
    surname_and_name = []
    def __init__(self, name, surname, record_book_number, grades):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(record_book_number, int) and isinstance(grades, list):
            if name.isalpha() and surname.isalpha() and record_book_number > 0 and all(0 <= grade <= 100 for grade in grades) and not f'{surname} {name}' in self.surname_and_name:
                Student.surname_and_name.append(f'{surname} {name}')
                self.name = name
                self.surname = surname
                self.record_book_number = record_book_number
                self.grades = grades
            else: raise ValueError
        else: raise TypeError

    def count_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} {self.surname}, RECORD #{self.record_book_number}, average = {self.count_average_grade()}"

class Group:
    def __init__(self, *students):
        if all(isinstance(student, Student) for student in students):
            if len(students) <= 20:
                self.students = students
            else:
                raise ValueError
        else:
            raise TypeError

    def count_highest_score(self):
        top_students = sorted(self.students, key = methodcaller('count_average_grade'), reverse = 1)
        return top_students[:5]

    
    


stud1 = Student('Ivan', 'Klapatiuk', 1, [10, 11, 11, 10, 12, 9, 11, 9])
stud2 = Student('Yevhenii', 'Adamchenko', 2, [11, 8, 10, 11, 11, 9, 10, 12])
stud3 = Student('Volodymyr', 'Smyrnyy', 3, [9, 12, 11, 9, 10, 11, 11, 12])
stud4 = Student('Maksym', 'Perepelytsia', 4, [4, 10, 9, 12, 10, 6, 9, 12])
stud5 = Student('Petro', 'Sahaydachnyy', 5, [10, 12, 8, 12, 6, 10, 9, 8])
stud6 = Student('Anna', 'Karenina', 6, [8, 10, 12, 9, 9, 10, 5, 8])
stud7 = Student('Oksana', 'Datsiuk', 7, [10, 12, 8, 9, 9, 10, 8, 6])
stud8 = Student('Iryna', 'Omelchenko', 8, [10, 10, 9, 12, 10, 11, 9, 9])
stud9 = Student('Dariya', 'Sheyko', 9, [4, 12, 10, 6, 9, 11, 11, 9])
stud10 = Student('Diana', 'Krupko', 10, [11, 10, 8, 9, 11, 12, 6, 7])
stud11 = Student('Viktoriya', 'Lys', 11, [12, 11, 9, 9, 5, 4, 10, 12])
stud12 = Student('Ivanna', 'Karaim', 12, [12, 5, 9, 10, 11, 6, 6, 7])
stud13 = Student('Olha', 'Kniahynia', 13, [7, 5, 8, 12, 12, 10, 11, 11])
stud14 = Student('Serhii', 'Buryakivsky', 14, [10, 6, 12, 5, 9, 9, 11, 11])
stud15 = Student('Pavlo', 'Nedashkivsky', 15, [11, 9, 9, 12, 10, 8, 8, 8])

group_x = Group(stud1, stud2, stud3, stud4, stud5, stud6, stud7, stud8, stud9, stud10, stud11, stud12, stud13, stud14, stud15)
for student in group_x.count_highest_score():
    print(student)