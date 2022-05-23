fruit=str(input())
size=str(input())
count=int(input())
price1=0
if fruit=="Watermelon":
    if size=="small":
       price1=2*56
    elif size=="big":
        price1=5*28.70
elif fruit == "Mango":
    if size == "small":
        price1 = 2 * 36.66
    elif size == "big":
        price1 = 5 * 19.60
elif fruit == "Pineapple":
    if size == "small":
        price1 = 2 * 42.10
    elif size == "big":
        price1 = 5 * 24.80
elif fruit == "Raspberry":
    if size == "small":
        price1 = 2 * 20
    elif size == "big":
        price1 = 5 * 15.20
price2=count*price1
price3=0
if 400<price2<=1000:
    price3=0.85*price2
elif price2>1000:
    price3=0.5*price2
else:
    price3=price2
print(f'{price3:.2f} lv.')


