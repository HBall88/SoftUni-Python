import math
neobhodimi_chasove=int(input())
dni_koito_imat=int(input())
slujiteli=int(input())
chasove=(dni_koito_imat-0.1*dni_koito_imat)*8+slujiteli*2*dni_koito_imat
chasove_za_polzvane=math.floor(chasove)
if chasove_za_polzvane>=neobhodimi_chasove:
    leftover=chasove_za_polzvane-neobhodimi_chasove
    print(f'Yes!{leftover} hours left.')
else:
    overtime=neobhodimi_chasove-chasove_za_polzvane
    print(f'Not enough time!{overtime} hours needed.')