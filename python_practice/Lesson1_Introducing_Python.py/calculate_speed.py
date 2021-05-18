distance_in_km = 150
time_in_hours = 2

distance_in_miles = distance_in_km/1.6
distance_in_meters = distance_in_km * 1000

time_in_seconds = time_in_hours * 3600

kmph = distance_in_km / time_in_hours
mph = distance_in_miles / time_in_hours
mps = distance_in_meters / time_in_seconds

print("The speed in kilometers per hour is:", kmph)
print("The speed in miles per hour is:", mph)
print("The speed in meters per second is:", mps)