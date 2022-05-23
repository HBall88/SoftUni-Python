n=int(input())
even=0
odd=0
for i in range(0, n):
    number=int(input())
    if i%2!=0:
        odd+=number
    else:
        even+=number
if even==odd:
    print(f'Yes')
    print(f'Sum = {even}')
else:
    tot=abs(even-odd)
    print(f'No')
    print(f'Diff = {tot}')