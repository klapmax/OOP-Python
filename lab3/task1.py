import time
import json
import os
from datetime import datetime

discount_40_perc = 0.6
student_discount = 0.5
late_price = 1.1
class Regular_ticket:   #superclass
    def __init__(self, customer, event_name, price, event_date):
        self.ticket_number = self.generate_number()
        self.__price = price
        self.event_name = event_name
        self.event_date = event_date
        self.customer = customer
        self.ticket()

    def ticket(self):
        file = open(self.ticket_number + '.json', "w")
        json.dump(self.__dict__, file, indent = 2)
        file.close()

    def get_ticket(file_name):
        if not os.path.exists(file_name + '.json'):
            raise FileNotFoundError
        file = open(file_name + '.json', "r")
        input = json.load(file)
        customer = input['customer']
        price = input['price']
        event_name = input['event_name']
        event_date = input['event_date']      
        file.close()
        return f"{file_name}\n{customer}\n{event_name}\nPrice: {round(price, 1)}\n{event_date}"

    def create_ticket(file_name):
        if not os.path.exists(file_name):
            raise FileNotFoundError
        file = open(file_name, "r")
        input = json.load(file)
        customer = input['customer']
        general_price = input['general_price']
        event_name = input['event_name']
        event_date = input['event_date']
        student = False
        if 'student' in input:
            student = input['student']
        file.close()
        return Regular_ticket.generate_ticket(customer, event_name, event_date, general_price, student)

    def generate_ticket(customer, event_name, event_date, general_price, student = False):
        if not isinstance(customer, str) and not isinstance(event_name, str) and not isinstance(event_date, str) and not isinstance(general_price, int) and not isinstance(student, bool):
            raise TypeError("wrong types of data")
        if student:
            return Student_ticket(customer, event_name, general_price, event_date)
        elif Regular_ticket.days_to_event(event_date) >= 60:
            return Advance_ticket(customer, event_name, general_price, event_date)
        else:
            return Late_ticket(customer, event_name, general_price, event_date)
    def __str__(self):
        return f"{self.ticket_number}, {self.__price}"

    @property
    def ticket_number(self):
        return self.__ticket_number

    @property
    def price(self):
        return self.__price

    @ticket_number.setter
    def ticket_number(self, ticket_number):
        self.__ticket_number = ticket_number

    @price.setter
    def price(self, price):
        self.__price = price

    def generate_number(self):
        real_time = datetime.now() 
        month = real_time.month
        day = real_time.day
        year = real_time.year
        hour = real_time.hour
        minute = real_time.minute
        second = real_time.second
        mlsec = real_time.microsecond
        time.sleep(0.0025)
        return f"{month}{day}{year}-{hour}{minute}{second}{mlsec}"

    def days_to_event(event_date):
        try:
            first = datetime.now()
            second = datetime.strptime(event_date, "%d.%m.%Y")
        except:
            raise ValueError("Wrong format of date")
        return abs((second - first).days)

class Advance_ticket(Regular_ticket):   #derived class
    def __init__(self, customer, event_name, price, event_date):
        super().__init__(customer, event_name, price, event_date)
    @property
    def price(self):
        return self.__price * discount_40_perc
    @price.setter
    def price(self, price):
        self.__price = price

class Late_ticket(Regular_ticket):  #derived class
    def __init__(self, customer, event_name, price, event_date):
        super().__init__(customer, event_name, price, event_date)
    @property
    def price(self):
        return self.__price * late_price
    @price.setter
    def price(self, price):
        self.__price = price

class Student_ticket(Regular_ticket):   #derived class
    def __init__(self, customer, event_name, price, event_date):
        super().__init__(customer, event_name, price, event_date)
    @property
    def price(self):
        return self.__price * discount_40_perc
    @price.setter
    def price(self, price):
        self.__price = price

def main():
    print(Regular_ticket.create_ticket("order.json"))
    #print(regular_ticket.ticket(''))
main()