n=int(input())
for _ in range(n):
    stringey=str(input())
    for char in stringey:
        if char=="," or char=="." or char== "_":
            print(f'{stringey} is not pure!')
            exit()
    else:
        print(f'{stringey} is pure.')