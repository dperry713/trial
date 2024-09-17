import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Relaxed", "Stressed", "Focused", "Bored"]

# List of days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of times of the day
times = ["Morning", "Afternoon", "Evening"]

# Outer loop: iterate through each day of the week
for day in range(7):
    print(f"\n{days[day]}:")
    
    # Inner loop: iterate through each time of the day
    for time in times:
        # Randomly select a mood
        mood = random.choice(moods)
        
        # Print the time of day and the randomly selected mood
        print(f"  {time}: {mood}")
