def getMoney():
    _money = int(input("How much is your money? \n> "))
    return _money

def getAplPrice():
    _aplPrice = int(input("How much is the price of apple per piece? \n> "))
    return _aplPrice

def getAplQuant():
    _aplQuant = money // aplPrice
    return _aplQuant

def getTotal():
    _total = aplQuant * aplPrice
    return _total

def getChange():
    _change = money - total
    return _change

def display(aplQuantF, changeF):
    print(f"You can buy {aplQuantF} apple/s and your change is {changeF} pesos.")

money = getMoney()
aplPrice = getAplPrice()
aplQuant = getAplQuant()
total = getTotal()
change = getChange()
display(aplQuant, change)