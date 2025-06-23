costumer_name = input("enter the costumer name: ")
birth_year = int(input("enter your birth year: "))
current_year = 2082
age = current_year - birth_year
if 18 <= age <= 70:
    print("you can have license")
else:
    print("you cannot have license")
