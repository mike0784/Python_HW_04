import random as rnd
n = int(input("Введите степень k: "))
text = ""

def formatText(num):
    text = ""
    if n - i > 1:
        text = "(x**" + str(n - i)+ ") + "
    if n - i == 1:
        text = "*x + "
    if n - i == 0:
        text = " = 0"
        
    return text

for i in range(0, n + 1):
    k = rnd.randint(0, 100)
    if k != 0:
        text = text + str(k) + formatText(i)
print(text)
f = open("c:/Users/Mike84/Desktop/Proba/HW_004/Result.txt", 'w')
f.writelines("k=" + str(n) + "   " + text)
f.close()