class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    def cost(self):
        cost = self.shares * self.price
        return cost

    def sell(self, shares_sold):
        self.shares = self.shares - shares_sold

