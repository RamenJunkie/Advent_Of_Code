with open("Day01Input.txt") as file:
    data = file.read()

sets = [each.split("   ") for each in data.split("\n")]
sets.pop()

list1 = []
list2 = []

for each in sets:
   list1.append(int(each[0]))
   list2.append(int(each[1]))

list1.sort()
list2.sort()

total = 0
total2 = 0
for i in range(len(list1)):
    total += abs(list1[i]-list2[i])
    total2 += list1[i]*list2.count(list1[i])

print(total)
print(total2)

#1666427
#24316233

