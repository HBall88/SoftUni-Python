print(f'When do the classes start?')

print(f'h>>> ', end="")
hours_starting=int(input())
hours_current=hours_starting

print(f'm>>> ', end="")
minutes_starting=int(input())
minutes_current=minutes_starting

print(f'How many classes do you have today?')
classes_count=int(input(">>>> "))

print(f'How long is one class? (in minutes)')
class_duration=int(input(">>>> "))

days_counter=0
for counter in range(1, classes_count+1):
    if counter==1:
        print(f'Beg of class №1: {hours_starting:02d}:{minutes_starting:02d}')
    minutes_current+=class_duration
    if minutes_current>=60:
        hours_current+=minutes_current//60
        minutes_current%=60
    if hours_current>24:
        hours_current=1
        days_counter+=1

    print(f'End of class №{counter}: {hours_current:02d}:{minutes_current:02d}')
    if counter != classes_count:
        print(f'Beg of break №{counter}: {hours_current:02d}:{minutes_current:02d}')
    if counter == classes_count:
        print(" ")
        print(f'Your classes end at: {hours_current:02d}:{minutes_current:02d}')
        if days_counter > 1:
            print(" ")
            print(f'٩( ๑╹ ꇴ╹)۶')
            print(f'Congratulations, you spent {days_counter} days at the school and completely fucked up the program!')
            print(f'Happy now?!')
        break

    pause_type=""
    if class_duration==30:
        pause_type = "10 minutes break"
        minutes_current += 10
        if minutes_current >= 60:
            hours_current += minutes_current // 60
            minutes_current %= 60
        if hours_current > 24:
            hours_current = 1

    else:
        if counter<3:
            pause_type="10 minutes break"
            minutes_current+=10
            if minutes_current >= 60:
                hours_current += minutes_current // 60
                minutes_current %= 60
            if hours_current > 24:
                hours_current = 1

        elif counter==3:
            pause_type="20 minutes break"
            minutes_current+=20
            if minutes_current >= 60:
                hours_current += minutes_current // 60
                minutes_current %= 60
            if hours_current > 24:
                hours_current = 1

        elif counter>3:
            pause_type="5 minute break"
            minutes_current+=5
            if minutes_current >= 60:
                hours_current += minutes_current // 60
                minutes_current %= 60
            if hours_current > 24:
                hours_current = 1

    print(f'End of break №{counter}: {hours_current:02d}:{minutes_current:02d}')
    print(" ")
    print(f'Beg of class №{counter+1}: {hours_current:02d}:{minutes_current:02d}')

