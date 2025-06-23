costumer_name = input("enter your name: ")
time = int(input("enter current time: "))
if 5 <= time <= 11:
    print(f"good morning {costumer_name}")
elif 12 <= time <= 17:
    print(f"good afternoon {costumer_name}")
elif 18 <= time <= 20:
    print(f"good evening {costumer_name}")
elif 20 <= time <= 23 or 0 <= time <= 4:
    print(f"good night {costumer_name}")
else:
    print(f"time is not valid {costumer_name}")
