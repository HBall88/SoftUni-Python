number=int(input())
first_number=number%10
second_number=number//10%10
third_number=number//100%10
for i in range(1, first_number+1):
    first_number_current=i
    for j in range(1, second_number+1):
        second_number_current=j
        for z in range(1, third_number+1):
            third_number_current=z
            result_current=first_number_current*second_number_current*third_number_current
            print(f"{first_number_current} * {second_number_current} * {third_number_current} = {result_current};")
