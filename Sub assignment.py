# Gabriel Hart
# Computer Programming
# In-Class Sub Assignment

# Playlist Builder

# Part 1: Build the List
playlist = ["Hotel California", "Stairway to Heaven", "Photograph", "All Along the Watchtower"]

new_song = input("Enter a song to add: ")
new_song = new_song.strip().title()

playlist.append(new_song)

# Part 2: Modify it
print("Number of songs:", len(playlist))

playlist.insert(0, "Free Bird")

# Remove a song using .remove()
playlist.remove("Photograph")

# Delete another song using del
del playlist[2]

# Print playlist alphabetically without changing the original
print("Alphabetical order:", sorted(playlist))

# Permanently sort the playlist
playlist.sort()

# Reverse the playlist
playlist.reverse()

# Part 3: Check It & Show It Off
print("Photograph" in playlist)

for song in playlist:
    print(song.upper())

# Part 4: Final Boss - for i in range()
print("Numbered Tracklist:")

for i in range(len(playlist)):
    print(i + 1, playlist[i])