fruit=str(input())
weekday=str(input())
quantity=float(input())
price=0
result=0
if weekday=="Monday" or weekday=="Tuesday" or weekday=="Wednesday" or weekday=="Thursday" or weekday=="Friday":
    if fruit=="banana":
        price=2.50
    elif fruit=="apple":
        price=1.20
    elif fruit=="orange":
        price=0.85
    elif fruit=="grapefruit":
        price=1.45
    elif fruit=="kiwi":
        price=2.70
    elif fruit=="pineapple":
        price=5.50
    elif fruit=="grapes":
        price=3.85
elif weekday=="Saturday" or weekday=="Sunday":
    if fruit=="banana":
        price=2.70
    elif fruit=="apple":
        price=1.25
    elif fruit=="orange":
        price=0.90
    elif fruit=="grapefruit":
        price=1.60
    elif fruit=="kiwi":
        price=3.00
    elif fruit=="pineapple":
        price=5.60
    elif fruit=="grapes":
        price=4.20
if price>0:
    result=price*quantity
    print(format(result, ".2f"))
else:
    print("error")