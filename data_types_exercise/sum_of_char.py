n=int(input())
total_sum=0
for _ in range(n):
    character=str(input())
    total_sum+=ord(character)
print(f'The sum equals: {total_sum}')