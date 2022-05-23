money_available=float(input())
gender=str(input())
age=int(input())
sport=str(input())
money_needed=0
if age<=19:
    if gender=="m":
        if sport=="Gym":
            money_needed=0.8*42
        elif sport=="Boxing":
            money_needed=0.8*41
        elif sport=="Yoga":
            money_needed=0.8*45
        elif sport=="Zumba":
            money_needed=0.8*34
        elif sport=="Dances":
            money_needed=0.8*51
        elif sport=="Pilates":
            money_needed=0.8*39
    elif gender=="f":
        if sport=="Gym":
            money_needed=0.8*35
        elif sport=="Boxing":
            money_needed=0.8*37
        elif sport=="Yoga":
            money_needed=0.8*42
        elif sport=="Zumba":
            money_needed=0.8*31
        elif sport=="Dances":
            money_needed=0.8*53
        elif sport=="Pilates":
            money_needed=0.8*37
else:
    if gender=="m":
        if sport=="Gym":
            money_needed=42
        elif sport=="Boxing":
            money_needed=41
        elif sport=="Yoga":
            money_needed=45
        elif sport=="Zumba":
            money_needed=34
        elif sport=="Dances":
            money_needed=51
        elif sport=="Pilates":
            money_needed=39
    elif gender=="f":
        if sport=="Gym":
            money_needed=35
        elif sport=="Boxing":
            money_needed=37
        elif sport=="Yoga":
            money_needed=42
        elif sport=="Zumba":
            money_needed=31
        elif sport=="Dances":
            money_needed=53
        elif sport=="Pilates":
            money_needed=37
if money_needed<=money_available:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    difference=money_needed-money_available
    print(f"You don't have enough money! You need ${difference:.2f} more.")