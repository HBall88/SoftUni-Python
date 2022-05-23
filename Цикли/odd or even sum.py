n = int(input())
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    value = int(input())
    if i % 2 == 0:
        even_sum += value
    else:
        odd_sum += value
if even_sum == odd_sum:
    print(f"Yes, sum = {odd_sum}")
else:
    print(f"No, diff = {abs(even_sum - odd_sum)}")