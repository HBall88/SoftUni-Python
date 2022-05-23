V=int(input())
P1=int(input())
P2=int(input())
H=float(input())
Sum=P1*H+P2*H
P1Percentage=(P1*H/Sum)*100
P2Percentage=(P2*H/Sum)*100
Summ=Sum/V*100
if Summ<=100:
    print(f'The pool is {format(Summ, ".2f")}% full. Pipe 1: {format(P1Percentage, ".2f")}%. Pipe 2: {format(P2Percentage, ".2f")}%.')
else:
    Over=(Summ-100)/100*V
    print(f'For {format(H, ".2f")} hours the pool overflows with {format(Over,".2f")} liters.')