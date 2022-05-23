n=int(input())
for _ in range(n):
    m = int(input())
    if m==88:
        print(f'Hello')
    elif m==86:
        print(f'How are you?')
    elif m<88 and m!=88 and m!=86:
        print(f'GREAT!')
    else:
        print(f'Bye.')

