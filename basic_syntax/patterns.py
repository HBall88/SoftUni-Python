length = int(input())
for i in range(1, length + 1):
    for j in range(0, i):
        print("*", end="")
    print()
for i in range(length - 1, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()
