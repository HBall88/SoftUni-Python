import math

x=int(input())
y=float(input())
z=int(input())
r=int(input())
litri=(0.4*(x*y))/2.5
if litri<z:
    o=z-litri
    print(f'It will be a tough winter! More {math.floor(o)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(litri)} liters.')
    raz=litri-z
    chov=raz/r
    print(f'{math.ceil(raz)} liters left -> {math.ceil(chov)} liters per person.')