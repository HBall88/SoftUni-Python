# def even_or_odd_number(num):
#     if num%2==0:
#         return "Even number"
#     else:
#         return "Odd number"
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(filter(lambda x: x%2 == 0, numbers))
# print(result)

# def check_numbers(num):
#     if num%2==0:
#         return True
#     else:
#         return False
#
# result = list(filter(check_numbers, numbers))

# numbers = list(map(int, input().split(", ")))
# numbers = []
# num = input()
# numbers += num.split()
# print(numbers)
# numbers += map(int, numbers)
# print(numbers)

# numbers = map(int, ["1", "2", "3"])
# print(numbers)

# def print_header():
#     print(f'This is header!')
#
# print_header()

# def sum_function(a, b):
#     return a+b
#
# def subtract_function(a, b):
#     return a - b
#
# def operations_with_numbers(a, b):
#     print(sum_function(a, b))
#     print(subtract_function(a, b))
#
# operations_with_numbers(5, 1)

# def countdown(number):
#     print(number)
#     if number == 0:
#         return
#     else:
#         countdown(number-1)
#
# countdown(5)

# def hello():
#     return "Hello SoftUni"
# print(hello())

# def hello(name):
#     return f'Hello {name}'
#
# print(hello(input()))

# def odd_even_number(number):
#     if number%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(odd_even_number(5))

# def odd_even_number(number):
#     result = None
#     if number%2==0:
#         result = "Even"
#     else:
#         result = "Odd"
#     return result
# print(odd_even_number(5))
#
# def person(first_name = "John", last_name = "Smith"):
#     print(first_name, last_name)
# person("Ivan")

# def greet(name):
#     print(f'Hello {name}')
#
# greet("Mike")
# greet () #error

# def greet(f_name, l_name):
#     '''This function just says Hello'''
#     print(f'Hello {f_name} {l_name}')

# x = lambda a, b, c: a*b*c
#
# print(x(1, 2, 3))

