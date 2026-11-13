from aisle1 import aisle1
from banana import fruitTotal
from banana import more
from aisle2 import aisle2
from restroom import restroomTotal
from aisle3 import aisle3
from kitchen import kitchenTotal

def main():
    whichAisle = input("Which Aisle? ")
    if whichAisle == "aisle 1":
        fruitGrandTotal = aisle1()
        print(f"Your grand total from Aisle No:1 is {fruitGrandTotal}")
        return fruitGrandTotal, main()
    elif whichAisle == "aisle 2":
        restroomGrandtotal = aisle2()
        print(f"Your grand total from Aisle No:2 is {restroomGrandtotal}")
        return restroomGrandtotal, main()
    elif whichAisle == "aisle 3":
        kitchenGrandtotal = aisle3()
        print(f"Your grand total from Aisle No:3 is {kitchenGrandtotal}")
        return kitchenGrandtotal, main()
    else:
        print("Sorry that aisle don't exist!.")

def mainMore():
    more= input(f"do you want to continue shopping? (yes/no) ")
    if more == "yes":
        main()
    else:
        print("Thank you for shopping with us!")

print(f"Hello and welcome to RAS Store")
main()
mainMore()