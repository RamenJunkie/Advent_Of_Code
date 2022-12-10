with open("Day09Input.txt") as file:
    data = file.read()

moves = data.split('\n')

positions = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
head_pos = [0,0]
tail_pos = [0,0]

head_moves = [head_pos]
tail_moves = [tail_pos]
long_tail_moves = [positions[len(positions)-1]]

tail_counter = 1
long_tail_counter = 1

def move_pos(a,b):
    if a - b > 0:
        return b+1
    if a - b < 0:
        return b-1
    return b

def move_head(dir,hpos):
    if dir == "R":
        return [hpos[0]+1,hpos[1]]
    if dir == "L":
        return [hpos[0]-1,hpos[1]]
    if dir == "U":
        return [hpos[0],hpos[1]+1]
    if dir == "D":
        return [hpos[0],hpos[1]-1]
    return pos

def move_tail(hpos,tpos):
    xpos = tpos[0]
    ypos = tpos[1]
    if abs(hpos[0]-xpos) > 1 and abs(hpos[1]-ypos) > 1:
        xpos = move_pos(hpos[0], xpos)
        ypos = move_pos(hpos[1], ypos)
    if abs(hpos[0]-xpos) > 1:
        ypos = hpos[1]
        xpos = move_pos(hpos[0], xpos)
    if abs(hpos[1]-ypos) > 1:
        xpos = hpos[0]
        ypos = move_pos(hpos[1], ypos)
    return [xpos, ypos]

# Part 1
for move in moves:
    turn = move.split(" ")
    for i in range(int(turn[1])):
        head_pos = move_head(turn[0], head_pos)
        head_moves.append(head_pos)
        tail_pos = move_tail(head_pos, tail_pos)
        if tail_pos not in tail_moves:
            tail_counter += 1
        tail_moves.append(tail_pos)

# Part 2
for move in moves:
    turn = move.split(" ")
    for i in range(int(turn[1])):
        positions[0] = move_head(turn[0], positions[0])
        for i in range(1,len(positions)):
            positions[i] = move_tail(positions[i-1], positions[i])
        if positions[len(positions)-1] not in long_tail_moves:
            long_tail_counter += 1
        long_tail_moves.append(positions[len(positions)-1])



# print(head_moves)
# print(tail_moves)
print(tail_counter)
#5902

#print(long_tail_moves)
print(long_tail_counter)
# high 11271
# high 2448
# low 2395

## 2445