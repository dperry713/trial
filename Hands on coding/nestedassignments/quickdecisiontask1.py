attendees = input("Enter number of attendees: ")
attendees = int(attendees)
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
