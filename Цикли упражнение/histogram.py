n=int(input())
n1=0
n2=0
n3=0
n4=0
n5=0
for i in range(0, n):
    num=int(input())
    if num<200:
        n1+=1
    elif 200<=num<=399:
        n2+=1
    elif 400<=num<=599:
        n3+=1
    elif 600<=num<=799:
        n4+=1
    elif 800<=num:
        n5+=1
p1=format(n1/n*100, ".2f")
p2=format(n2/n*100, ".2f")
p3=format(n3/n*100, ".2f")
p4=format(n4/n*100, ".2f")
p5=format(n5/n*100, ".2f")
print(p1+"%")
print(p2+"%")
print(p3+"%")
print(p4+"%")
print(p5+"%")