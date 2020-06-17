class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        cost = self.shares * self.price
        return cost

    def sell(self, shares_sold):
        self.shares = self.shares - shares_sold

