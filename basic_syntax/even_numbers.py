n = int(input())
breakp = False
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        pass
    else:
        print(f"{number} is odd!")
        breakp = True
        break
if breakp != True:
    print("All numbers are even.")
