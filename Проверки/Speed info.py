s=float(input())
if s<=10:
    print("slow")
elif 10<s<=50:
    print("average")
elif 50<s<=150:
    print("fast")
elif 150<s<=1000:
    print("ultra fast")
else:
    print("extremely fast")