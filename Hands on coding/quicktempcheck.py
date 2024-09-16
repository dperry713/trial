# Function to suggest a movie genre based on mood and weather
def suggest_movie(mood, weather):
    if mood == "happy":
        if weather == "sunny":
            return "Recommended movie: A feel-good comedy."
        elif weather == "rainy":
            return "Recommended movie: A light-hearted romantic comedy."
        else:
            return "Invalid weather input."
    elif mood == "sad":
        if weather == "sunny":
            return "Recommended movie: An uplifting drama."
        elif weather == "rainy":
            return "Recommended movie: A comforting, emotional drama."
        else:
            return "Invalid weather input."
    elif mood == "adventurous":
        if weather == "sunny":
            return "Recommended movie: An action-packed adventure or thriller."
        elif weather == "rainy":
            return "Recommended movie: A suspenseful mystery or a fantasy adventure."
        else:
            return "Invalid weather input."
    else:
        return "Invalid mood input."

# Main part of the program
mood = input("Enter your current mood (happy, sad, adventurous): ").lower()
weather = input("Enter the day's weather (rainy/sunny): ").lower()

# Display the recommended movie
movie = suggest_movie(mood, weather)
print(movie)
