type=str(input())
rows=int(input())
columns=int(input())
all_seats=rows*columns
final_revenue=0
if type=="Premiere":
    final_revenue=all_seats*12.00
elif type=="Normal":
    final_revenue=all_seats*7.50
elif type=="Discount":
    final_revenue=all_seats*5.00
print(format(final_revenue, ".2f")+" leva")