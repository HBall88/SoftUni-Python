hour=int(input())
weekday=str(input())
if weekday=="Sunday":
    print("closed")
else:
    if 10<=hour<=18:
        print("open")
    else:
        print("closed")