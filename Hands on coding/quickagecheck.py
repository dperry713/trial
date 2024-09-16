# Function to determine access to games based on age
def check_game_access(age):
    if age >= 18:
        return "You are old enough to access all games."
    else:
        if age >= 13:
            return "You can access teen-rated games."
        elif age >= 7:
            return "You can access games rated for ages 7 and above."
        else:
            return "You are only allowed to access games suitable for all ages."

# Main part of the program
try:
    age = int(input("Enter your age: "))

    # Display the appropriate message based on age
    message = check_game_access(age)
    print(message)

except ValueError:
    print("Please enter a valid number for your age.")
