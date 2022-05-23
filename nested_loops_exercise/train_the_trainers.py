judges_count=int(input())
grade_counter=0
grade_treshhold=0
grade_counter_global=0
grade_treshhold_global=0
grade_average=0
grade_average_global=0
presentation_name=str(input())
while True:
    if presentation_name=="Finish":
        print(f"Student's final assessment is {grade_average_global:.2f}.")
        break
    for shitty_useless_counter in range(0, judges_count):
        grade_current=float(input())
        grade_counter_global +=1
        grade_treshhold_global +=grade_current
        grade_counter+=1
        grade_treshhold+=grade_current
    grade_average=grade_treshhold/grade_counter
    grade_average_global = grade_treshhold_global/grade_counter_global
    print(f'{presentation_name} - {grade_average:.2f}.')
    grade_counter =0
    grade_treshhold =0
    presentation_name=str(input())