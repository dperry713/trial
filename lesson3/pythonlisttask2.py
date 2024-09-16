grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order
sorted_grades = sorted(grades, reverse=True)

# Print the sorted list
print("Sorted grades (descending order):")
print(sorted_grades)

# Calculate the average grade
average_grade = sum(grades) / len(grades)

# Print the average grade
print(f"\nAverage grade: {average_grade:.2f}")
