duljina=int(input())
shirochina=int(input())
visochina=int(input())
procent=float(input())
obem=(duljina*shirochina*visochina)/1000
zaetobem=(procent/100)*obem
izpolzwaemobem=obem-zaetobem
print(izpolzwaemobem)