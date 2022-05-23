import math
beginning=int(input())
first_digit_beg=math.floor(beginning/1000%10)
second_digit_beg=math.floor(beginning/100%10)
third_digit_beg=math.floor(beginning/10%10)
forth_digit_beg=math.floor(beginning%10)
end=int(input())
first_digit_end=math.floor(end/1000%10)
second_digit_end=math.floor(end/100%10)
third_digit_end=math.floor(end/10%10)
forth_digit_end=math.floor(end%10)

for ticker in range(beginning, end+1):
    truth_counter = 0
    digits_counter=0
    first_digit_counter=0
    second_digit_counter=0
    third_digit_counter = 0
    forth_digit_counter = 0
    for char in str(ticker):
        char=int(char)
        if char%2!=0:
            truth_counter+=1
    if truth_counter==4:
        for char in str(ticker):
            char = int(char)
            digits_counter+=1
            if digits_counter==1:
                if first_digit_beg<=char<=first_digit_end:
                    first_digit_counter+=1
            elif digits_counter==2:
                if second_digit_beg<=char<=second_digit_end:
                    second_digit_counter+=1
            elif digits_counter==3:
                if third_digit_beg<=char<=third_digit_end:
                    third_digit_counter+=1
            elif digits_counter==4:
                if forth_digit_beg<=char<=forth_digit_end:
                    forth_digit_counter+=1
        if first_digit_counter==1 and second_digit_counter==1 and third_digit_counter==1 and forth_digit_counter==1:
            print(ticker, end=" ")
