destination=str(input())
while destination !="End":
    price_trip=float(input())
    sum_money = 0
    while sum_money<price_trip:
        saved_money=float(input())
        sum_money+=saved_money
    print(f'Going to {destination}!')
    destination=input()