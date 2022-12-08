n = [1, 1, 2, 3, 4, 4, 4]

dicte = {}
for i in range(0, len(n)):
    if n[i] not in dicte.keys():
        dicte[n[i]] = 1
    else:
        dicte[n[i]] = dicte[n[i]] + 1

print(n)
for item in dicte:
    if dicte[item] == 1:
        print(item, end=" ")
print()