strings = input().split(", ")
numbers = []
zeros_counter = 0

for string in strings:
    number = int(string)
    numbers.append(number)

for number in numbers:
    if number == 0:
        zeros_counter+=1
        numbers.remove(number)

for _ in range(0, zeros_counter):
    numbers.append(0)

print(numbers)