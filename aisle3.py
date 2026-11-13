from kitchen import kitchenItems
from banana import kitchenmore

def aisle3():
    print(f"Hello, This is aisle no:3 (for Kitchen Items)")
    print(f"We have: ")
    print("         Stoves")
    print("         Dishwashers")
    print("         Hotpots")
    print("         Fridges")
    print("         Dinner Sets")
    print("         Glasses")
    want = input(f"Do you want to buy kitchen items: (yes/no) ")
    if want == "yes":
        return kitchenItems() + kitchenmore()
    elif want == "no":
        print("Goodbye")
        return 0
    else:
        print("Please enter yes or no.")