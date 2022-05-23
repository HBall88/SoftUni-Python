target = 10000
steps = 0
is_goal_reached = False
time_to_exit = False
diff = 0
while not time_to_exit:
    temp_steps = input()
    if temp_steps == "Going home":
        temp_steps = int(input())
        time_to_exit = True
    else:
        temp_steps = int(temp_steps)
    steps += temp_steps
    if steps >= target:
        is_goal_reached = True
        time_to_exit = True
    diff = abs(steps - target)

if is_goal_reached:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")