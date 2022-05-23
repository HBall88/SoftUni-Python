import math
SeriesName=str(input())
EpisodeLength=int(input())
BreakDurance=int(input())
LunchTime=(1/8)*BreakDurance
RelaxTime=(1/4)*BreakDurance
Atime=BreakDurance-(LunchTime+RelaxTime)
if EpisodeLength<=Atime:
    h=math.ceil(Atime-EpisodeLength)
    print(f'You have enough time to watch {SeriesName} and left with {h} minutes free time.')
if EpisodeLength>Atime:
    h=math.ceil(EpisodeLength-Atime)
    print(f"You don't have enough time to watch {SeriesName}, you need {h} more minutes.")