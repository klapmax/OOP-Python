class Product:
    def __init__(self, name_of_product, price, dimension, description):
        self.__name = name_of_product
        self.price = price
        self.__dimension = dimension
        self.__description = description

class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__mobile_phone = mobile_phone

class Order():
    def __init__(self, customer, *products):
        self.__customer = customer
        self.__products = products

    def method(self):
        cost = 0
        for i in range(len(self.__products)):
            cost += self.__products[i].price
        return cost

Maks = Customer('Klapatiuk', 'Maksym', 'Volodymyrovych', '+380687046036')
Xiaomi = Product('Cellphone', 15000, 'L = 16, W = 8', 'black')
Sennheiser = Product('Headphones', 8000, 'Weight = 100 g, Height = 3', 'black-blue')
order = Order(Maks, Xiaomi, Sennheiser)

print(order.method())