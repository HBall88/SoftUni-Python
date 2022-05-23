over_20kg_luggage_price=float(input())
kg_luggage=float(input())
days_travelling=int(input())
count_of_luggage=int(input())
price1=0
price2=0
price_final=0
if kg_luggage<10:
    price1=0.2*over_20kg_luggage_price
if 10<=kg_luggage<=20:
    price1=0.5*over_20kg_luggage_price
if kg_luggage>20:
    price1=over_20kg_luggage_price
if days_travelling>30:
    price2=price1*1.1
if 7<=days_travelling<=30:
    price2=price1*1.15
if 7>days_travelling:
    price2=price1*1.4
price_final=count_of_luggage*price2
print(f'The total price of bags is: {format(price_final, ".2f")} lv.')