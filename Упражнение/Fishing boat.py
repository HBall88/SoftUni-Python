budget=int(input())
season=str(input())
fishermen_count=int(input())
rent=0
rent_final=0
rent_final1=0
if season=="Spring":
    rent=3000
    if fishermen_count<=6:
        rent_final=rent*0.90
    if 7<=fishermen_count<=11:
        rent_final=rent*0.85
    if fishermen_count>=12:
        rent_final=rent*0.75
    if fishermen_count%2==0:
        rent_final1=rent_final*0.95
if season=="Summer":
    rent=4200
    if fishermen_count<=6:
        rent_final=rent*0.90
    if 7<=fishermen_count<=11:
        rent_final=rent*0.85
    if fishermen_count>=12:
        rent_final=rent*0.75
    if fishermen_count%2==0:
        rent_final1=rent_final*0.95
if season=="Autumn":
    rent=4200
    if fishermen_count<=6:
        rent_final=rent*0.90
    if 7<=fishermen_count<=11:
        rent_final=rent*0.85
    if fishermen_count>=12:
        rent_final=rent*0.75
if season=="Winter":
    rent=2600
    if fishermen_count<=6:
        rent_final=rent*0.90
    if 7<=fishermen_count<=11:
        rent_final=rent*0.85
    if fishermen_count>=12:
        rent_final=rent*0.75
    if fishermen_count%2==0:
        rent_final1=rent_final*0.95
if rent_final1==0:
    if rent_final<=budget:
        revenue=budget-rent_final
        print(f'Yes! You have {format(revenue, ".2f")} leva left.')
    if rent_final>budget:
        revenue=rent_final-budget
        print(f'Not enough money! You need {format(revenue, ".2f")} leva.')
if rent_final1>0:
    if rent_final1<=budget:
        revenue=budget-rent_final1
        print(f'Yes! You have {format(revenue, ".2f")} leva left.')
    if rent_final1>budget:
        revenue=rent_final1-budget
        print(f'Not enough money! You need {format(revenue, ".2f")} leva.')