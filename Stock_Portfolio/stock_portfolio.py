

# class stock:
#     def __init__(self, name, quantity, price):
#         self.name_of_stock = name
#         self.quantity = quantity
#         self.price = price

class user:
    def __init__(self, name):
        self.user = name
    
    portfolio = {}

    def buy_stock(self, name, quantity):
        if name not in self.portfolio:
            self.portfolio[name] = quantity
        else:
            self.portfolio[name] += quantity
            
    def sell_stock(self, name, quantity):
        if name not in self.portfolio:
            print('Stock not in profolio')
            return
        elif self.portfolio[name] < quantity:
            print("Insufficient quantity of stock")
            return
        else:
            self.portfolio[name] -= quantity
            return