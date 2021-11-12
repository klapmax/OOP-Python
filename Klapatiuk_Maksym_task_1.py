class Queue:
    def __init__(self, queue_number, surname_name_patronymic, family, date):
        if isinstance(queue_number, int) and isinstance(surname_name_patronymic, str) and isinstance(family, str) and isinstance(date, str):
            if queue_number > 0 and surname_name_patronymic.isalpha() and family.isalpha():
                self.queue_number = queue_number
                self.surname_name_patronymic = surname_name_patronymic
                self.family = family
                self.date = date
            else: raise ValueError("incorrect values")
        else: raise TypeError("incorrect data")

    @property
    def queue_number(self):
        return self.__queue_number

    @property
    def surname_name_patronymic(self):
        return self.__surname_name_patronymic
    
    @property
    def family(self):
        return self.__family

    @property
    def date(self):
        return self.__date

    @queue_number.setter
    def set_queue_number(self, queue_number):
        self.__queue_number = queue_number

    @surname_name_patronymic.setter
    def set_surname_name_patronymic(self, surname_name_patronymic):
        self.__surname_name_patronymic = surname_name_patronymic

    @family.setter
    def set_family(self, family):
        self.__family = family

    @date.setter
    def set_date(self, date):
        self.__date = date

    def __str__(self):
        return f"Number: {self.__queue_number}\nMember: {self.__surname_name_patronymic}\nFamily: {self.__family}\nDate: {self.__date}"
