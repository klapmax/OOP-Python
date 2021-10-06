from fractions import Fraction
class Rational:
    def init(self, numerator = 1, denominator = 1):
        self.__numerator = numerator
        self.__denominator = denominator

        if isinstance(self.__numerator, int) and isinstance(self.__denominator, int):
            try:
                action = Fraction(self.__numerator, self.__denominator)
            except ZeroDivisionError: quit("denominator != 0")
        else:
            quit("error")

    def oper(self):
        return Fraction(self.__numerator, self.__denominator)

    def calculate(self):
        return self.__numerator / self.__denominator


object = Rational()
print(object.oper())
print(object.calculate())