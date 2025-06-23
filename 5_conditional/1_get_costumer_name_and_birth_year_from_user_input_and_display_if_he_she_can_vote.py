costumer_name = input("enter the costumer name: ")
birth_year = int(input("enter the birth year: "))
CURRENT_YEAR = 2082
age = CURRENT_YEAR - birth_year
if age > 18:
    print("you are eligible for voting:")
else:
    print("you are not eligible for voting:")
