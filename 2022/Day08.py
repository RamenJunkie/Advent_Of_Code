with open("Day08Input.txt") as file:
    data = file.read()

tree_grid = data.split('\n')

leny = len(tree_grid)-1

tall_total = 0

def check_west(x,y):
    for each in range(0, x):
        if tree_grid[y][x] <= tree_grid[y][each]:
            return False
    return True

def check_east(x,y):
    for each in range(x+1,len(tree_grid)):
        if tree_grid[y][x] <= tree_grid[y][each]:
            return False
    return True

def check_north(x,y):
    for each in range(0, y):
        if tree_grid[y][x] <= tree_grid[each][x]:
            return False
    return True

def check_south(x,y):
    for each in range(y + 1, len(tree_grid)):
        if tree_grid[y][x] <= tree_grid[each][x]:
            return False
    return True

def scenic_score(x,y):
    east_score = 0
    west_score = 0
    north_score = 0
    south_score = 0

    for i in range(x+1,len(tree_grid)):
        if tree_grid[y][i] < tree_grid[y][x]:
            east_score += 1
        else:
            east_score += 1
            break
    for i in range(y+1, len(tree_grid)):
        if tree_grid[i][x] < tree_grid[y][x]:
            # print(tree_grid[i][x] + " " + tree_grid[y][x])
            south_score += 1
        else:
            # print(tree_grid[i][x] + " " + tree_grid[y][x])
            south_score += 1
            break
    for i in reversed(range(0, x)):
        if tree_grid[y][i] < tree_grid[y][x]:
            # print(tree_grid[y][i] + " " + tree_grid[y][x])
            west_score += 1
        else:
            # print(tree_grid[y][i] + " " + tree_grid[y][x])
            west_score += 1
            break
    for i in reversed(range(0, y)):
        if tree_grid[i][x] < tree_grid[y][x]:
            # print(tree_grid[i][x] + " " + tree_grid[y][x])
            north_score += 1
        else:
            # print(tree_grid[i][x] + " " + tree_grid[y][x])
            north_score += 1
            break
    # print(f"{north_score} * {west_score} * {east_score} * {south_score}")
    return east_score * south_score * west_score * north_score

high_score = 0
for y in range(1, len(tree_grid[0])-1):
    for x in range(1, len(tree_grid)-1):
        if check_west(x,y) or check_east(x,y) or check_north(x,y) or check_south(x,y):
            tall_total += 1
        score = scenic_score(x,y)
        if score > high_score:
            high_score = score


print(tall_total+((len(tree_grid))*4)-4)
# 2007 High
# 1991 High
# 1859 Correct
print(high_score)
# 332640