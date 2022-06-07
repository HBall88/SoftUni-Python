n=int(input())

numbers = []
filtered_numbers = []

for _ in range(n):
    number=int(input())
    numbers.append(number)

command=input()
if command == "even":
    for num in numbers:
        if num%2==0 or num==0:
            filtered_numbers.append(num)
elif command == "odd":
    for num in numbers:
        if num%2!=0 and num!=0:
            filtered_numbers.append(num)
elif command == "positive":
    for num in numbers:
        if num>=0:
            filtered_numbers.append(num)
elif command == "negative":
    for num in numbers:
        if num<0:
            filtered_numbers.append(num)
print(filtered_numbers)