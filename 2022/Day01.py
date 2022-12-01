with open("Day01Input.txt") as file:
    calories = file.read()

calories = calories.replace("\n"," ")
elves = [each.split(" ") for each in calories.split("  ")]

totals = []
for each in elves:
    total = 0
    for i in each:
        total += int(i)
    totals.append(total)

totals.sort(reverse=True)
print(totals[0]+totals[1]+totals[2])
# 69177
#207456