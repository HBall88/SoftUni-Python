age=int(input())
washing_machine_price=float(input())
toy_price=int(input())
toy_saved=0
count_toy_years=0
money_earned=0
money_saved=0
leftover=0
counter=0
for i in range(1, age+1, 2):
    count_toy_years+=1
toy_saved=count_toy_years*toy_price
for j in range(2, age+1, 2):
    counter+=1
    if counter==1:
        money_earned=10
    elif counter>1:
        money_earned+=10+(counter-1)*10
money_saved=toy_saved+money_earned-counter
if money_saved>=washing_machine_price:
    leftover=abs(money_saved-washing_machine_price)
    print(f'Yes! {format(leftover, ".2f")}')
elif money_saved<washing_machine_price:
    leftover=abs(money_saved-washing_machine_price)
    print(f'No! {format(leftover, ".2f")}')