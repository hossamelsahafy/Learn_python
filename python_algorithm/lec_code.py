#!/usr/bin/python3
def exp1(a, b):
    ans = 1
    while b > 0:
        ans *= a
        b -= 1
    return ans


print(exp1(2, 3))
