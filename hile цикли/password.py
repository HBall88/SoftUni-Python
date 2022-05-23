username=str(input())
password=str(input())
i=str(input())
if i == password:
    print(f"Welcome {username}!")
while i!=password:
    i=str(input())
    if i==password:
        print(f"Welcome {username}!")
        break