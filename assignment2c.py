# Hart, Gabriel
# Computer Programming, p4
# Assignment #2c: Homework 2
# September 18, 2026

# Step 1: Initialize the flight log
flight_log = [1000, 2500, 4200, 6000, 7800, 9500, 11000, 12500]
print("Initial log:", flight_log)

# Step 2: Append new sensor readings
flight_log.append(14000)
print("After first append:", flight_log)

flight_log.append(15500)
print("After second append:", flight_log)

# Step 3: Remove corrupted early entries with pop(index)
removed = flight_log.pop(0)
print("After pop:", flight_log)

removed = flight_log.pop(0)
print("After second pop:", flight_log)

# Step 4: Insert a missing mid-flight reading
flight_log.insert(3, 9000)
print("After insert:", flight_log)

# Step 5: Print tracking logs, including an explicit index lookup
print(f"Reading at index 3: {flight_log[3]}")
print("Final flight log:", flight_log)