first_direction = input("Do you want to go left or right? (l/r): ")
if first_direction == "l": 
    print("you've entered a haunted house")
    print("you hear sounds. you see a hallway. and there are stairs.")
    print("do you want to go up the stairs or down the hallway? (s/h): ") 
    x = input()
    if x == "a":
        print("you decide to go up the stairs")
    elif x == "b":
        print("you decide to go down the hallway")
    else:
        print("you're confused and don't know what to do")

else:
    print("you're in a dungeon")
print("you see a door and a window. do you want to go through the door or the window? (d/w): ")
y = input()
if y == "d":
    print("you decide to go through the door")
elif y == "w":
    print("you decide to go through the window")
else:
    print("you're confused and don't know what to do")
n = input("you see a monster. do you want to fight or run? (f/r): ")
if n == "f":
    print("you decide to fight the monster")
elif n == "r":
    print("you decide to run away from the monster")
if n == "f":
    print("you get thrown in space and die. you lose")
elif n == "r":
    print("you run away and escape.")
    print("you see a spaceship. do you want to go in the spaceship or keep running? (s/r): ")
    z = input()
    if z == "s":
        print("you go in the spaceship and escape. you win!")
    elif z == "r":
        print("you find a ghost")
        print("is the ghost friendly or scary? (f/s): ")
        a = input()
if a == "f":
        print("the ghost is friendly and helps you escape.")
    elif a == "s":
        print("the ghost is scary and kills you. you lose.")
        print ("you see a treasure chest. do you want to open it or leave it? (o/l): ")
        b = input()
if b == "o":
        print("you open the treasure chest and find gold. you win!")
    elif b == "l":
        print("you don't open the treasure chest and leave it.")
        print("theres a broken clock on the ground. do you want to fix it or leave it? (f/l): ")
        c = input()
if c == "f":
        print("you fix the clock and it starts working.")
    elif c == "l":
        print("you leave the clock and continue on your way.")
