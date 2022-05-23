command = input()
initial_hiking_meters = 5364
the_peak_height = 8848
days_for_hiking = 1
while command != "END":
    meters_to_hike = int(input())
    if command == "Yes":
        days_for_hiking += 1
        if days_for_hiking > 5:
            print("Failed!")
            print(f"{initial_hiking_meters}")
            break
        initial_hiking_meters += meters_to_hike
    else:
        initial_hiking_meters += meters_to_hike
    if initial_hiking_meters >= the_peak_height:
        print(f"Goal reached for {days_for_hiking} days!")
        break
    command = input()
if command == "END":
    if initial_hiking_meters >= the_peak_height:
        print(f"Goal reached for {days_for_hiking} days!")
    else:
        print("Failed!")
        print(f"{initial_hiking_meters}")