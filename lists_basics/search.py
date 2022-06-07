n = int(input())
keyword = input()
list_1 = []
list_2 = []
for _ in range(n):
    action=input()
    list_1.append(action)
    if keyword in action:
        list_2.append(action)
print(list_1)
print(list_2)