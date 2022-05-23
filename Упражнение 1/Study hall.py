w=float(input())
h=float(input())-1
wworkscount=w//1.20
hworkscount=h//0.7
count=wworkscount*hworkscount-3
countdone="{:.0f}".format(count)
print(countdone)