import sys
weight_max=0
time_max=0
quality_max=0
number_of_snowballs=int(input())
max_value=-sys.maxsize
for _ in range(number_of_snowballs):
    weight=int(input())
    time_needed=int(input())
    quality=int(input())
    value=(weight/time_needed)**quality
    if value>max_value:
        max_value=value
        weight_max=weight
        time_max=time_needed
        quality_max=quality
print(f'{weight_max} : {time_max} = {int(max_value)} ({quality_max})')