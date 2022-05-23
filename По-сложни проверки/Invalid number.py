number = int(input())
valid = number == 0 or number >= 100 and number <= 200
if not valid:
    print("invalid")
