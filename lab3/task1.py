import time
import json
from datetime import datetime
class regular_ticket:   #superclass
    def __init__(self, event_name, event_date, customer, price):
        if(isinstance(price, int) or isinstance(price, float)):
            self.ticket_number = self.generate_number()
            self.price = price
            self.event_name = event_name
            self.event_date = event_date
            self.customer = customer
            self.ticket()
        else:
            raise TypeError

    def ticket(self):
        file = open(self.ticket_number + ".json", 'w')
        json.dump(self.__dict__, file, indent = 2)
        file.close()



    def __str__(self):
        return f"{self.ticket_number} {self.price}"

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
        return f"Ticket number: {month}{day}{year}-{hour}{minute}{second}{mlsec}"

    def days_to_event(event_date):
        try:
            d1 = datetime.now()
            d2 = datetime.strptime(event_date, "%d.%m.%Y")
        except:
            raise ValueError("Invalid  format of date")
        return abs((d2 - d1).days)

class advance_ticket(regular_ticket):   #derived class
    def __init__(self, event_name, event_date, customer, price):
        super().__init__(event_name, event_date, customer, round(price*0.6, 1))

class late_ticket(regular_ticket):  #derived class
    def __init__(self, event_name, event_date, customer, price):
        super().__init__(event_name, event_date, customer, round(price*1.1, 1))

class student_ticket(regular_ticket):   #derived class
    def __init__(self, event_name, event_date, customer, price):
        super().__init__(event_name, event_date, customer, round(price*0.5))


def main():
    reg_ticket = regular_ticket("dsjhsd", "21.02.2022", "Ira", 1400)
    adv_ticket = advance_ticket("dsjhsd", "21.02.2022", "Ira", 1400)
    lt_ticket = late_ticket("dsjhsd", "21.02.2022", "Ira", 1400)
    stud_ticket = student_ticket("dsjhsd", "21.02.2022", "Ira", 1400)
    print(reg_ticket)
    print(adv_ticket)
    print(lt_ticket)
    print(stud_ticket)
main()