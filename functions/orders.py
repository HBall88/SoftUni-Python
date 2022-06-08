product = input()
quantity = int(input())
def cashier(product, quantity):
    result = 0
    if product == "coffee":
        result = quantity * 1.50
    elif product == "coke":
        result = quantity * 1.40
    elif product == "water":
        result = quantity * 1.00
    elif product == "snacks":
        result = quantity * 2.00
    print("{:.2f}".format(result))



cashier(product, quantity)