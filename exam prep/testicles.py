import math
count_of_balls=int(input())
sum_points=0
sum_points1=0
red_balls=0
orange_balls=0
yellow_balls=0
white_balls=0
black_balls=0
other_colored_balls=0
for i in range(0, count_of_balls):
    color=str(input())
    if color=="red":
        sum_points+=5
        red_balls+=1
    if color=="orange":
        sum_points+=10
        orange_balls+=1
    if color=="yellow":
        sum_points+=15
        yellow_balls+=1
    if color=="white":
        sum_points+=20
        white_balls+=1
    if color=="black":
        sum_points1=math.floor(sum_points/2)
        black_balls+=1
        sum_points=sum_points1
    if color!="red" and color!="orange" and color!="yellow" and color!="white" and color!="black":
        other_colored_balls+=1
print(f'Total points: {sum_points}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_colored_balls}')
print(f'Divides from black balls: {black_balls}')