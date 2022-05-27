n = int(input())
balanced = 0
for i in range(n):
    string = input()
    if string == "(":
        balanced += 1
        if balanced > 1:
            print("UNBALANCED")
            exit()
    elif string == ")":
        balanced -= 1
if balanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")