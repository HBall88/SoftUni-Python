# shot_targets = list(map(int, input().split(" ")))
#
# while True:
#     commandc = input()
#     if commandc == "End":
#         break
#     else:
#         command = int(commandc)
#     if command > len(shot_targets)-1:
#         pass
#     else:
#         current_target = shot_targets[command]
#         shot_targets[command] = -1
#         index = 0
#         for target in shot_targets:
#             if target == -1:
#                 pass
#             elif target>current_target:
#                 shot_targets[index] = target-current_target
#             elif target<=current_target:
#                 shot_targets[index] = target+current_target
#         index += 1
#
# targets_counter = 0
#
# for target in shot_targets:
#     if target == -1:
#         targets_counter += 1
#
# shot_targets_as_strings = list(map(str, shot_targets))
# shot_targets_as_a_string = " ".join(shot_targets_as_strings)
# print(f"Shot targets: {targets_counter} -> {shot_targets_as_a_string}")
#     # print(shot_targets)
#     # print(current_target)

targets_sequence_integers = list(map(int, input().split()))
counter = 0

while True:
    command = input()
    if command == "End":
        break
    else:
        index = int(command)
        if index < len(targets_sequence_integers) and targets_sequence_integers[index] > -1:
            target = targets_sequence_integers[index]
            targets_sequence_integers[index] = -1
            for i, num in (enumerate(targets_sequence_integers)):
                if num == -1:
                    continue
                if target < num:
                    targets_sequence_integers[i] -= target
                elif target >= num and num > -1:
                    targets_sequence_integers[i] += target
            counter += 1

print(f"Shot targets: {counter} ->", end=" ")
print(" ".join(map(str, targets_sequence_integers)))