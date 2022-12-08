import math
n = int(input("Введите число: "))
result = []

def simple_num(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            result.append(i)
            num = num / i
    if num > 2:
        result.append(int(num))

simple_num(n)
print("n=" + str(n) + "  " + str(result))