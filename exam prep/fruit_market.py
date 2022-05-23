strawberries_price=float(input())
bananas_count=float(input())
oranges_count=float(input())
malini_count=float(input())
strawberries_count=float(input())
malini_price=1/2*strawberries_price
oranges_price=0.6*malini_price
bananas_price=0.2*malini_price
price=format(strawberries_count*strawberries_price+malini_count*malini_price+oranges_count*oranges_price+bananas_price*bananas_count, ".2f")
print(price)