PochivniDni=int(input())
Pdv=PochivniDni*127
RabotniDni=365-PochivniDni
Rdv=RabotniDni*63
SumaVreme=Pdv+Rdv
if SumaVreme<=30000:
    print("Tom sleeps well")
    fi1=30000-SumaVreme
    Chasove=fi1//60
    Minuti=((fi1%60)/60)*60
    print(f'{format(Chasove, ".0f")} hours and {format(Minuti, ".0f")} minutes less for play')
else:
    print("Tom will run away")
    fi2=SumaVreme-30000
    Chasove = fi2 // 60
    Minuti = ((fi2 % 60) / 60) * 60
    print(f'{format(Chasove, ".0f")} hours and {format(Minuti, ".0f")} minutes more for play')