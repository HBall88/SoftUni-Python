juniors=int(input())
seniors=int(input())
trace=str(input())
contestants=juniors+seniors
if contestants>=50 and trace=="cross-country":
    before_sum=juniors*(8-0.25*8)+seniors*(9.50-0.25*9.50)
    sum=0.95*before_sum
if contestants<50 and trace=="cross-country":
    sum=0.95*(juniors*8+seniors*9.50)
if trace=="trail":
    sum=0.95*(juniors*5.50+seniors*7)
if trace=="downhill":
    sum=0.95*(juniors*12.25+seniors*13.75)
if trace=="road":
    sum=0.95*(juniors*20+seniors*21.50)
print(format(sum, ".2f"))