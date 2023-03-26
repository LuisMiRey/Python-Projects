age = 18
height = 170

# and
if age >= 8 and height >= 135:
    print("You can ride th ride! 1")
else:
    print("You are not right")

#or 

if age >= 17 or height >= 160:
    print("You can ride th ride! 2")

#elif (else if)
if height < 120:
    print("You can't tide any ried :(")
elif height < 135:
    print("You can ride level-1 rides")
elif height < 200:
    print("you can ride any ride!")
else:
    print("Too tall to ride the rides :(")

#Exercise

if age >= 18 and height >= 160:
    print("Allowed to drive")
elif age >= 15 or height >= 145:
    print("Allowed to go to the gym")
else:
    print("who you are!")
