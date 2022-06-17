command = input()
def command_checker(command):
    if command == "int":
        whatever = int(input())
        print(whatever*2)
    elif command == "real":
        whatever = float(input())
        print("{:.2f}".format(whatever*1.5))
    elif command == "string":
        whatever = input()
        print(f'${whatever}$')

command_checker(command)