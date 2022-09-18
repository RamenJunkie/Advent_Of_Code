def rotator(degrees, current):
  global xpos
  global ypos
  change = degrees+current
  if change < 0:
    change = change+360
  if change >=360:
    change = change-360
  #print change
  #return change
  if change == 90 or change == 270:
   temp=xpos
   xpos=-ypos
   ypos=temp
  if change == 180 or change == 270:
   xpos=-xpos
   ypos=-ypos
 

with open('day12data.txt') as f:
    lines = [line.rstrip() for line in f]

xpos=1
ypos=10
shipx=0
shipy=0
#0 is East
orientation=0
cardinals = ["E","S","W","N"]

for i in lines:
  #print i
  next_orient=i[0]
  amount=int(i[1:])

  if next_orient == "L":
    rotator(-amount,orientation)
  if next_orient == "R":
    rotator(amount,orientation)
  if next_orient == "N":
    xpos=xpos+amount
  if next_orient == "S":
    xpos=xpos-amount
  if next_orient == "E":
    ypos=ypos+amount
  if next_orient == "W":
    ypos=ypos-amount
  if next_orient == "F":
    shipx=shipx+(xpos)*amount
    shipy=shipy+(ypos)*amount

  print "Ship Moves: "+next_orient+" direction "+str(amount)+" times"

  print "Beacon: "+str(xpos)+"E/W "+str(ypos)+"N/S"
  print "Ship: "+str(shipx)+"E/W "+str(shipy)+"N/S"
print abs(shipx)+abs(shipy)
print shipx
print shipy
