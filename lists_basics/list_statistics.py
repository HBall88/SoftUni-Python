positive_numbers_list=[]
negative_numbers_list=[]
sum_negatives=0
n=int(input())
for _ in range(n):
    number=int(input())
    if number>=0:
        positive_numbers_list.append(number)
    else:
        sum_negatives+=number
        negative_numbers_list.append(number)
positives_count = len(positive_numbers_list)
print(positive_numbers_list)
print(negative_numbers_list)
print(f'Count of positives: {positives_count}')
print(f'Sum of negatives: {sum_negatives}')