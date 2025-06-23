# You are running stationary. Store items: book – 2 , pen - 3 , pencil - 1, marker - 1 in a list.​
# Display this list. Add pen at end of list & display the list again​
# Count number of pencil on list & display it​
# Add sticky_notes in list at third position & display the list​
# Remove pencil from list and display list​
# Remove item from 2nd position. Display removed item & the list​
# Remove item from 1st & 2nd position. Display removed items & the list​
# Display total items in the list.​
# Display all items of list separated by comma ​
# Display the items from position 1 to 3 from list.​
# Display on which position the pen lies in the list. Also display item on 3rd position​

stationary_item = ["book", "book", "pen", "pen", "pen", "pencil", "marker"]
print("initial list:", stationary_item)
stationary_item.append("pen")
pencil_count = stationary_item.count("pencil")
print("number of pencil in the list:", pencil_count)
stationary_item.insert(2, "sticky_notes")
print("list after adding sticky_notes:", stationary_item)
stationary_item.remove("pencil")
print("after removing pencil:", stationary_item)
removed_item = stationary_item.pop(1)
print(f"removed item from second position:{removed_item}")
print("list after removal:", stationary_item)
removed_item1 = stationary_item.pop(0)
removed_item2 = stationary_item.pop(0)
print("total items in the list:", len(stationary_item))
print(", ".join(stationary_item))
print(stationary_item[0:3])
print(stationary_item.index("pen"))
