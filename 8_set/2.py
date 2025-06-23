# You are running stationary. Store items: book – 2 , pen - 3 , pencil - 1, marker - 1,staple-1 in a list.​

# Store unique items in a variable and display it​

# Display total unique items count​

# add sticky_notes to the unique item variable & display variable​

# Remove pen from variable & display it​

# Remove staple from variable & display it

stationary_item = ["book", "book", "pen", "pen", "pen", "pencil", "marker", "staple"]
unique_item = set(stationary_item)
print("unique items in the list:", unique_item)
print("total unique items in the list:", len(unique_item))
unique_item.add("sticky_notes")
print("list after adding sticky_notes:", unique_item)
unique_item.remove("pen")
print("after removing pen:", unique_item)
unique_item.remove("staple")
print("after removing staple:", unique_item)
