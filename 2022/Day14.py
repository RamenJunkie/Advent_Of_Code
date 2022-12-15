import math

with open("Day14Input.txt") as file:
    data = file.read()

lines = data.split('\n')

def draw_cave(lx, ly):
    grid = []
    line = []
    floor = []
    for i in range(0,lx*2):
        line.append(".")
    for j in range(0,ly+2):
        grid.append(line.copy())
    for i in range(0, lx * 2):
        floor.append("#")
    grid.append(floor)
    return grid

def draw_rocks(rocks,cave):
    for rockline in rocks:
        for i in range(len(rockline)-1):
            startx = int(rockline[i][0])
            starty = int(rockline[i][1])
            endx = int(rockline[i+1][0])
            endy = int(rockline[i+1][1])
            if starty == endy:
                xrange = sorted([startx, endx])
                for horiz in range(xrange[0],xrange[1]+1):
                    cave[starty][horiz] = "#"
            if startx == endx:
                yrange = sorted([starty, endy])
                for vert in range(yrange[0], yrange[1]+1):
                    cave[vert][startx] = "#"
    return cave

def show_cave():
    for i in cave:
        print(" ".join(i))

smallest_x = 100000
smallest_y = 100000
largest_x = -1
largest_y = -1
rocks = []
for line in lines:
    sets = line.split(" -> ")
    r = []
    for n in sets:
        nsplit = n.split(",")
        if int(nsplit[0]) < smallest_x:
            smallest_x = int(nsplit[0])
        if int(nsplit[1]) < smallest_y:
            smallest_y = int(nsplit[1])
        if int(nsplit[0]) > largest_x:
            largest_x = int(nsplit[0])
        if int(nsplit[1]) > largest_y:
            largest_y = int(nsplit[1])
        r.append(n.split(","))
    rocks.append(r)

# print(f"{smallest_x} {largest_x} | {smallest_y} {largest_y}")
# print(rocks)

cave = draw_cave(largest_x,largest_y)
# show_cave()
rocky_cave = draw_rocks(rocks,cave)

sand_start = 500
rocky_cave[0][sand_start] = "+"

captured = True
sand_count = 0
while captured:
    sand_pos = [0,sand_start]

    sand_drop = True
    while sand_drop:
        if sand_pos[0] > len(rocky_cave)-3:
            captured = False
            sand_drop = False
        elif rocky_cave[sand_pos[0]+1][sand_pos[1]] == ".":
            sand_pos[0] += 1
        elif rocky_cave[sand_pos[0]+1][sand_pos[1]-1] == ".":
                sand_pos[0] += 1
                sand_pos[1] -= 1
        elif rocky_cave[sand_pos[0]+1][sand_pos[1]+1] == ".":
                sand_pos[0] += 1
                sand_pos[1] += 1
        else:
            sand_count+=1
            rocky_cave[sand_pos[0]][sand_pos[1]] = "O"
            sand_drop = False

    # show_cave()

print(sand_count)
show_cave()
# Part 1 = 728

#### RESUME FOR PART 2 #####
captured = True
while captured:
    sand_pos = [0,sand_start]

    sand_drop = True
    while sand_drop:
        if sand_pos[0] > len(rocky_cave)-1:
            captured = False
            sand_drop = False
        elif rocky_cave[sand_pos[0]+1][sand_pos[1]] == ".":
            sand_pos[0] += 1
        elif rocky_cave[sand_pos[0]+1][sand_pos[1]-1] == ".":
                sand_pos[0] += 1
                sand_pos[1] -= 1
        elif rocky_cave[sand_pos[0]+1][sand_pos[1]+1] == ".":
                sand_pos[0] += 1
                sand_pos[1] += 1
        else:
            if sand_pos == [0,sand_start]:
                captured = False
            else:
                rocky_cave[sand_pos[0]][sand_pos[1]] = "O"
            sand_count+=1
            sand_drop = False

print(sand_count)

show_cave()
# Part 2 = 27623