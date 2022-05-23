import sys
s=input()
max_number=-sys.maxsize
while s!="Stop":
    number=int(s)
    if number>max_number:
        max_number=number
    s=input()
print(max_number)