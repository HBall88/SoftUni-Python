todo_list = []
while True:
    task = input().split('-')
    if task[0] == 'End':
        break
    todo_list.append([int(task[0]), task[1]])

todo_list.sort(key=lambda x: x[0])
todo_list = [item[1] for item in todo_list]
print(todo_list)