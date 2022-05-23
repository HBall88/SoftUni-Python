student_tickets_counter = 0
kids_tickets_counter = 0
standart_tickets_counter = 0
total_tickets_counter = 0
command = input()
while command != "Finish":
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    total_places = free_places
    while free_places > 0:
        ticket_type = str(input())
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter += 1
        elif ticket_type == "standart":
            standart_tickets_counter += 1
        elif ticket_type == "kid":
            kids_tickets_counter +=1
        free_places-=1
        sold_tickets+=1
        total_tickets_counter+=1
    percent_fullness=sold_tickets/total_places*100
    print(f'{movie_name} - {percent_fullness:.2f}% full')
    command = input()
student_tickets_percent=student_tickets_counter/total_tickets_counter*100
standart_tickets_percent = standart_tickets_counter / total_tickets_counter * 100
kids_tickets_percent = kids_tickets_counter / total_tickets_counter * 100
print(f'Total tickets: {total_tickets_counter}')
print(f'{student_tickets_percent:.2f}% student tickets.')
print(f'{standart_tickets_percent:.2f}% standart tickets.')
print(f'{kids_tickets_percent:.2f}% kids tickets.')