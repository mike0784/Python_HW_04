import math
d = input("Введите точность числа: ")

dn = len(d.split(".")[1])
print("Ответ: " + str(round(math.pi, dn)))