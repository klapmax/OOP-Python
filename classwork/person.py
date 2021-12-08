class Person:
    """Describing Person class that contains primary information about some person."""
    def __init__(self, name, surname, patronymic, date, sex):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(patronymic, str) and isinstance(date, str) and isinstance(sex, str):
            if name.isalpha() and surname.isalpha() and patronymic.isalpha() and sex.isalpha():
                self.name = name
                self.surname = surname
                self.patronymic = patronymic
                self.date = date
                self.sex = sex
            else: raise ValueError
        else: raise TypeError
    """Getters"""
    @property
    def name(self):
        return self.__name
    @property
    def surname(self):
        return self.__surname
    @property
    def patronymic(self):
        return self.__patronymic
    @property
    def date(self):
        return self.__date
    @property
    def sex(self):
        return self.__sex
    """Setters"""
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Incorrect type of data!")
        if not name:
            raise ValueError("Invalid string (empty)!")
        self.__name = name
    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Incorrect type of data!")
        if not surname:
            raise ValueError("Invalid string (empty)!")
        self.__surname = surname
    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("Incorrect type of data!")
        if not patronymic:
            raise ValueError("Invalid string (empty)!")
        self.__patronymic = patronymic
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("Incorrect type of data!")
        if not date:
            raise ValueError("Invalid string (empty)!")
        self.__date = date
    @sex.setter
    def sex(self, sex):
        if not isinstance(sex, str):
            raise TypeError("Incorrect type of data!")
        if not sex:
            raise ValueError("Invalid string (empty)!")
        self.__sex = sex
    
    def __str__(self):
        return f"Name: {self.__name}, Surname: {self.__surname}, Patr.: {self.__patronymic}, Date of birth: {self.__date}, Sex: {self.__sex}."


"""Derived class named Employee that contains additional information about that person."""
class Employee(Person):
    def __init__(self, name, surname, patronymic, date, sex, organization, specialty, position, salary, work_experience):
        super().__init__(name, surname, patronymic, date, sex)
        if isinstance(organization, str) and isinstance(specialty, str) and isinstance(position, str) and isinstance(salary, int) and isinstance(work_experience, int):
            if organization.isalpha() and specialty.isalpha() and salary.is_integer() and work_experience.is_integer:
                self.organization = organization
                self.specialty = specialty
                self.position = position
                self.salary = salary
                self. work_experience = work_experience
            else: raise ValueError
        else: raise TypeError
    """Getters + Setters"""
    @property
    def organization(self):
        return self.__organization
    @organization.setter
    def organization(self, organization):
        if not isinstance(organization, str):
            raise TypeError("Incorrect type of data!")
        if not organization:
            raise ValueError("Invalid string (empty)!")
        self.__organization = organization
    @property
    def specialty(self):
        return self.__specialty
    @specialty.setter
    def specialty(self, specialty):
        if not isinstance(specialty, str):
            raise TypeError("Incorrect type of data!")
        if not specialty:
            raise ValueError("Invalid string (empty)!")
        self.__specialty = specialty
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position):
        if not isinstance(position, str):
            raise TypeError("Incorrect type of data!")
        if not position:
            raise ValueError("Invalid string (empty)!")
        self.__position = position
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, int):
            raise TypeError("Incorrect type of data!")
        if not salary:
            raise ValueError("Invalid string (empty)!")
        self.__salary = salary
    @property
    def work_experience(self):
        return self.__work_experience
    @work_experience.setter
    def work_experience(self, work_experience):
        if not isinstance(work_experience, int):
            raise TypeError("Incorrect type of data!")
        if not work_experience:
            raise ValueError("Invalid string (empty)!")
        self.__work_experience = work_experience

    def __str__(self):
        return f"Organization: {self.__organization}, Specialty: {self.__specialty}, Position: {self.__position}, Salary: {self.__salary}, Work experience: {self.__work_experience}."

class Organization(Employee):
    def __init__(self, name, surname, patronymic, date, sex, organization, specialty, position, salary, work_experience):
        super().__init__(name, surname, patronymic, date, sex, organization, specialty, position, salary, work_experience)
        