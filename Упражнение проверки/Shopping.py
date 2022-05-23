budget=float(input())
GPUs=int(input())
CPUs=int(input())
RAMs=int(input())
GPUsPrice=GPUs*250
CPUsPrice=0.35*GPUsPrice*CPUs
RAMsPrice=0.10*GPUsPrice*RAMs
totprice=GPUsPrice+CPUsPrice+RAMsPrice
if GPUs>CPUs:
    totprice1=totprice-0.15*totprice
    if totprice1<=budget:
        h=budget-totprice1
        print(f'You have {format(h, ".2f")} leva left!')
    if totprice1>budget:
        h=totprice1-budget
        print(f'Not enough money! You need {format(h,".2f")} leva more!')
else:
    if totprice<=budget:
        h=budget-totprice
        print(f'You have {format(h, ".2f")} leva left!')
    if totprice>budget:
        h=totprice-budget
        print(f'Not enough money! You need {format(h,".2f")} leva more!')