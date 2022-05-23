import math
figure=str(input())
if figure=="square":
    stranak=float(input())
    Sk=stranak*stranak
    print(format(Sk, ".3f"))
elif figure=="rectangle":
    stranap1=float(input())
    stranap2=float(input())
    Sp=stranap1*stranap2
    print(format(Sp, ".3f"))
elif figure=="circle":
    radius=float(input())
    So=math.pi*radius*radius
    print(format(So, ".3f"))
elif figure=="triangle":
    stranat=float(input())
    visochina=float(input())
    St=stranat*visochina/2
    print(format(St, ".3f"))