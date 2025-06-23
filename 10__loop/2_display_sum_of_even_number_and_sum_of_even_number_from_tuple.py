tuple_a = (1, 4, 7, 12, 17, 20)
sum = 0
for num in tuple_a:
    if num % 2 == 0:
        print(num)
        sum = sum + num
print(sum)
