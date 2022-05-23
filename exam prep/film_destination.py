film_budget=float(input())
destination=str(input())
season=str(input())
days_count=int(input())
one_day_price=0
if season=="Winter":
    if destination=="Dubai":
        one_day_price=0.7*45000
    elif destination=="Sofia":
        one_day_price=1.25*17000
    elif destination=="London":
        one_day_price=24000
elif season=="Summer":
    if destination=="Dubai":
        one_day_price=0.7*40000
    elif destination=="Sofia":
        one_day_price=1.25*12500
    elif destination=="London":
        one_day_price=20250
price=one_day_price*days_count
diff=film_budget-price
if diff>=0:
    print(f'The budget for the movie is enough! We have {format(diff, ".2f")} leva left!')
else:
    print(f'The director needs {format(abs(diff), ".2f")} leva more!')