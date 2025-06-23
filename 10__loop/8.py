# Store list of fruit on a list. Generate new list such that If fruit start with a/A then convert to upper case else convert to lower case (for & comprehension)

fruit_list = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [
    fruit.upper() if fruit.startswith("a") or fruit.startswith("A") else fruit.lower()
    for fruit in fruit_list
]
print(new_list)
