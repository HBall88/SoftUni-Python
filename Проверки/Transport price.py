n=int(input())
dn=str(input())
if dn=="day":
    taksi=0.79*n+0.70
if dn=="night":
    taksi=0.90*n+0.70
bus=0.09*n
vlak=0.06*n
if n<20:
    print(format(taksi, ".2f"))
if 20<=n<100:
    optimal=min(taksi, bus)
    optimalf=format(optimal, ".2f")
    print(optimalf)
if 100<=n:
    optimal=min(taksi, bus, vlak)
    optimalf=format(optimal, ".2f")
    print(optimalf)