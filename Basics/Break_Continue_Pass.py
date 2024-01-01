#!/usr/bin/python3
# Break Continue Pass
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 17, 19]
# continue
for num in my_numbers:
    if num == 15:
        continue
    print(num)
print("#" * 50)
# Break
for num in my_numbers:
    print(num)
    if num == 15:
        break
print("#" * 50)
# pass
for num in my_numbers:
    if num == 10:
        pass
    print(num)
