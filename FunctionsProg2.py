def getApl():
    _apl = int(input("How many apple do you want to buy? \n> "))
    return _apl

def getOrng():
    _orng = int(input("How many orange do you want to buy? \n> "))
    return _orng

def getAplPrice():
    _aplPrice = 20 
    return _aplPrice

def getOrngPrice():
    _orngPrice = 25 
    return _orngPrice

def getAplTotal():
    _appleTotal = quantapl * aplPrice
    return _appleTotal

def getOrngTotal():
    _orangeTotal = quantorng * orngPrice
    return _orangeTotal

def getOverallTtl():
    overallTtl = appleTotal + orangeTotal
    return overallTtl

def display(totalF):
    print(f"The total amount is {totalF} pesos.")

quantapl= getApl()
quantorng = getOrng()
aplPrice = getAplPrice()
orngPrice = getOrngPrice()
appleTotal = getAplTotal()
orangeTotal = getOrngTotal()
total = getOverallTtl()
display(total)