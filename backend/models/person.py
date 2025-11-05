# Person class
class Person:
    def __init__(self, name, bill):
        self.name = name 
        self.bill = 0
        self.order = {}
        self.totalBill = bill.subtotal
        self.tax = bill.tax
        self.tip = bill.tipCost
        
    def addItem(self, item):
        self.bill += item.price 
        self.order[item.name] = item.price
        
    def deleteItem(self, item):
        del self.order[item.name]
        self.bill -= item.price
        
    def myPart(self):
        self.part = self.bill / self.totalBill
    
    def totalIt(self):
        taxPart = self.part * self.tax 
        tipPart = self.part * self.tip 
        self.myTotal = round(self.bill + taxPart + tipPart, 2)
        
    def final(self):
        self.myPart()
        self.totalIt()
        return {
            "name": self.name,
            "items": [{"name": i, "price": self.order[i]} for i in self.order],
            "total": self.myTotal 
        }