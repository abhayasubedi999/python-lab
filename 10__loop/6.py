# From the set {1, 4, 5, 7, 8, 11, 12, 15, 18}. Generate new list such that odd number is doubled and even number is tripled. It shouldn’t contain number 5 in the new list. Stop further calculation if you see number 15​

set = {1, 4, 5, 7, 8, 11, 12, 15, 18}
new_list = []
for i in set:
    if i % 2 == 0:
        new_list.append(i * 3)
    else:
        new_list.append(i * 2)
    if i == 15:
        break

print(new_list)
