number=int(input())
for current_number in range(1111, 10000):
    number_is_spetial = True
    current_number_as_string=str(current_number)
    for current_digit in current_number_as_string:
        if int(current_digit)==0 or number%int(current_digit)!=0:
            number_is_spetial=False
            break
    if number_is_spetial:
        print(current_number, end=" ")