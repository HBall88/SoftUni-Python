lost_fights=int(input())
helmet_price=float(input())
sword_price=float(input())
shield_price=float(input())
armor_price=float(input())
price_to_pay=0
shield_counter=0
for game in range(1, lost_fights+1):
    if game%2==0:
        price_to_pay+=helmet_price
    if game%3==0:
        price_to_pay+=sword_price
    if game%2==0 and game%3==0:
        price_to_pay+=shield_price
        shield_counter+=1
        if shield_counter%2==0:
            price_to_pay+=armor_price
print(f'Gladiator expenses: {price_to_pay:.2f} aureus')