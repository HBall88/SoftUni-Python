import math
brdni=int(input())
hrana=int(input())
kuche=float(input())
kotka=float(input())
kostenurka=float(input())/1000
ob=kuche*brdni+kotka*brdni+kostenurka*brdni
if ob<=hrana:
    v=hrana-ob
    print(f'{math.floor(v)} kilos of food left.')
else:
    v=ob-hrana
    print(f'{math.ceil(v)} more kilos of food are needed.')