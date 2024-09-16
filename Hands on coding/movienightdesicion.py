# Function to determine the outfit
def suggest_outfit(temperature, event_type):
    if event_type == "formal":
        if temperature > 25:
            return "Wear a light suit with breathable fabric and dress shoes."
        elif 15 <= temperature <= 25:
            return "Wear a suit with a tie and formal shoes."
        else:
            return "Wear a warm formal coat over a suit and formal shoes."
    elif event_type == "casual":
        if temperature > 25:
            return "Wear shorts and a t-shirt with sneakers or sandals."
        elif 15 <= temperature <= 25:
            return "Wear jeans or chinos with a light shirt and casual shoes."
        else:
            return "Wear a warm jacket with a sweater and casual shoes."
    else:
        return "Invalid event type."

# Main part of the program
try:
    # Get input from the user
    temperature = float(input("Enter the day's temperature in Celsius: "))
    event_type = input("Enter the type of event (formal/casual): ").lower()

    # Display the recommended outfit
    outfit = suggest_outfit(temperature, event_type)
    print(f"Recommended outfit: {outfit}")

except ValueError:
    print("Please enter a valid number for the temperature.")
