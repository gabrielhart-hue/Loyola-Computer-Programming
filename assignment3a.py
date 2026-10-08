# Gabriel Hart
# Computer Programming, Period 4
# Assignment 3a
# October 7th, 2026

alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points for shooting the alien.")

alien_color = "yellow"

if alien_color == "green":
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points for shooting the alien.")


alien_color = "green"

if alien_color == "green":
    print("The player earned 5 points.")
elif alien_color == "yellow":
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

alien_color = "yellow"

if alien_color == "green":
    print("The player earned 5 points.")
elif alien_color == "yellow":
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

alien_color = "red"

if alien_color == "green":
    print("The player earned 5 points.")
elif alien_color == "yellow":
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")


age = 21

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


usernames = ["admin", "Jaden", "Sarah", "Mike", "Alex"]

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")


current_users = ["John", "Mike", "Sarah", "Alex", "David"]

new_users = ["JOHN", "Tom", "Sarah", "Chris", "Emma"]

current_users_lower = []

for username in current_users:
    current_users_lower.append(username.lower())

for username in new_users:
    if username.lower() in current_users_lower:
        print(username + " will need to enter a new username.")
    else:
        print(username + " is available.")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")