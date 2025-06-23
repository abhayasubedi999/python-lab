# 2_calculate_amount_returned_after_certain_time
principal = float(input("enter the principal: "))
rate = float(input("enter the rate: "))
time_in_years = float(input("enter the time: "))
intrest = (principal * time_in_years * rate) / 100
amount = intrest + principal
print("""the amount is :{amount}""".format(amount=amount))
