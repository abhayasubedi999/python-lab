# Write a function that counts number of character in string and returns result. Example: if arg is: Apple it has to return {‘A’: 1, ‘p’: 2. ‘l’: 1, ‘e’: 1}
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


Apple = input("enter the string: ")
result = count_characters("Apple")
print(result)
