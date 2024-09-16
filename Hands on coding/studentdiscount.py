# Function to determine discount percentage
def calculate_discount(grade, sports_team, drama_club):
    discount = 0
    
    if grade == "a":
        discount = 30
        if sports_team == "yes" or drama_club == "yes":
            discount += 10
    elif grade == "b":
        discount = 20
        if sports_team == "yes" and drama_club == "yes":
            discount += 10
        elif sports_team == "yes" or drama_club == "yes":
            discount += 5
    elif grade == "c":
        discount = 10
        if sports_team == "yes" or drama_club == "yes":
            discount += 5
    elif grade == "d":
        discount = 5
        if sports_team == "yes" or drama_club == "yes":
            discount += 5
    else:
        return "Invalid grade input."

    return f"Your discount percentage is: {discount}%"

# Main part of the program
grade = input("Enter your letter grade (a, b, c, d): ").lower()
sports_team = input("Are you part of a sports team? (yes/no): ").lower()
drama_club = input("Are you part of the drama club? (yes/no): ").lower()

# Display the discount percentage
discount_message = calculate_discount(grade, sports_team, drama_club)
print(discount_message)
