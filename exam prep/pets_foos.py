days_count=int(input())
food_in_the_beginning=float(input())
biscuit_counter=0
biscuit_quantity=0
dog_food_global=0
cat_food_global=0
all_food_global=0
for shit in range(1, days_count+1):
    dog_food_eaten=float(input())
    cat_food_eaten=float(input())
    dog_food_global+=dog_food_eaten
    cat_food_global+=cat_food_eaten
    all_food_eaten=dog_food_eaten+cat_food_eaten
    all_food_global+=all_food_eaten
    if shit%3==0:
        biscuit_counter+=1
        biscuit_quantity=0.1*all_food_eaten
print(f'Total eaten biscuits: {round(biscuit_quantity)}gr.')
all_food_percent=format(all_food_global/food_in_the_beginning*100, ".2f")
print(f'{all_food_percent}% of the food has been eaten.')
dog_percent= format(dog_food_global/all_food_global*100, ".2f")
print(f'{dog_percent}% eaten from the dog.')
cat_percent=format(cat_food_global/all_food_global*100, ".2f")
print(f'{cat_percent}% eaten from the cat.')
