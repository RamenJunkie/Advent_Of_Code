with open("Day02_Input.txt") as file:
    boxes = file.read()

all_boxes = boxes.split("\n")
all_paper = []
sum_paper = 0
sum_ribbon = 0

for each in all_boxes:
    sides = [int(i) for i in each.split('x')]
    sides.sort()
    side_areas = [sides[0]*sides[1], sides[1]*sides[2], sides[2]*sides[0]]
    box_volume = sides[0]*sides[1]*sides[2]
    box_ribbon = sides[0]*2 + sides[1]*2
    box_total = side_areas[0]*3 + side_areas[1]*2 + side_areas[2]*2
    sum_paper += box_total
    sum_ribbon += box_ribbon+box_volume

print(sum_paper)
print(sum_ribbon)

# 1606483
# 3842356
