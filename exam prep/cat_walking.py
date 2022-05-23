minutes_walking_daily=int(input())
walkings_count=int(input())
calories_consumed_daily=int(input())
sum_minutes_walking=minutes_walking_daily*walkings_count
burned_calories=sum_minutes_walking*5
fifty_percent_of_consumed_calories=0.5*calories_consumed_daily
if burned_calories>=fifty_percent_of_consumed_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")