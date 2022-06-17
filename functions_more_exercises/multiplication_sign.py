number_one = int(input())
number_two = int(input())
number_three = int(input())

def is_zero(x):
    if x == 0:
        return True
    else:
        return False

def is_negative(x):
    if x<0:
        return True
    else:
        return False

def sign_is_minus(x):
    if x%2 == 0:
        return "positive"
    else:
        return "negative"

negative_signs_counter = 0
if is_zero(number_one):
    print(f'positive')
    exit()
elif is_negative(number_one):
    negative_signs_counter+=1

if is_zero(number_two):
    print(f'positive')
    exit()
elif is_negative(number_two):
    negative_signs_counter+=1

if is_zero(number_three):
    print(f'positive')
    exit()
elif is_negative(number_three):
    negative_signs_counter+=1

print(sign_is_minus(negative_signs_counter))
