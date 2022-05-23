town=str(input())
sales=float(input())
comission=0
if town=="Sofia":
    if 0<=sales<=500:
        comission=0.05*sales
    elif 500<sales<=1000:
        comission = 0.07 * sales
    elif 1000<sales<=10000:
        comission = 0.08 * sales
    elif sales>10000:
        comission=0.12*sales
elif town=="Varna":
    if 0<=sales<=500:
        comission=0.045*sales
    elif 500<sales<=1000:
        comission = 0.075 * sales
    elif 1000<sales<=10000:
        comission = 0.10 * sales
    elif sales>10000:
        comission=0.13*sales
elif town=="Plovdiv":
    if 0<=sales<=500:
        comission=0.055*sales
    elif 500<sales<=1000:
        comission = 0.08 * sales
    elif 1000<sales<=10000:
        comission = 0.12 * sales
    elif sales>10000:
        comission=0.145*sales
if comission>0:
    print(format(comission, ".2f"))
else:
    print("error")