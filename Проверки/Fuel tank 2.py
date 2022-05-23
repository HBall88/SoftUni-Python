type_of_fuel=str(input())
quantity=float(input())
club_card=str(input())
if club_card=="Yes":
    if type_of_fuel=="Gasoline":
        v=quantity*2.04
        if 20<quantity<=25:
            vgot=v-0.08*v
            print(format(vgot, ".2f") + " lv.")
        if quantity>25:
            vgot=v-0.10*v
            print(format(vgot, ".2f")+" lv.")
        if quantity<20:
            vgot=v
            print(format(vgot, ".2f") + " lv.")
    if type_of_fuel=="Diesel":
        v=quantity*2.21
        if 20<quantity<=25:
            vgot=v-0.08*v
            print(format(vgot, ".2f") + " lv.")
        if quantity>25:
            vgot=v-0.10*v
            print(format(vgot, ".2f")+" lv.")
        if quantity < 20:
            vgot=v
            print(format(vgot, ".2f") + " lv.")
    if type_of_fuel=="Gas":
        v=quantity*0.85
        if 20<quantity<=25:
            vgot=v-0.08*v
            print(format(vgot, ".2f") + " lv.")
        if quantity>25:
            vgot=v-0.10*v
            print(format(vgot, ".2f")+" lv.")
        if quantity < 20:
            vgot=v
            print(format(vgot, ".2f") + " lv.")
if club_card=="No":
    if type_of_fuel == "Gasoline":
        v = quantity * 2.22
        if 20 < quantity <= 25:
            vgot = v - 0.08 * v
            print(format(vgot, ".2f") + " lv.")
        if quantity > 25:
            vgot = v - 0.10 * v
            print(format(vgot, ".2f") + " lv.")
        if quantity<20:
            vgot=v
            print(format(vgot, ".2f") + " lv.")
    if type_of_fuel == "Diesel":
        v = quantity * 2.33
        if 20 < quantity <= 25:
            vgot = v - 0.08 * v
            print(format(vgot, ".2f") + " lv.")
        if quantity > 25:
            vgot = v - 0.10 * v
            print(format(vgot, ".2f") + " lv.")
        if quantity < 20:
            vgot=v
            print(format(vgot, ".2f") + " lv.")
    if type_of_fuel=="Gas":
        v=quantity*0.93
        if 20<quantity<=25:
            vgot=v-0.08*v
            print(format(vgot, ".2f") + " lv.")
        if quantity>25:
            vgot=v-0.10*v
            print(format(vgot, ".2f")+" lv.")
        if quantity < 20:
            vgot=v
            print(format(vgot, ".2f") + " lv.")