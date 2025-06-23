balance = 2000
amount_to_withdraw = int(input("enter amount to withdraw: "))

if amount_to_withdraw < balance:
    balance = balance - amount_to_withdraw
    print(
        f"{amount_to_withdraw} is withdrawer from your account and your remaining balance is {balance} "
    )
else:
    print("insufficient balance")

print(balance)
