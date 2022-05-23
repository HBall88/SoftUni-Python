i = float(input())
if i == 0:
    print("zero")

elif i > 0:
    if i < 1:
        small_large = "small"
        print(f"{small_large} positive")
    elif i > 1000000:
        small_large = "large"
        print(f"{small_large} positive")
    else:
        print("positive")

else:
    if abs(i) < 1:
        small_large = "small"
        print(f"{small_large} negative")
    elif abs(i) > 1000000:
        small_large = "large"
        print(f"{small_large} negative")
    else:
        print("negative")
