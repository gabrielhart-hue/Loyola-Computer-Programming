first_direction = input("Do you want to go left or right? (l/r): ")
if first_direction == "l":
    print("you've entered a haunted house")
    print("you hear sounds. you see a hallway. and there are stairs.")
    x = input("do you want to go up the stairs or down the hallway? (s/h): ")
    if x == "s":
        print("you decide to go up the stairs")
    elif x == "h":
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
    print("you get thrown in space and die. you lose")
elif n == "r":
    print("you decide to run away from the monster")
    print("you run away and escape.")
    print("you see a spaceship. do you want to go in the spaceship or keep running? (s/r): ")
    z = input()
    if z == "s":
        print("you go in the spaceship and escape. you win!")
    elif z == "r":
        print("you find a ghost")
        a = input("is the ghost friendly or scary? (f/s): ")
        if a == "f":
            print("the ghost is friendly and helps you escape.")
            print("you see a treasure chest. do you want to open it or leave it? (o/l): ")
            b = input()
            if b == "o":
                print("you open the treasure chest and find gold. you win!")
            elif b == "l":
                print("you don't open the treasure chest and leave it.")
                print("theres a broken clock on the ground. do you want to fix it or leave it? (f/l): ")
                c = input()
                if c == "f":
                    print("you fix the clock and it starts working.")
                    print("can you tell time? (y/n): ")
                    d = input()
                    if d == "y":
                        print("you can tell time and continue on your way.")
                        print("the clock is actually a time machine.")
                        print("do you want to go to the past or the future? (p/f): ")
                        e = input()
                        if e == "p":
                            print("you go to the past and meet your ancestors. you learn about your family history and gain wisdom. you win!")
                        elif e == "f":
                            print("you go to the future and see how the world has changed. you learn about new technologies and gain knowledge.")
                            print("but the monster from earlier is there with you!")
                            print("do you want to swim away in the ocean or ignore the monster")
                            f = input("(s/i): ")
                            if f == "s":
                                print("you swim away in the ocean but the monster is actaully is michael phelps and he eats you. you lose.")
                            elif f == "i":
                                print("you ignore the monster and continue on your way. you find a treasure chest and open it. you find gold and win!")
                    elif d == "n":
                        print("you really can't tell time. you lose.")
                elif c == "l":
                    print("you leave the clock and continue on your way.")
                    print("can you tell time? (y/n): ")
                    d = input()
                    if d == "y":
                        print("you can tell time and continue on your way.")
                    elif d == "n":
                        print("you really can't tell time. you lose.")
                    if d == "y":
                        print("you run into the monster again. he's very mad this time and runs at you and then eats you.")
                        print("the monster falls asleep with you in his stomach. you wake up and escape. you win!")
                else:
                    print("you're confused and don't know what to do")
            else:
                print("you're confused and don't know what to do")
        elif a == "s":
            print("the ghost is scary and kills you. you lose.")
        else:
            print("you're confused and don't know what to do")
    else:
        print("you're confused and don't know what to do")
else:
    print("you're confused and don't know what to do")
    print("the treasure chest is locked and you can't open it. you lose.")
