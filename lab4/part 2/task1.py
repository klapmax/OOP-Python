import json
from abc import ABC, abstractmethod

class ICourse(ABC):
    """Interface for Course """
    @abstractmethod
    def __init__(self, title, teacher, list_of_topics):
        pass

class Course(ICourse):
    """ Class for set information for courses """
    def __init__(self, title, teacher, list_of_topics):
        self.title = title
        self.teacher = teacher
        self.list_of_topics = list_of_topics

    @property
    def title(self):
        return self._title
    @property
    def teacher(self):
        return self._teacher
    @property
    def list_of_topics(self):
        return self._list_of_topics
    @property
    def list_of_topics(self):
        return self._list_of_topics

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("incorrect type")
        if not all(letter.isalpha() for letter in title):
            raise ValueError("Invalid name, surname")
        if not title:
            raise ValueError("string is empty")
        self._title = title

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, str):
            raise TypeError("incorrect type")
        if not teacher:
            raise ValueError("string is empty")
        self._teacher = teacher

    @list_of_topics.setter
    def list_of_topics(self, list_of_topics):
        if not all([isinstance(topic, str) for topic in list_of_topics]):
            raise TypeError("Incorrect type")
        if not list_of_topics:
            raise ValueError("string is empty")
        self._list_of_topics = list_of_topics

class ILocalCourse(ABC):
    """Interface for ILocalCourse """
    @abstractmethod
    def __init__(self, title, teacher, list_of_topics):
        pass
    @abstractmethod
    def __str__(self):
        pass


class LocalCourse(Course, ILocalCourse):
    """Class for getting information about Local course """
    def __init__(self, title, teacher, list_of_topics):
        super().__init__(title, teacher, list_of_topics)

    def __str__(self):
        return f' Local course: {self.title} teacher: {self.teacher}, topics: {self.list_of_topics}'


class IOffsiteCourse(ABC):
    @abstractmethod
    def __init__(self, title, teacher, list_of_topics):
        pass

    @abstractmethod
    def __str__(self):
        pass


class OffsiteCourse(Course, IOffsiteCourse):
    """Class for get information about Offsite course """
    def __init__(self, title, teacher, list_of_topics):
        super().__init__(title, teacher, list_of_topics)

    def __str__(self):
        return f' Offsite course: {self.title} teacher: {self.teacher}, topics: {self.list_of_topics}'

class ITeacher(ABC):
    """Interface for Teacher"""
    @abstractmethod
    def __init__(self, name, name_course=None):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Teacher(ITeacher):
    def __init__(self, name, name_course=None):
        self.name = name
        self.name_course = name_course

    @property
    def name(self):
        return self._name
    @property
    def name_course(self):
        return self._name_course

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("incorrect type")
        if not name:
            raise ValueError("string is empty")
        self._name = name

    @name_course.setter
    def name_course(self, name_course):
        if not all([isinstance(course, str) for course in name_course]):
            raise TypeError("Incorrect type")
        if name_course is None:
            name_course = [""]
        self._name_course = name_course

    def __str__(self):
        return f' {self.name}: course - {self.name_course}'


class ICourseFactory(ABC):
    """Interface for ICourseFactory """
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def add_teacher(self, name, course=None):
        pass
    @abstractmethod
    def add_course(self, title, teacher, list_of_topics, type_course):
        pass
    @abstractmethod
    def del_teacher(self, name, title):
        pass


class CourseFactory(ICourseFactory):
    """Factory for create teacher and Local/Offsite course """
    def __init__(self):
        self.courses = {}
        self.teachers = {}

    def add_teacher(self, name, courses=None):
        if courses is None:
            courses = []
        self.teachers = json.load(open("Teachers.json"))
        with open('Teachers.json', 'w') as file:
            self.teachers.update({name: Teacher(name, courses).__dict__})
            json.dump(self.teachers, file, indent=2)
        return Teacher(name, courses)

    def add_course(self, title, teacher, list_of_topics, type_course):
        dict_of_courses = {"Local": LocalCourse(title, teacher.name, list_of_topics),
                           "Offsite": OffsiteCourse(title, teacher.name, list_of_topics)}
        if title not in teacher.name_course:
            teacher.name_course.append(title)
        self.add_teacher(teacher.name, teacher.name_course)
        self.courses = json.load(open("Courses.json"))
        with open('Courses.json', 'w') as file:
            self.courses.update({title: dict_of_courses[type_course].__dict__})
            json.dump(self.courses, file, indent=2)
        return dict_of_courses[type_course]

    def del_teacher(self, name, title):
        with open("Teachers.json", 'r') as file:
            self.teachers = json.load(open("Teachers.json"))
        if name in self.teachers.keys():
            del self.teachers[name]
            self.courses[title]["teacher"] = ""
        with open('Courses.json', 'w') as file:
            json.dump(self.courses, file, indent=2)
        with open('Teachers.json', 'w') as file:
            json.dump(self.teachers, file, indent=2)
        return self.teachers

create_course = CourseFactory()
teacher_1 = create_course.add_teacher("Maksym Klapatiuk")
course_1 = create_course.add_course("Teorver", teacher_1, ["Classes", "Swing"], "Local")
teacher_2 = create_course.add_teacher("Buryak", ["English", "Python"])
course_2 = create_course.add_course("Shald", teacher_2, ["Classes", "Swing"], "Offsite")
#print(course_1)
#print(course_2)
#print(teacher_1)
#print(teacher_2)
#create_course.del_teacher
print("Teachers:")
print('\n'.join("{}: \n{}".format(key, value) for key, value in create_course.teachers.items()))
print("\nCourses:")
print('\n'.join("{}: \n{}".format(key, value) for key, value in create_course.courses.items()))