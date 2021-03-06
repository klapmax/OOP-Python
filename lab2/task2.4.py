class Binary_Tree:
    # initialization of tree, required checkings
    def __init__(self, code, price):
        self.left = None
        self.right = None
        self.code = code
        self.price = price
        if not isinstance(price, int) or not isinstance(code, int):
            raise TypeError("incorrect type of data")
        if price < 0 or code < 0 or not code or not price:
            raise ValueError("incorrect value")

    # movement on our tree
    def get_data(self, code, price):
        if self.code:
            if code == self.code:
                raise ValueError("incorrect data")
            if code < self.code:
                if self.left is None:
                    self.left = Binary_Tree(code, price)
                else:
                    self.left.get_data(code, price)
            elif code > self.code:
                if self.right is None:
                    self.right = Binary_Tree(code, price)
                else:
                    self.right.get_data(code, price)
        else:
            self.code = code
    
    def get_price(self, code):
        if code < self.code:
            if self.left is None:
                raise ValueError("Error")
            return self.left.get_price(code)
        elif code > self.code:
            if self.right is None:
                raise ValueError("Error")
            return self.right.get_price(code)
        else:
            return self.price

    def cost(self, code, quantity):
        price_of_product = self.get_price(code)
        final_price = price_of_product * quantity
        return final_price


object = Binary_Tree(1, 46)
object.get_data(2, 54)
object.get_data(3, 46)
object.get_data(4, 300)
object.get_data(5, 16)
object.get_data(6, 91)
object.get_data(7, 812)
object.get_data(8, 16)
object.get_data(9, 32)
object.get_data(10, 254)
print('Total value: ' + str(object.cost(7, 44)))