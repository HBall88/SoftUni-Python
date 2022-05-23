time1=int(input())
time2=int(input())
time3=int(input())
timesum=time1+time2+time3
timemin=timesum//60
timesec=timesum%60
if timesec<10:
    print(f'{timemin}:0{timesec}')
else:
    print(f'{timemin}:{timesec}')