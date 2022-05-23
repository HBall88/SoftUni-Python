divisor=int(input())
boundary=int(input())
n=boundary
while True:
    if n%divisor==0:
        print(n)
        exit()
    else:
        n-=1
