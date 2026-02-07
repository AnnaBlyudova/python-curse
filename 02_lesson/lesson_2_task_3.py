
import math


def square(a):
    s = a * a
    if a != int(a):
        return math.ceil(s)
    return s


a = float(input("Введите длину стороны квадрата в см: "))
print(square(a))
