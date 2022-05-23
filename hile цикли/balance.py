inpt=input()
balance=0.0
i=0
x=0
while inpt!="NoMoreMoney":
    i=float(inpt)
    if i<0:
        x+=1
        print(f'Invalid operation!')
        print(f'Total: {format(balance, ".2f")}')
        break
    balance+=i
    print(f'Increase: {format(i, ".2f")}')
    inpt= input()
if x==0:
    print(f'Total: {format(balance, ".2f")}')