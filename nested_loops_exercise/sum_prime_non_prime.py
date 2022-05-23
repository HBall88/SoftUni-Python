sum_prime_numbers=0
sum_non_prime_numbers=0
command=input()
while command!="stop":
    current_number=int(input())
    if current_number<0:
        print("Number is negative.")
    else:
        number_is_prime=True
        for number in range(2, current_number):
            if current_number%number==0:
                number_is_prime=False
                break
        if number_is_prime==True:
            sum_prime_numbers+=current_number
        else:
            sum_non_prime_numbers+=current_number
    command=input()