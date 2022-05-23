while True:
    command=str(input())
    if command=="End":
        exit()
    else:
        if command=="SoftUni":
            continue
        for char in command:
            print(f"{char}{char}", end="")
        print()
