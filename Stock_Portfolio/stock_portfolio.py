
class user:
    def __init__(self, name):
        self.user = name
    
    portfolio = {}

    def buy_stock(self, name, quantity):
        if quantity <= 0:
            raise QuantityError("Quantity can not be less than 1")
        elif name not in self.portfolio:
            self.portfolio[name] = quantity
        else:
            self.portfolio[name] += quantity
            
    def sell_stock(self, name, quantity):
        if quantity <= 0:
            raise QuantityError("Quantity can not be less than 1")
        elif name not in self.portfolio:
            raise MissingError('Stock not in profolio')
        elif self.portfolio[name] < quantity:
            raise ShareSaleException("Insufficient quantity of stock")
        else:
            self.portfolio[name] -= quantity
            if self.portfolio[name] == 0:
                self.portfolio.pop(name)

    def show_stock(self, name):
        return self.portfolio[name]



class ShareSaleException(Exception):
    # print("Insufficient quantity of stock")
    pass

class QuantityError(Exception):
    pass

class MissingError(Exception):
    pass