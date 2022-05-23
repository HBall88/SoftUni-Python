record_in_seconds=float(input())
distance_in_meters=float(input())
one_meter_distance_time=float(input())
slow_downs_count=distance_in_meters//50
slow_downs=slow_downs_count*30
george_time=distance_in_meters*one_meter_distance_time+slow_downs
if george_time<record_in_seconds:
    print(f'Yes! The new record is {george_time:.2f} seconds.')
else:
    difference=george_time-record_in_seconds
    print(f'No! He was {difference:.2f} seconds slower.')