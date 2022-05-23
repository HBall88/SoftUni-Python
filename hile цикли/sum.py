i=int(input())
sum_numbers=0
if sum_numbers >= i:
    print(sum_numbers)
while sum_numbers<i:
    number=int(input())
    sum_numbers+=number
    if sum_numbers>=i:
        print(sum_numbers)
        break