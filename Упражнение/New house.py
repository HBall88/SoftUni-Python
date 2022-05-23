type_of_flower=str(input())
flowers_count=int(input())
budget=int(input())
final_price=0
if type_of_flower=="Roses" and flowers_count>80:
    final_price=5*flowers_count*0.9
elif type_of_flower=="Dahlias" and flowers_count>90:
    final_price=3.80*flowers_count*0.85
elif type_of_flower=="Tulips" and flowers_count>80:
    final_price=2.80*flowers_count*0.85
elif type_of_flower=="Narcissus" and flowers_count<120:
    final_price=3.00*flowers_count*1.15
elif type_of_flower=="Gladiolus" and flowers_count<80:
    final_price=2.50*flowers_count*1.20
else:
    if type_of_flower=="Roses":
        final_price=flowers_count*5
    if type_of_flower=="Dahlias":
        final_price=flowers_count*3.80
    if type_of_flower=="Tulips":
        final_price=flowers_count*2.80
    if type_of_flower=="Narcissus":
        final_price=flowers_count*3.00
    if type_of_flower=="Gladiolus":
        final_price=flowers_count*2.50
if final_price<=budget:
    remaining=budget-final_price
    print(f'Hey, you have a great garden with {flowers_count} {type_of_flower} and {format(remaining, ".2f")} leva left.')
if final_price>budget:
    remaining=final_price-budget
    print(f'Not enough money, you need {format(remaining, ".2f")} leva more.')