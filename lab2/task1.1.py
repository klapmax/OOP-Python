class Rectangle:
    def __init__(self, lenght=1, width=1):
        if not isinstance(lenght, float) or not isinstance(width, float):
            raise TypeError("Uncorrect type") 
        if lenght < 0 or lenght > 20 or width < 0 or width > 20:
            raise ValueError("Uncorrect value")
        self.__lenght = lenght
        self.__width = width

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, len):
        if not isinstance(len, float): 
            raise TypeError("Uncorrect type for lenght")
        if len < 0 or len > 20:
            raise ValueError("Uncorrect value for lenght")
        self.__lenght = len
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, wid):
        if not isinstance(wid, float): 
            raise TypeError("Uncorrect type for width")
        if wid < 0 or wid > 20:
            raise ValueError("Uncorrect value for width")
        self.__width = wid

    def perimeter(self):
        return (self.width + self.lenght)*2
        
    def area(self):
        return self.width * self.lenght

def main():
    rectangle = Rectangle(14.0, 2.0)
    print('Lenght is: ', rectangle.lenght)
    print('Width is: ', rectangle.width)
    print('perimeter is: ', rectangle.perimeter())
    print('area is: ', rectangle.area())
    return { "success": True }

print(main())