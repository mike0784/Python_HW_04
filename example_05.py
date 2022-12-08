
import re
file1 = "c:/Users/Mike84/Desktop/Proba/HW_004/ex1.txt"
file2 = "c:/Users/Mike84/Desktop/Proba/HW_004/ex2.txt"
fileResult = "c:/Users/Mike84/Desktop/Proba/HW_004/result_05.txt"

text1 = ""
text2 = ""

def readFile(file):
    f = open(file, "r")
    text = f.readline()
    f.close()
    return text

text1 = readFile(file1)
text2 = readFile(file2)

var1 = text1.replace(" + ", " = ").split(" = ")
var2 = text2.replace(" + ", " = ").split(" = ")

def parsing(item):
    rs = []
    if "x**" in item:
        rs = re.findall(r'[\d]+', item)
        return rs
    elif "*x" in item:
        rs = re.findall(r'[\d]+', item)
        rs.append("1")
        return rs
    else:
        rs = re.findall(r'[\d]+', item)
        rs.append("0")
        return rs

ss1 = {int(parsing(var1[x])[1]) : int(parsing(var1[x])[0]) for x in range(0, len(var1)-1)}
ss2 = {int(parsing(var2[x])[1]) : int(parsing(var2[x])[0]) for x in range(0, len(var2)-1)}
result = {**ss1, **ss2}

for i in result:
    if i in ss2 and i in ss1:
        result[i] = result[i] + ss1[i]

text = ""
for item in result:
    if item > 1:
        text = text + str(result[item]) + "(x**" + str(item)+ ") + "
    if item == 1:
        text = text + str(result[item]) + "*x + "
    if item == 0:
        text = text + str(result[item]) + " = 0"

f = open(fileResult, "w")
f.write(text)
f.close()