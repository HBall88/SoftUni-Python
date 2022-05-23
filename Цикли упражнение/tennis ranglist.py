import math

tours_count=int(input())
starting_points=int(input())
sum_final=0
winner_counter=0
points_sum=0
for i in range(0, tours_count):
    state=str(input())
    if state=="W":
        points_sum+=2000
        winner_counter+=1
        if sum_final==0:
            sum_final+=starting_points+2000
        else:
            sum_final+=2000
    if state=="F":
        points_sum += 1200
        if sum_final==0:
            sum_final+=starting_points+1200
        else:
            sum_final+=1200
    if state=="SF":
        points_sum += 720
        if sum_final==0:
            sum_final+=starting_points+720
        else:
            sum_final+=720
average_points=points_sum/tours_count
print(f'Final points: {sum_final}')
print(f'Average points: {math.floor(average_points)}')
percentage=winner_counter/tours_count*100
print(format(percentage, ".2f")+"%")