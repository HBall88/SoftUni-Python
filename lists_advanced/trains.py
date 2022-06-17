count = int(input())
train = [0] * count

while True:
    command = input()
    if command == "End":
        break
    data = command.split(" ")
    current = data[0]
    if current == "add":
        people_to_add = data[1]
        train[-1] += int(people_to_add)
    elif current == "insert":
        index = int(data[1])
        number_of_people = int(data[2])
        train[index] += number_of_people
    elif current == "leave":
        index = int(data[1])
        number_of_people = int(data[2])
        train[index] -= number_of_people

print(train)