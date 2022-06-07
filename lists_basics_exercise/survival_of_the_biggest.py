strings = input().split(" ")
how_many_to_remove = int(input())
numbers = []
ready = []

for string in strings:
    numb = int(string)
    numbers.append(numb)

for number in numbers:
    numbers.remove(min(numbers))
    how_many_to_remove-=1
    if how_many_to_remove==0:
        break

for number in numbers:
    ready.append(str(number))

numbers_as_string = ", ".join(ready)
print(numbers_as_string)