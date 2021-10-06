class Rectangle:
    def setter(self, length, width):
        if user_width > 0.0 and user_width <= 20.0 and user_length > 0.0 and user_length <= 20.0:
            self.width = width
            self.length = length
        else:
            return None 
            

    def __init__(self, length = 1, width = 1):
        self.setter(length, width)
    
    def getter(self):
        return self.length, self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.width * self.length

try:
    user_length = float(input())
    user_width = float(input())
    if user_width >= 0 and user_length >= 0:
        object = Rectangle(user_length, user_width)
        print("perimeter = ", object.perimeter(),', ' "area = " ,object.area())
except:
    print("Error!!!")