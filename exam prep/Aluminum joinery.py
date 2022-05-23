count_of_frames=int(input())
type_of_frames=str(input())
way_of_delivery=str(input())
sum1=0
sum2=0
sum3=0
sum4=0
if count_of_frames<10:
    print("Invalid order")
elif type_of_frames=="90X130":
    sum1=count_of_frames*110
    if count_of_frames>30:
        sum2=0.95*sum1
    if count_of_frames>60:
        sum2=0.92*sum1
    if way_of_delivery=="With delivery":
        sum3=sum2+60
    if way_of_delivery=="Without delivery":
        sum3=sum2
    if count_of_frames>99:
        sum4=0.96*sum3
    print(f'{format(sum4, ".2f")} BGN')
elif type_of_frames=="100X150":
    sum1=count_of_frames*140
    if count_of_frames>40:
        sum2=0.94*sum1
    if count_of_frames>80:
        sum2=0.9*sum1
    if way_of_delivery=="With delivery":
        sum3=sum2+60
    if way_of_delivery=="Without delivery":
        sum3=sum2
    if count_of_frames>99:
        sum4=0.96*sum3
    print(f'{format(sum4, ".2f")} BGN')
elif type_of_frames=="130X180":
    sum1=count_of_frames*190
    if count_of_frames>20:
        sum2=0.93*sum1
    if count_of_frames>50:
        sum2=0.88*sum1
    if way_of_delivery=="With delivery":
        sum3=sum2+60
    if way_of_delivery=="Without delivery":
        sum3=sum2
    if count_of_frames>99:
        sum4=0.96*sum3
    print(f'{format(sum4, ".2f")} BGN')
elif type_of_frames=="200X300":
    sum1=count_of_frames*250
    if count_of_frames>25:
        sum2=0.91*sum1
    if count_of_frames>50:
        sum2=0.86*sum1
    if way_of_delivery=="With delivery":
        sum3=sum2+60
    if way_of_delivery=="Without delivery":
        sum3=sum2
    if count_of_frames>99:
        sum4=0.96*sum3
    print(f'{format(sum4, ".2f")} BGN')