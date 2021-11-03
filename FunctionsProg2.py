def getApl():
    _apl = int(input("How many apple do you want to buy? \n> "))
    return _apl

def getOrng():
    _orng = int(input("How many apple do you want to buy? \n> "))
    return _orng

def getPrice(apl_, orng_):
    aplPrice = apl_ * 20
    orngPrice = orng_ * 25
    overallPrice = aplPrice + orngPrice
    return overallPrice