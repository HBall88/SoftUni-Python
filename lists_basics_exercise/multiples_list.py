factor = int(input())
count_of_elements = int(input())
list_of_numbers = []
list_of_numbers.append(factor)
factor_new = factor
for i in range(count_of_elements-1):
    factor_new += factor
    list_of_numbers.append(factor_new)
print(list_of_numbers)