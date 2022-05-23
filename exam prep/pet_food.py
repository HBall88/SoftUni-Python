days=1
days_count=int(input())
total_food=float(input())
counter_days_for_biscuits=0
biscuits_counter=0
biscuits_total=0
food_sum_global=0
dog_food_global=0
cat_food_global=0
for days in range(1, days_count+1):
    the_food_the_dog_ate=int(input())
    the_food_the_cat_ate=int(input())
    dog_food_global+=the_food_the_dog_ate
    cat_food_global+=the_food_the_cat_ate
    food_sum_for_the_day=the_food_the_dog_ate+the_food_the_cat_ate
    food_sum_global+=the_food_the_dog_ate+the_food_the_cat_ate
    if days%3==0:
        biscuits_counter+=1
        biscuits_total+=0.1*food_sum_for_the_day
print(f"Total eaten biscuits: {round(biscuits_total)}gr.")
eaten_food_percentage=food_sum_global/total_food*100
print(f"{eaten_food_percentage:.2f}% of the food has been eaten.")
dog_food_percentage=dog_food_global/food_sum_global*100
print(f"{dog_food_percentage:.2f}% eaten from the dog.")
cat_food_percentage=cat_food_global/food_sum_global*100
print(f"{cat_food_percentage:.2f}% eaten from the cat.")