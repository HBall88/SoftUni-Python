string = input()
repeater = int(input())
def reppy(string, repeater):
    for _ in range(repeater):
        print(string, end="")

reppy(string, repeater)