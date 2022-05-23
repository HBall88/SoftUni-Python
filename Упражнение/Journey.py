budget=float(input())
season=str(input())
percentage=0
price=0
residence="a"
destination="a"
if budget<=100:
    destination="Bulgaria"
    if season=="summer":
        residence="Camp"
        percentage=0.3
        price=percentage*budget
    if season=="winter":
        residence="Hotel"
        percentage = 0.7
        price = percentage * budget
elif budget<=1000:
    destination="Balkans"
    if season=="summer":
        residence="Camp"
        percentage=0.4
        price=percentage*budget
    if season=="winter":
        residence="Hotel"
        percentage = 0.8
        price = percentage * budget
elif budget>1000:
    destination="Europe"
    residence="Hotel"
    percentage=0.9
    price=percentage*budget
print(f'Somewhere in {destination}')
print(f'{residence} - {format(price, ".2f")}')