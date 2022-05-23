budget=float(input())
statists=int(input())
clothing=float(input())
dekor=0.10*budget
if statists>150:
    priceclothing=(statists*clothing)-0.10*(statists*clothing)
if statists<=150:
    priceclothing=statists*clothing
sum=priceclothing+dekor
if sum>budget:
    h=sum-budget
    print("Not enough money!")
    print(f'Wingard needs {format(h, ".2f")} leva more.')
if sum<=budget:
    h=budget-sum
    print("Action!")
    print(f'Wingard starts filming with {format(h, ".2f")} leva left.')