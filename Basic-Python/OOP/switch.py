#Requires Python 3.10
#This is switch as in other programming lenguages

direction = input("Which direction? ").lower()

match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "east":
        print("Right")
    case "west":
        print("Left")
    case "west":
        print("Left")
    case _: #All the other options
        print("Not a valid direction")

#Creare a switch for a number 

floor_number = 4
match floor_number:
    case 4:
        print("Unlucky in Japan")
    case 13:
        print("Unlucky in USA")
    case _:
        print("No issues with this number")