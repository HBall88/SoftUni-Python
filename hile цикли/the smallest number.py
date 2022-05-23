import sys
s=input()
min_number=sys.maxsize
while s!="Stop":
    number=int(s)
    if number<min_number:
        min_number=number
    s=input()
print(min_number)