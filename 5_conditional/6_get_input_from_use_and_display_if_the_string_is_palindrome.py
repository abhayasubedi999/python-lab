string = input("enter any word : ")
reversed_string = string[::-1]
if string == reversed_string:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome")
