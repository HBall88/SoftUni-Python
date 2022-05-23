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

for counter in range(1, classes_count+1): #+1, защото стойността на classes_count е exclusive :)
    #добавяме дължината на часа
    minutes_current+=class_duration
    if minutes_current>=60:
        hours_current+=minutes_current//60
        minutes_current%=60

    #принтираме края на i-тия час
    print(f'End of class №{counter}: {hours_current:02d}:{minutes_current:02d}')
    if counter==classes_count:
        print(f'Your classes end at: {hours_current:02d}:{minutes_current:02d}')
        break

    #добавяме дължината на междучасието:
    #1 и 2 час - 10 минути
    #3 час - 20 минути
    #след 3 час - 5 минути
    #ако часовете са по 30 минути, то сме онлайн и всички междучасия са по 10 минути
    pause_type=""
    if class_duration==30:
        pause_type = "10 minutes break"
        minutes_current += 10
        if minutes_current >= 60:
            hours_current += minutes_current // 60
            minutes_current %= 60

    else:
        if counter<3:
            pause_type="10 minutes break"
            minutes_current+=10
            if minutes_current >= 60:
                hours_current += minutes_current // 60
                minutes_current %= 60

        elif counter==3:
            pause_type="20 minutes break"
            minutes_current+=20
            if minutes_current >= 60:
                hours_current += minutes_current // 60
                minutes_current %= 60

        elif counter>3:
            pause_type="5 minute break"
            minutes_current+=5
            if minutes_current >= 60:
                hours_current += minutes_current // 60
                minutes_current %= 60

    #принтираме края на i-тото междучасие (ако има такова)
    print(f'End of break №{counter}: {hours_current:02d}:{minutes_current:02d}')
    print(" ")
