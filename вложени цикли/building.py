floors=int(input())
spaces=int(input())
counter=-1
if floors==1:
    counter = -1
    for i in range(1, spaces+1):
        counter+=1
        print(f'L{floors}{counter}', end=" ")
    print()
else:
    counter = -1
    for i in range(1, spaces + 1):
        counter += 1
        print(f'L{floors}{counter}', end=" ")
    print()
    for i in range(floors-1, 0, -1):
        if i%2!=0:
            counter=-1
            for j in range(1, spaces+1):
                counter+=1
                print(f"A{i}{counter}", end=" ")
            print()
        if i%2==0:
            counter=-1
            for j in range(1, spaces+1):
                counter+=1
                print(f"O{i}{counter}", end=" ")
            print()
