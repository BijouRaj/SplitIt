# Bill class
class Bill:
    def __init__(self, overall, subtotal, tax, tip):
        self.overall = overall
        self.subtotal = subtotal
        self.tax = tax
        self.tip = tip 
        self.tipCost = self.subtotal * self.tip 