with open("Day03Input.txt") as file:
    data = file.read()

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
contents = [[each[:int(len(each)/2)],each[int(len(each)/2):]] for each in data.split('\n')]
groups = zip(*[iter(contents)]*3)

def find_item(elf):
    for i in elf[0]:
        if i in elf[1]:
            return letters.index(i) + 1

def find_badge(group):
    elves = [group[0][0]+group[0][1],group[1][0]+group[1][1],group[2][0]+group[2][1]]
    for i in elves[0]:
        if i in elves[1] and i in elves[2]:
            return letters.index(i)+1

priority_sum = 0
badge_sum = 0
for each_group in groups:
    for elf in each_group:
        priority_sum += find_item(elf)
    badge_sum += find_badge(each_group)


print(priority_sum)
# 7526 Too Low
# 7826
print(badge_sum)
# 2577