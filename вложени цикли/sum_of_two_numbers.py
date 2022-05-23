beg=int(input())
end=int(input())
number=int(input())
sum_i_j=0
position_counter=0
is_true=False
for i in range(beg, end+1):
    for j in range(beg, end+1):
        position_counter+=1
        sum_i_j=i+j
        if sum_i_j==number:
            is_true=True
            print(f'Combination N:{position_counter} ({i} + {j} = {i+j})')
            break
    if is_true==True:
        break
if is_true==False:
    print(f"{position_counter} combinations - neither equals {number}")