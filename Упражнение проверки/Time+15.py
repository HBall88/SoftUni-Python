hour=int(input())
min=int(input())
min+=15
hour+=min//60
min%=60
if hour>23:
    hour=0
print(f'{hour}:{min:02d}')