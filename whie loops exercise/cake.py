len=int(input())
lon=int(input())
count_of_pieces=len*lon
diff=count_of_pieces
leftover=0
while diff>0:
    take=input()
    if take=="STOP":
        break
    else:
        take=int(take)
    diff-=take
    leftover=abs(diff)
if diff<0:
    print(f'No more cake left! You need {leftover} pieces more.')
else:
    print(f"{leftover} pieces are left.")