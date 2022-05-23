fuel=str(input())
liters=float(input())
if fuel=="Diesel":
    if liters>=25:
        print("You have enough diesel.")
    if liters<25:
        print("Fill your tank with diesel!")
elif fuel=="Gasoline":
    if liters>=25:
        print("You have enough gasoline.")
    if liters<25:
        print("Fill your tank with gasoline!")
elif fuel=="Gas":
    if liters>=25:
        print("You have enough gas.")
    if liters<25:
        print("Fill your tank with gas!")
else:
    print("Invalid fuel!")