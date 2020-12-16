def split_str(s):
  return [ch for ch in s]

with open('day3datab.txt') as f:
    lines = [line.rstrip() for line in f]

trees = 0
slopex = 1
slopey = 2
posx=0
posy=0
line_loop=len(lines[1])
distance=len(lines)-2
#print distance

while (posy<distance):
  #print trees
  posx=posx+slopex
  posy=posy+slopey
  #print str(posy)+"/"+str(distance)
  if(posx>=line_loop):
    posx=posx-line_loop
  #print str(posx)+","+str(posy)
  print str(lines[posy][posx])
  whatis=str(lines[posy][posx])
  if (whatis == "T"):
    trees+=1
  print trees
