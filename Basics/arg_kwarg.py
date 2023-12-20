#!/usr/bin/python3
def my_sum(a, b, *args, option=True):
    result = 0
    for x in args:
        result += x
    if option:
        return a + b + result
    else:
        return 0


print(my_sum(1, 2, 3, 4, 5, option=False))  # This will now print 0
# -------------------------------------------------------------------------
print("=" * 50)


def make_sentence(**kwargs):
    result = ""
    for x in kwargs.values():
        result += x
    return result


print(make_sentence(a="Meow", b="me"))
print("=" * 50)
# --------------------------------------------------------


def make_sen(**kwargs):
    result = ""
    for x in kwargs:
        result += x
    return result


print(make_sen(a="Meow", b="me"))
print("=" * 50)
# ------------------------------------------------------------


def human_Details(**kwargs):
    result = ""
    for key, value in kwargs.items():
        print(f"{key}, {value}")


human_Details(name="am7", age=36, job="Meow")
print("=" * 50)


# --------------------------------------------------------------
def print_args(x, y, args, option=True, **kwargs):
    print(x, y)
    print(args)
    print(option)
    print(kwargs.values())
    print(kwargs.items())


print_args(1, 2, "3 is arg", "4 is arg", channel="Meow")
