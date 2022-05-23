n=int(input())
sum_numbers=0
counter=0
for x1 in range(0, n+1):
    for x2 in range(0, n+1):
        for x3 in range(0, n+1):
            sum_numbers=x1+x2+x3
            if sum_numbers==n:
                counter+=1
print(counter)