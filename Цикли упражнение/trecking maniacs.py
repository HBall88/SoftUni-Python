groups_count=int(input())
sum_people=0
sum_Musala=0
sum_Monblan=0
sum_Kilimanjaro=0
sum_K2=0
sum_Everest=0
Musala=0
Monblan=0
Kilimanjaro=0
K2=0
Everest=0
for i in range(0, groups_count):
    g=int(input())
    if g<=5:
        sum_people+=g
        sum_Musala+=g
    if 6<=g<=12:
        sum_people+=g
        sum_Monblan+=g
    if 13<=g<=25:
        sum_people+=g
        sum_Kilimanjaro+=g
    if 26<=g<=40:
        sum_people+=g
        sum_K2+=g
    if g>=41:
        sum_people+=g
        sum_Everest+=g
Musala=format(sum_Musala/sum_people*100, ".2f")
Monblan=format(sum_Monblan/sum_people*100, ".2f")
Kilimanjaro=format(sum_Kilimanjaro/sum_people*100, ".2f")
K2=format(sum_K2/sum_people*100, ".2f")
Everest=format(sum_Everest/sum_people*100, ".2f")
print(Musala+"%")
print(Monblan+"%")
print(Kilimanjaro+"%")
print(K2+"%")
print(Everest+"%")