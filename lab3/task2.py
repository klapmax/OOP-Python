import json
from datetime import datetime
import calendar
class Customer:
    """describing customer class"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def name(self):
        return self.__name
    @property
    def surname(self):
        return self.__surname
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Incorrect type of data!")
        if not all(char.isalpha() for char in name):
            raise ValueError("Invalid name!")
        if not name:
            raise ValueError("Invalid string (empty)!")
        self.__name = name
    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Incorrect type of data!")
        if not all(char.isalpha() for char in surname):
            raise ValueError("Invalid name!")
        if not surname:
            raise ValueError("Invalid string (empty)!")
        self.__surname = surname

    def __str__(self):
        return f"Customer: {self.name} {self.surname}"



class Pizza:
    """describing pizza class"""
    def __init__(self):
        self.list_of_ingredients = {}

    def add_ingredients(self, components):
        for ingr in components:
            if ingr not in ingredients.keys():
                raise ValueError("No such ingredient!")
            if not isinstance(ingr, str):
                raise TypeError("Input error!")
            self.list_of_ingredients.update({ingr: ingredients[ingr]})
        self.price = sum(list(self.list_of_ingredients.values())) + self.price
    
    def __repr__(self):
        return  f"\nPizza of {self.type_of_pizza()} is {self.name_of_pizza} {self.primary_price()}. So price with added: {self.price} \nIngredients: {self.description}, Extra ingredients: {self.list_of_ingredients}"             f""

            
class Monday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Monday.__name__]['pizza']
        self.price = info[Monday.__name__]['cost']
        self.description = info[Monday.__name__]['ingredients']

    def type_of_pizza(self):
        return Monday.__name__

    def primary_price(self):
        return info[Monday.__name__]['cost']
             
class Tuesday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Tuesday.__name__]['pizza']
        self.price = info[Tuesday.__name__]['cost']
        self.description = info[Tuesday.__name__]['ingredients']

    def type_of_pizza(self):
        return Tuesday.__name__

    def pimary_price(self):
        return info[Tuesday.__name__]['cost']

class Wednesday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Wednesday.__name__]['pizza']
        self.price = info[Wednesday.__name__]['cost']
        self.description = info[Wednesday.__name__]['ingredients']

    def type_of_pizza(self):
        return Wednesday.__name__

    def pimary_price(self):
        return info[Wednesday.__name__]['cost']

class Thursday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Thursday.__name__]['pizza']
        self.price = info[Thursday.__name__]['cost']
        self.description = info[Thursday.__name__]['ingredients']

    def type_of_pizza(self):
        return Thursday.__name__

    def primary_price(self):
        return info[Thursday.__name__]['cost']

class Friday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Friday.__name__]['pizza']
        self.price = info[Friday.__name__]['cost']
        self.description = info[Friday.__name__]['ingredients']

    def type_of_pizza(self):
        return Friday.__name__

    def pimary_price(self):
        return info[Friday.__name__]['cost']

class Saturday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Saturday.__name__]['pizza']
        self.price = info[Saturday.__name__]['cost']
        self.description = info[Saturday.__name__]['ingredients']

    def type_of_pizza(self):
        return Saturday.__name__

    def pimary_price(self):
        return info[Saturday.__name__]['cost']

class Sunday(Pizza):
    def __init__(self):
        super().__init__()
        self.name_of_pizza = info[Sunday.__name__]['pizza']
        self.price = info[Sunday.__name__]['cost']
        self.description = info[Sunday.__name__]['ingredients']

    def type_of_pizza(self):
        return Sunday.__name__

    def pimary_price(self):
        return info[Sunday.__name__]['cost']

class Order:
    def __init__(self, customer, day):
        if not isinstance(customer, Customer):
            raise TypeError("Invalid type!")
        self.customer = customer
        self.day = day
        self.pizza = Pizza()
        self.pizza_list = []
    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, day):
        try:
            self._day = day
            if isinstance(day, str):
                self._day = datetime.strptime(day, "%d.%m.%Y")
        except ValueError as err:
            raise

    def type_of_pizza(self):
        """Method that returns pizza-of-day"""
        dict_pizza = {"Monday":Monday(), "Tuesday": Tuesday(), "Wednesday": Wednesday(),"Thursday":Thursday(),
                      "Friday": Friday(), "Saturday":Saturday(), "Sunday": Sunday()}
        return dict_pizza[calendar.day_name[self.day.weekday()]] 

    def add_pizza(self, add_pizza):
        """"Method that adds the pizza to order."""
        if not isinstance(add_pizza, list):
            raise TypeError("Incorrect type!")
        for item in add_pizza:
            if not isinstance(item, Pizza):
                raise TypeError("Incorrect type!")
        for i in add_pizza:
            self.pizza_list.append(i)
    
    def total_value(self):
        """"Counts and returns the total price of the whole order"""
        total = 0
        for item in self.pizza_list:
            total += item.price
        return total
    
    def __str__(self):
        return f'{self.customer}, {self.pizza_list}'

with open('pizza_of_the_day.json', 'r') as file:
    info = json.load(file)
with open('ingredients.json', 'r') as file:
    ingredients = json.load(file)

customer1 = Customer("Poligraf", "Sharikov")
order1 = Order(customer1, "18.11.2021")
pizza1 = order1.type_of_pizza()
pizza1.add_ingredients(["tomato", "ham"])
pizza2 = order1.type_of_pizza()
pizza2.add_ingredients(["pineapples"])
order1.add_pizza([pizza1, pizza2])
print(order1)
print("Total value order: " + str(order1.total_value()))

customer2 = Customer("Professor", "Preobrazhenskiy")
order2 = Order(customer2, "15.11.2021")
pizza3 = order2.type_of_pizza()
pizza3.add_ingredients(["corn", "pineapples"])
pizza2 = order2.type_of_pizza()
order2.add_pizza([pizza3])
print(order2)
print("Total value order: " + str(order2.total_value()))

with open('order_of_pizzas.json', 'w') as file:
    json.dump(pizza3.__dict__, file, indent = 3)

add_ingredients = { "cheese": 25,
    "mushrooms": 10,
    "ham": 30,
    "squid": 50,
    "shrimp": 50,
    "tomato": 5,
    "pepper": 5,
    "olive": 5,
    "salami": 25,
    "pineapples": 10,
    "corn": 10,
    "chicken": 30 }

with open('ingredients.json', 'w') as file:
    json.dump(add_ingredients, file, indent = 3)