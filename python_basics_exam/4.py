computers_count=int(input())
sales_sum=0
sales_counter=0
rating_sum=0
for ticker in range(0, computers_count):
    current_number=int(input())
    rating=current_number%10
    rating_sum+=rating
    sales_possible=current_number//10
    if rating==2:
        sales_current=0.00*sales_possible
        sales_sum+=sales_current
        sales_counter+=1
    elif rating==3:
        sales_current=0.50*sales_possible
        sales_sum+=sales_current
        sales_counter += 1
    elif rating==4:
        sales_current=0.70*sales_possible
        sales_sum+=sales_current
        sales_counter += 1
    elif rating==5:
        sales_current=0.85*sales_possible
        sales_sum+=sales_current
        sales_counter += 1
    elif rating==6:
        sales_current=1.00*sales_possible
        sales_sum+=sales_current
        sales_counter += 1
print(format(sales_sum, ".2f"))
middle=format(rating_sum/computers_count, ".2f")
print(middle)