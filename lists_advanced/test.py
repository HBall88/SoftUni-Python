#
# even_numbers = [num for num in [1, 2, 3, 4, 5, 6] if num%2==0]
#
# print(even_numbers)

# print([x for x in range(11)])
# print(list(range(11)))

# nums = [1, 2,3, 4, 5, 6, 7, 8, 9, 10]
# result = [num for num in nums if num%2==0 if num>5 if num!=10]
# # print(result)

# matrix = [[x for x in range(3)] for _ in range(3)]
# print(matrix)

# list = [1, 2, 3]
# list += [4]
# list.append(4)
# print(list)

# list = [1, 2, 3]
# list+=[5, 6, 11]
# list.extend([12, 2, 1])
# print(list)

# list = [1, 2, 3, 4, 5, 6, 4, 2, 3, 4]
# list.insert(0, 69)
# print(list)

# my_list = [1, 2, 3, 4]
# my_list.clear()
# print(my_list)

# my_list = [1, 2, 3, 4, 5, 6, 7]
# my_list.pop()
# print(my_list)

# my_list = [1, 2, 3, 2]
# my_list.remove(2)
# print(my_list)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
# del my_list[0:5]
# print(my_list)

# my_list = [1, 2, 3, 3, 5, 3, 6]
# print(my_list.count(3))

# my_list = [1, 2, 3, 2, 2]
# last = my_list.index(2)
# print(last)

# my_list = [1, 2, 3, 4, 5]
# a = my_list.reverse()
# print(a)

# nums = ["one", "three", "two", "eleven", "seven"]
# x = sorted(nums, key = len)
# print(x)

# nums = [1, 2, 3, 4, 5, 6]
# def even_numbers(num):
#     return num%2
# sorted_nums = sorted(nums, key = even_numbers)
# print(sorted_nums)

# nums = [1, 2, 3, 4, 5, 6]
# def even_numbers(num):
#     return num%2
# sorted_nums = sorted(nums, reverse=True)
# print(sorted_nums)

# print(list(map(lambda x: x*2, [1, 2, 3, 4, 5, 6])))

print(len([1, 2, 3, 4, 5]))