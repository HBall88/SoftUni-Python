month=str(input())
nights_spent=int(input())
if month=="May" or month=="October":
    studio=50*nights_spent
    if nights_spent>14:
        studio1=0.7*studio
    elif nights_spent>7:
        studio1=0.95*studio
    else:
        studio1=studio
    Apartment=65*nights_spent
    if nights_spent>14:
        Apartment1=0.9*Apartment
    else:
        Apartment1=Apartment
    print(f'Apartment: {format(Apartment1, ".2f")} lv.')
    print(f'Studio: {format(studio1, ".2f")} lv.')
if month=="June" or month=="September":
    studio=75.20*nights_spent
    if nights_spent>14:
        studio1=0.8*studio
    else:
        studio1=studio
    Apartment=68.70*nights_spent
    if nights_spent>14:
        Apartment1=0.9*Apartment
    else:
        Apartment1=Apartment
    print(f'Apartment: {format(Apartment1, ".2f")} lv.')
    print(f'Studio: {format(studio1, ".2f")} lv.')
if month=="July" or month=="August":
    studio=76*nights_spent
    studio1=studio
    Apartment=77*nights_spent
    if nights_spent>14:
        Apartment1=0.9*Apartment
    else:
        Apartment1=Apartment
    print(f'Apartment: {format(Apartment1, ".2f")} lv.')
    print(f'Studio: {format(studio1, ".2f")} lv.')