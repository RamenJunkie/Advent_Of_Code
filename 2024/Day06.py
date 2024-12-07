import time
import os

with open("Day06Input.txt") as file:
    data = file.read()

lines = data.split("\n")
lines.pop()

guard = [0,0,0]
grid = []
guard_active = True
total = 0
total2 = 0
distances = []
cur_steps = 0

for each in lines:
  if "^" in each:
    guard[0] = each.index("^")
    guard[1] = lines.index(each)
#  print(guard)
  grid.append(list(each))

def print_grid(thegrid):
  for each in thegrid:
    print("".join(each))

#print_grid(grid)

def move_guard(thegrid, guard_pos):
# 0 - North, 1 - East, 2 - South, 3 - West
# Defind in guard[2]
# guard[0] = x coord (across rows), guard [1] = y coord (up and down lines)
  step = 1
  if (thegrid[guard_pos[1]-1][guard_pos[0]] != "#") and guard_pos[2] == 0:
    thegrid[guard_pos[1]][guard_pos[0]] = "X"
    thegrid[guard_pos[1]-1][guard_pos[0]] = "^"
    guard_pos[1] = guard_pos[1]-1
  elif (thegrid[guard_pos[1]][guard_pos[0]+1] != "#") and guard_pos[2] == 1:
    thegrid[guard_pos[1]][guard_pos[0]] = "X"
    thegrid[guard_pos[1]][guard_pos[0]+1] = "^"
    guard_pos[0] = guard_pos[0]+1
  elif (thegrid[guard_pos[1]+1][guard_pos[0]] != "#") and guard_pos[2] == 2:
    thegrid[guard_pos[1]][guard_pos[0]] = "X"
    thegrid[guard_pos[1]+1][guard_pos[0]] = "^"
    guard_pos[1] = guard_pos[1]+1
  elif (thegrid[guard_pos[1]][guard_pos[0]-1] != "#") and guard_pos[2] == 3:
    thegrid[guard_pos[1]][guard_pos[0]] = "X"
    thegrid[guard_pos[1]][guard_pos[0]-1] = "^"
    guard_pos[0] = guard_pos[0]-1
  else:
    guard_pos[2] = (guard_pos[2]+1) % 4
    step = 0
#  print(guard_pos)

  return thegrid, guard_pos, step


while guard_active:
  this_step = 0
  grid, guard, this_step = move_guard(grid, guard)
  if this_step == 0:
    distances.append(cur_steps)
    cur_steps = 0
  else:
    cur_steps += this_step
# Optionally Print the Map
#  print_grid(grid)
#  time.sleep(.001)
#  os.system('clear')
#  print(guard)
#  print(len(grid)-1)
  if guard[1] >= len(grid)-1 or guard[1] <= 0 or guard[0] >= len(grid[0])-1 or guard[0] <= 0:
    grid[guard[1]][guard[0]] = "X"
    guard_active = False
    print("The guard has left the area!")

for each in grid:
  total+= each.count("X")

#Print the final grid for fun
#print_grid(grid)

print(distances)

print(total)
# 5318
print(total2)
