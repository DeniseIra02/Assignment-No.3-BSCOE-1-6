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