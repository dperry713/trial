attendees = input("Enter number of attendees: ")
attendees = int(attendees)

# Determine venue
venue = "large hall" if attendees > 100 else "conference room"

# Determine equipment
if attendees > 50:
    audio_system = "professional audio system"
else:
    audio_system = "basic speakers"

if attendees > 30:
    visual_equipment = "projector and screen"
else:
    visual_equipment = "large monitor"

# Additional recommendations
if attendees > 100:
    additional_rec = "Consider hiring event staff"
elif attendees > 50:
    additional_rec = "Consider providing refreshments"
else:
    additional_rec = "Basic setup should suffice"

# Print recommendations
print(f"Recommended venue: {venue}")
print(f"Recommended audio: {audio_system}")
print(f"Recommended visual equipment: {visual_equipment}")
print(f"Additional recommendation: {additional_rec}")
