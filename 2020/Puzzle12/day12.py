def rotator(degrees, current):
  change = degrees+current
  if change < 0:
    change = change+360
  if change >=360:
    change = change-360
  #print change
  return change  
 

with open('day12data.txt') as f:
    lines = [line.rstrip() for line in f]

xpos=0
ypos=0
#0 is East
orientation=0
cardinals = ["E","S","W","N"]

for i in lines:
  #print i
  next_orient=i[0]
  amount=int(i[1:])

  print "Ship Moves: "+next_orient+" direction "+str(amount)+" times"

  if next_orient == "L":
    orientation = rotator(-amount,orientation)
  if next_orient == "R":
    orientation = rotator(amount,orientation)
  if next_orient == "F":
    next_orient = cardinals[(orientation/90)]
  #print amount
  #print next_orient
  #print cardinals[(orientation/90)]
  if next_orient == "N":
    xpos=xpos+amount
  if next_orient == "S":
    xpos=xpos-amount
  if next_orient == "E":
    ypos=ypos+amount
  if next_orient == "W":
    ypos=ypos-amount


  print xpos
  print ypos
print abs(xpos)+abs(ypos)
