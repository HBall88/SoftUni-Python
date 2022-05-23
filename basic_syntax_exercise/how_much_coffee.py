coffee_counter=0
while True:
    command=str(input())
    if command=="END":
        break
    else:
        if command=="coding" or command=="dog" or command=="cat" or command=="movie":
            coffee_counter+=1
        elif command=="CODING" or command=="DOG" or command=="CAT" or command=="MOVIE":
            coffee_counter+=2
if coffee_counter<=5:
    print(coffee_counter)
else:
    print(f'You need extra sleep')