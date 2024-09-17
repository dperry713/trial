import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Relaxed"]

# List of days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week
for day in range(7):
    # Randomly select a mood
    mood = random.choice(moods)
    
    # Print the day and the randomly selected mood
    print(f"{days[day]}: {mood}")
