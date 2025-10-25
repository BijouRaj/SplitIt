
# whoever is paying the bill takes a picture of the receipt, decide on tip amount

# parse receipt for information, assign each item to each person

# each individual person gets the price of their item added to their bill

# calculate tip/tax and add to individual bills (based on percentage of subtotal)

# send out bills through venmo - to be done when integrated with FastAPI

# cool frontend


# Bill class
class Bill:
    def __init__(self, subtotal, tax, tip):
        self.subtotal = subtotal
        self.tax = tax
        self.tip = tip 
        


# Item class
class Item:
    def __init__(self, name, price):
        self.name = name 
        self.price = price 
    # def assign(self, name):
    #     self.person = name
        

# Person class
class Person:
    def __init__(self, name, totalBill):
        self.name = name 
        self.bill = 0
        self.order = {}
        self.totalBill = totalBill
        
    # def addItem(self, item, cost):
    #     self.bill += int(cost) 
    #     self.order[item] = cost
    def addItem(self, item):
        self.bill += item.price 
        self.order[item.name] = item.price
        
    def deleteItem(self, item):
        del self.order[item.name]
        self.bill -= item.price
        
    def myPart(self):
        #self.percentage = self.bill / self.totalBill 
        return self.bill / self.totalBill
        
p = Person("Bob", 100)
fish = Item("fish", 10)
chicken = Item("chicken", 20)
p.addItem(fish)
p.addItem(chicken)
p.deleteItem(chicken)
print(p.name)
print(p.bill)
print(p.totalBill)
print(p.order)
print(p.myPart())
        
# Receipt class
class Receipt:
    def __init__(self):
        self.order = []
        self.guests = {}
        
    def parse(self, receipt):
        for item in receipt:
            self.order.append(item)
            
    def findPeople(self):
        num = input("How many guests?" )
    




def calculateTip(total, percent):
    return total * percent 

def split(total, percentage):
    return total * percentage 

def findPercentage(total, items):
    individualCost = 0
    for item in items:
        individualCost += item 


"""
people = input("How many people in your party? ")
val = 1
ppl = []
for i in range(int(people)):
    person = Person("John")
    ppl.append(person) 
print(ppl)

"""

# go through each item in receipt, assign to person

"""
receipt = {"Fish": "30", "Chicken": "15", "Water": "20"}

guests = {"Bob", "Dana", "Kim"}

people = {}

for guest in guests:
    people[guest] = Person(guest)
    
allItems = []
    
for item, price in receipt.items():
    curr = Item(item, price)
    buy = input(f"Who ordered the {item}? " )
    people[buy].addTo(item, price)
    
for person in people.values():
    print(person.name)
    print(person.bill)
    print(person.order)
    
    
    curr.assign(buy)
    allItems.append(curr)
    
for item in allItems:
    print(item.name)
    print(item.person)
    
    """
