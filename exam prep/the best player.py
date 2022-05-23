counter=0
text=str(input())
while True:
    if text=="End":
        break
    else:
        for char in text:
            char=int(char)
            if 0<=char<=9:
                counter+=1
                break
            else:
                break
    text = str(input())
print(counter)