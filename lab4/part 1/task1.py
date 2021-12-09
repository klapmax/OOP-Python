from math import gcd
class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        if isinstance(numerator, int) and isinstance(denominator, int):
            if denominator:
                self.__numerator = numerator // gcd(numerator, denominator)
                self.__denominator = denominator // gcd(numerator, denominator)
            else:
                raise ZeroDivisionError("Zero division!")
        else:
            raise TypeError("Incorrect type!")

    def get_float(self):
        return self.__numerator/self.__denominator

    def get_simple(self):
        return f'{self.__numerator}/{self.__denominator}'

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Ratoinals only!")
        numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        denominator = self.__denominator * other.__denominator
        return Rational(numerator, denominator)
        
    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Ratoinals only!")
        numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        denominator = self.__denominator * other.__denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Ratoinals only!")
        denominator = int(self.__denominator * other.__denominator)
        numerator = int(self.__numerator * other.__numerator)
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Ratoinals only!")
        denominator = int(self.__denominator * other.__numerator)
        numerator = int(self.__numerator * other.__denominator)
        return Rational(numerator, denominator)
    
    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rationals only!")
        return self.__numerator * other.__denominator > self.__denominator * other.__numerator

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rationals only!")
        return self.__numerator * other.__denominator < self.__denominator * other.__numerator
    
    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rationals only!")
        return self.__numerator/self.__denominator >= other.__numerator/other.__denominator

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rationals only!")
        return self.__numerator/self.__denominator <= other.__numerator/other.__denominator
    
    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rationals only!")
        return self.__numerator/self.__denominator == other.__numerator/other.__denominator
    
    def __ne__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rationals only!")
        return self.__numerator/self.__denominator != other.__numerator/other.__denominator
        
    def __iadd__(self,other):      
        if not isinstance(other, Rational):
            raise TypeError("Rationals only!")
        self.numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        self.__denominator = self.__denominator * other.__denominator
        return self

    def __isub__(self,other):     
        if not isinstance(other, Rational):
            raise TypeError("Rationals only!") 
        self.__numerator  = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        self.__denominator = self.__denominator*other.__denominator
        return self

def main():
    a = Rational(7, 19)
    b = Rational(5, 13)
    print('Addition: ', (a + b).get_simple())
    print('Substraction: ', (a - b).get_simple())
    print('Multiplication: ', (a * b).get_simple())
    print('Division: ', (a / b).get_simple())
    print('Is 1st higher?: ', a > b)
    print('Is 2nd higher?: ', a < b)
    print('Are 1st and 2nd equal?: ', a == b)
    print('Are 1st and 2nd different?: ', a != b)
main()