submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Check if Alice submitted the assignment and attended the class
if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted the assignment and attended the class.")
else:
    print("Alice did not submit the assignment or did not attend the class, or both.")
