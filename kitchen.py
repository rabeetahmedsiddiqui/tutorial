def dinnerSet():
    dinnerSetPrice = 95000
    dinnerSetQuantity = 20
    dinnerSetTotal = 0
    dinnerSetReq= int(input(f"There are {dinnerSetQuantity} peices of dinner Set, each dozen cost {dinnerSetPrice} pkr. How much do you want: "))
    dinnerSetQuantity = dinnerSetQuantity - dinnerSetReq
    dinnerSetTotal = dinnerSetPrice * dinnerSetReq
    if dinnerSetReq > dinnerSetQuantity :
        print("There are not enough pieces of dinner sets")
        return 0
    else:
        print(f"Thanks for buying. You total price of dinner sets are {dinnerSetTotal}")
    return dinnerSetTotal

def glass():
    glassPrice = 1200
    glassQuantity = 30
    glassTotal = 0
    glassReq= int(input(f"There are {glassQuantity} pieces of glass, each piece cost {glassPrice} pkr. How much do you want: "))
    glassQuantity = glassQuantity - glassReq
    glassTotal = glassPrice * glassReq
    if glassReq > glassQuantity :
        print("There are not enough pieces of glass")
        return 0
    else:
        print(f"Thanks for buying. You total price of glass are {glassTotal}")
    return glassTotal

def stove():
    stovePrice = 25000
    stoveQuantity = 15
    stoveTotal = 0
    stoveReq = int(input(f"There are {stoveQuantity} pieces of stove, each piece cost {stovePrice} pkr. How much do you want: "))
    stoveQuantity = stoveQuantity - stoveReq
    stoveTotal = stovePrice * stoveReq
    if stoveReq > stoveQuantity :
        print("There are not enough pieces of stoves")
        return 0
    else:
        print(f"Thanks for buying. You total price of stoves are {stoveTotal}")
    return stoveTotal

def dishwasher():
    dishwasherPrice = 300
    dishwasherQuantity = 100
    dishwasherTotal = 0
    dishwasherReq = int(input(f"There are {dishwasherQuantity} pieces of dishwasher, each piece cost {dishwasherPrice} pkr. How much do you want: "))
    dishwasherQuantity = dishwasherQuantity - dishwasherReq
    dishwasherTotal = dishwasherPrice * dishwasherReq
    if dishwasherReq > dishwasherQuantity :
        print("There are not enough pieces of dishwashers")
        return 0
    else:
        print(f"Thanks for buying. You total price of dishwashers are {dishwasherTotal}")
    return dishwasherTotal

def hotpot():
    hotpotPrice = 999
    hotpotQuantity = 20
    hotpotTotal = 0
    hotpotReq = int(input(f"There are {hotpotQuantity} pieces of hotpot, each piece cost {hotpotPrice} pkr. How much do you want: "))
    hotpotQuantity = hotpotQuantity - hotpotReq
    hotpotTotal = hotpotPrice * hotpotReq
    if hotpotReq > hotpotQuantity :
        print("There are not enough pieces of hotpots")
        return 0
    else:
        print(f"Thanks for buying. You total price of hotpots are {hotpotTotal}")
        return hotpotTotal


def fridge():
    fridgePrice = 210000
    fridgeQuantity = 50
    fridgeTotal = 0
    fridgeReq= int(input(f"There are {fridgeQuantity} kilograms of fridge, each kilos cost {fridgePrice} pkr. How much do you want: "))
    fridgeQuantity = fridgeQuantity - fridgeReq
    fridgeTotal = fridgePrice * fridgeReq
    if fridgeReq > fridgeQuantity :
        print("There are not enough kilos of fridges")
        return 0
    else:
        print(f"Thanks for buying. You total price of fridges are {fridgeTotal}")
    return fridgeTotal

def kitchenItems():
    buyItem = input("Which item do you want to buy? ")
    if buyItem == "stove":
        return stove()
    elif buyItem == "dish washer":
        return dishwasher()
    elif buyItem == "hotpot":
        return hotpot()
    elif buyItem == "fridge":
        return fridge()
    elif buyItem == "dinner set":
        return dinnerSet()
    elif buyItem == "glass":
        return glass()
    else:
        print(f"We have no item that name is {buyItem}. retry. ")
        return kitchenItems()

def kitchenmore():
    morekitchen = input("Do you want to buy more items? (yes/no): ")
    if morekitchen == "yes":
        return kitchenItems() + kitchenmore()
    elif morekitchen == "no":
        print("Goodbye")
        return 0
    else:
        print(f"Please enter yes or no.")
        return kitchenmore()

def kitchenTotal():
    stoveTotal = stove()
    dishwasherTotal = dishwasher()
    hotpotTotal = hotpot()
    fridgeTotal = fridge()
    dinnerSetTotal = dinnerSet()
    glassTotal = glass()
    kitchenGrandTotal = stoveTotal + dishwasherTotal + hotpotTotal + fridgeTotal + dinnerSetTotal + glassTotal 
    return kitchenGrandTotal