weight=float(input())
type=str(input())
distance=int(input())
price=0
if type=="standard":
    if weight<1:
        price=0.03*distance
    elif 1<=weight<10:
        price=0.05*distance
    elif 10<=weight<40:
        price=0.10*distance
    elif 40<=weight<90:
        price=0.15*distance
    elif 90<=weight<150:
        price=0.20*distance
elif type=="express":
    if weight<1:
        over_kilo=0.8*0.03
        over_km=weight*over_kilo
        up=over_km*distance
        price=0.03*distance+up
    elif 1<=weight<10:
        over_kilo = 0.4 * 0.05
        over_km = weight * over_kilo
        up = over_km * distance
        price=0.05*distance+up
    elif 10<=weight<40:
        over_kilo = 0.05 * 0.10
        over_km = weight * over_kilo
        up = over_km * distance
        price=0.10*distance+up
    elif 40<=weight<90:
        over_kilo = 0.02 * 0.15
        over_km = weight * over_kilo
        up = over_km * distance
        price=0.15*distance+up
    elif 90<=weight<150:
        over_kilo = 0.01 * 0.20
        over_km = weight * over_kilo
        up = over_km * distance
        price=0.20*distance+up
price1=format(price, ".2f")
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price1} lv.")