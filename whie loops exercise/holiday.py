money_needed_for_the_excursion=float(input())
available_money=float(input())
days_counter=0
spending_counter=0
while available_money<money_needed_for_the_excursion and spending_counter<5:
    command=str(input())
    money=float(input())
    days_counter+=1
    if command=='save':
        available_money+=money
        spending_counter=0
    elif command=="spend":
        available_money-=money
        spending_counter+=1
        if available_money<0:
            available_money=0
if spending_counter==5:
    print(f"You can't save the money.")
    print(days_counter)
if available_money>=money_needed_for_the_excursion:
    print(f'You saved the money for {days_counter} days.')
