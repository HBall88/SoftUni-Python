n=int(input())
salary=float(input())
lost_money=0
what_happened=0
for i in range(0, n):
    website_name=str(input())
    if website_name=="Facebook":
        lost_money+=150
    if website_name=="Instagram":
        lost_money+=100
    if website_name=="Reddit":
        lost_money+=50
what_happened=salary-lost_money
if what_happened<=0:
    print(f'You have lost your salary.')
else:
    print(format(what_happened, ".0f"))