budget_available=float(input())
nights_spent=int(input())
price_per_night=float(input())
if nights_spent>7:
    price_per_night=0.95*price_per_night
additional_shit_percent=int(input())/100
cost1=nights_spent*price_per_night
cost2=cost1+additional_shit_percent*budget_available
diff=budget_available-cost2
if diff>=0:
    print(f'Ivanovi will be left with {format(diff, ".2f")} leva after vacation.')
else:
    print(f'{format(abs(diff), ".2f")} leva needed.')