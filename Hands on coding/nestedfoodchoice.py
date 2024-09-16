# Function to suggest a dish based on meal type and dietary preference
def suggest_dish(meal_type, dietary_preference):
    if meal_type == "veg":
        if dietary_preference == "sugar free":
            return "Recommended dish: Grilled vegetable salad with sugar-free dressing."
        elif dietary_preference == "regular":
            return "Recommended dish: Vegetable curry with rice."
        else:
            return "Invalid dietary preference input."
    elif meal_type == "non-veg":
        if dietary_preference == "sugar free":
            return "Recommended dish: Grilled chicken with a side of steamed vegetables."
        elif dietary_preference == "regular":
            return "Recommended dish: Chicken biryani."
        else:
            return "Invalid dietary preference input."
    else:
        return "Invalid meal type input."

# Main part of the program
meal_type = input("Enter your meal type preference (veg/non-veg): ").lower()
dietary_preference = input("Enter your dietary preference (sugar free/regular): ").lower()

# Display the recommended dish
dish = suggest_dish(meal_type, dietary_preference)
print(dish)
