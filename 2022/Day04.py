with open("Day04Input.txt") as file:
    data = file.read()

worklist = data.split("\n")

def check_range(elves):
    work = elves.split(",")
    elf1 = work[0].split("-")
    elf2 = work[1].split("-")
    for i in range(int(elf1[0]),int(elf1[1])+1):
        if i in range(int(elf2[0]),int(elf2[1])+1):
            return 1
    return 0

def check_overlap(elves):
    work = elves.split(",")
    elf1 = work[0].split("-")
    elf2 = work[1].split("-")
    if (int(elf1[0])-int(elf2[0]))*(int(elf1[1])-int(elf2[1])) > 0:
        return 0
    return 1

total = 0
range_total = 0
for each in worklist:
    total += check_overlap(each)
    range_total += check_range(each)

print(total)
#485
print(range_total)
# 658 LOW
#857