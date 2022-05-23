budget=float(input())
category=str(input())
people=int(input())
money_needed=0
travel_price=0
all_money=0
remaining_money=0
if category=="VIP":
    money_needed=people*499.99
if category=="Normal":
    money_needed=people*249.99
if 1<=people<=4:
    travel_price=0.75*budget
if 5<=people<=9:
    travel_price=0.6*budget
elif 10<=people<=24:
    travel_price=0.5*budget
elif 25<=people<=49:
    travel_price=0.4*budget
elif people>50:
    travel_price=0.25*budget
all_money=money_needed+travel_price
if all_money<budget:
    remaining_money=budget-all_money
    print(f'Yes! You have {format(remaining_money, ".2f")} leva left.')
if all_money>budget:
    remaining_money=all_money-budget
    print(f'Not enough money! You need {format(remaining_money, ".2f")} leva.')