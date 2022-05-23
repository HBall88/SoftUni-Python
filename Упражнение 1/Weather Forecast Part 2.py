d=float(input())
if 26.0<=d<=35.00:
    print("Hot")
elif 20.1<=d<=25.9:
    print("Warm")
elif 15.00<=d<=20.00:
    print("Mild")
elif 12.00<=d<=14.9:
    print("Cool")
elif 5.00<=d<=11.9:
    print("Cold")
else:
    print("unknown")