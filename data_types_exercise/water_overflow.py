n_of_lines=int(input())
capacity=255
water_counter=0
for _ in range(n_of_lines):
    water_added=int(input())
    if capacity-water_added<0:
        print(f'Insufficient capacity!')
        continue
    water_counter+=water_added
    capacity-=water_added
print(water_counter)

