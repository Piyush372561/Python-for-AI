#Logical operators 
User_age = 16
has_license = True

#AND - both must be true
can_drive = User_age >= 18 and has_license
print("Can drive:", can_drive)

#OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print("Is weekend:", is_weekend)

#NOT - negates the value
is_adult = User_age >= 18
is_child = not is_adult
print("Is child:", is_child)
