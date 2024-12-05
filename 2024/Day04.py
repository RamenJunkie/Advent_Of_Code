with open("Day04Input.txt") as file:
    data = file.read()

import numpy as np

lines = data.split("\n")
lines.pop()
diaglines = []
total = 0
total2 = 0
grid = []
gridsize = len(lines[1])

for each in lines:
  grid.append(list(each))

a = np.array(grid)

rotated_a = np.rot90(a)

# Part 2 visa the shitty Brute Force Way
for i in range(len(lines)-1):
  for j in range(len(lines[i])-1):
    if i != 0 and j != 0:
#      print(lines[i][j])
      if lines[i][j] == 'A':
        check1 = lines[i+1][j+1]+lines[i][j]+lines[i-1][j-1]
        check2 = lines[i+1][j-1]+lines[i][j]+lines[i-1][j+1]
        if (check1 == "MAS" or check1 == "SAM") and (check2 == "MAS" or check2 == "SAM"):
          total2 += 1
#          print(check1)
#          print(check2)
#          print("Match")
        else:
          print(check1)
          print(check2)
          print(lines[i-1])
          print(lines[i])
          print(lines[i+1])
          print("------")


# Rotate the array 90 and add the lines to our overall lines
for row in rotated_a:
#  print(''.join(row))
  lines.append(''.join(row))

# Rotate the array diagonally
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))
#######################################################################################################


## Join the rotated numpy array and add it to our total lines to ge the diagonals
for n in diags:
  new_string = f"{''.join(str(i) for i in n.tolist())}" 
#  print(new_string)
#  padding = int((gridsize - len(new_string))/2)
#  diag_string = ('o'*padding) + new_string + ('o'*padding)
#  if len(diag_string) % 2 == 0:
#    diag_string = diag_string[:-1]
  lines.append(new_string)
#  diaglines.append(diag_string)

#print(diaglines)

# Count up for Part 1
for each in lines:
#  print(each)
  total+= each.count("XMAS")
  total+= each.count("SAMX")

#dlist1 = diaglines[:len(diaglines)//2]
#dlist2 = diaglines[len(diaglines)//2:]





# Print Totals
print(total)
print(total2)

#1771 = Too low
#2003 = Too Low
#Part 1 - 2427

#3085 Too High
#1312 Too Low
#1900 - Part 2
