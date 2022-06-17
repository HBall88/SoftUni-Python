# initial_energy = int(input())
# won_battles = 0
#
# while True:
#     command_current = input()
#     if command_current == "End of battle":
#         break
#     else:
#         command = int(command_current)
#     initial_energy -= command
#
#     if won_battles%3==0:
#         initial_energy+=won_battles
#
#
#     if initial_energy < 0:
#         print(f"Not enough energy! Game ends with {won_battles} won battles and 0 energy")
#         exit()
#
#     won_battles += 1
#
# print(f"Won battles: {won_battles}. Energy left: {initial_energy}")

initial_energy = int(input())

strike = 0
win = True

command = input()

while not command == "End of battle":
    distance = int(command)
    initial_energy -= distance
    strike += 1

    if strike % 3 == 0:
        initial_energy += strike

    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {strike} won battles and {initial_energy} energy")
        win = False
        break

    command = input()

else:
    print(f"Won battles: {strike}. Energy left: {initial_energy}")