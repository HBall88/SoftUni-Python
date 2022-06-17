# current_version = [int(number) for number in input().split(".")]
# current_version[-1] += 1
# for current_index in range(len(current_version)-1, -1, -1):
#     if current_version[current_index]>9:
#         current_version[current_index] = 0
#         if current_index - 1 >= 0:
#             current_version[current_index - 1] += 1
#
# print(".".join(str(number) for number in current_version))

version = input()
version = int(version.replace(".", ""))
version += 1
