place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid choice. The forest is mysterious, and you're lost.")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You light a torch and discover ancient cave paintings!")
    elif action == "proceed in the dark":
        print("You stumble in the dark and find a hidden underground lake!")
    else:
        print("Invalid choice. The cave is enigmatic, and you're disoriented.")
else:
    print("Invalid choice. Please choose either 'forest' or 'cave'.")
