left_sum=0
right_sum=0
n=int(input())
for i in range(n*2):
    current_number=int(input())
    if i<n:
        left_sum+=current_number
    elif i>=n:
        right_sum+=current_number
if left_sum==right_sum:
    print(f'Yes, sum = {right_sum}')
if left_sum!=right_sum:
    difference=abs(left_sum-right_sum)
    print(f'No, diff = {difference}')
