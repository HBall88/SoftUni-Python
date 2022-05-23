number_of_orders=int(input())
sum_money=0
for _ in range(number_of_orders):
    price_per_order=0
    price_per_capsule=float(input())
    days=int(input())
    capsules_per_day=int(input())
    if 0.01>price_per_capsule or price_per_capsule>100 or days<1 or days>31 or capsules_per_day<1 or capsules_per_day>2000:
        continue
    else:
        price_per_order=days*capsules_per_day*price_per_capsule
        sum_money+=price_per_order
        print(f'The price for the coffee is: ${price_per_order:.2f}')
print(f'Total: ${sum_money:.2f}')