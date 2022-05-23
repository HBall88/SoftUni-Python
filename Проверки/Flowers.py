import math

mangolii=int(input())
zumbuli=int(input())
rozi=int(input())
kaktusi=int(input())
cena_podaruk=float(input())
m=mangolii*3.25
z=zumbuli*4.00
r=rozi*3.50
k=kaktusi*8.00
s=m+z+r+k
sgot=s-0.05*s
if sgot>=cena_podaruk:
    leftovers=sgot-cena_podaruk
    print(f'She is left with {math.floor(leftovers)} leva.')
else:
    borrow=cena_podaruk-sgot
    print(f'She will have to borrow {math.ceil(borrow)} leva.')