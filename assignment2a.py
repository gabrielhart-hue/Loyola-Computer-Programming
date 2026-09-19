# Hart, Gabriel
# Computer Programming, p4
# Assignment #2a: Homework 2
# September 18, 2026 

# 1. Hobbies
hobbies = ["playing guitar", "playing saxophone", "listening to music", "gaming", "watching movies"]

print("Hobbies:", hobbies)
print("Length of hobbies:", len(hobbies))
print("Index 2:", hobbies[2])
print("First hobby:", hobbies[0])


# 2. Create a list of 100 "hello!"
hello_list = ["hello!"] * 100
print("100 hellos:", hello_list)


# 3. Combine list1 and list2 into list3
list1 = ["pumpkin", "halloween", "jack-o-lantern", "spooky"]
list2 = ["christmas", "new year", "holiday", "santa"]

list3 = list1 + list2
print("list3:", list3)


# 4. Foods
favFoods = ["pizza", "tacos", "hamburgers", "pasta", "steak"]

print("Length of favFoods:", len(favFoods))
print("Index 2:", favFoods[2])
print("Index 1 using negative indexing:", favFoods[-4])

favFoods.append("Gabriel")
favFoods.insert(2, 17)
favFoods.remove("steak")

print("Final food list:", favFoods)


# 5. Counting to Twenty
print("Counting to 20:")
for number in range(1, 21):
    print(number)


# 6. Odd Numbers
odd_numbers = list(range(1, 21, 2))

print("Odd numbers:")
for number in odd_numbers:
    print(number)


# 7. Animals
animals = ["dog", "cat", "rabbit"]

for animal in animals:
    print(f"A {animal} would make a great pet.")

print("Any of these animals would make a great pet!")


# 8. Guest List
guests = ["Jimmy Page", "Jimi Hendrix", "David Gilmour"]

for guest in guests:
    print(f"{guest}, I would like to invite you to dinner!")


# 9. Changing Guest List
print(f"{guests[1]} can't make it to dinner.")

guests[1] = "Eric Clapton"

print("Updated invitations:")
for guest in guests:
    print(f"{guest}, I would like to invite you to dinner!")