budget = int(input())
prices_products = input()
while True:
    if prices_products == "End":
        break
    else:
        prices_products = int(prices_products)
    budget -= prices_products
    if (budget < 0):
        print("You went in overdraft!")
        break
    prices_products = input()
if budget >= 0:
    print(f'You bought everything needed.')
