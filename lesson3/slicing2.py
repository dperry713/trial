temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Method 1: Using a list comprehension
temps_above_100 = [temp for temp in temperatures if temp > 100]

print("Temperatures above 100 (using list comprehension):")
print(temps_above_100)

# Method 2: Using list slicing
# First, find the index of the first temperature above 100
start_index = next(i for i, temp in enumerate(temperatures) if temp > 100)

temps_above_100_slice = temperatures[start_index:]

print("\nTemperatures above 100 (using list slicing):")
print(temps_above_100_slice)
