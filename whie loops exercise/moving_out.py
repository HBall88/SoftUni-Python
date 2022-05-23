width=int(input())
length=int(input())
height=int(input())
space=width*length*height
boxes_count=input()
sum_boxes=0
diff=0
while boxes_count!="Done":
    boxes_count=int(boxes_count)
    sum_boxes+=boxes_count
    if sum_boxes>=space:
        break
    boxes_count=input()
diff=space-sum_boxes
if diff<0:
    print(f'No more free space! You need {abs(diff)} Cubic meters more.')
else:
    print(f'{abs(diff)} Cubic meters left.')