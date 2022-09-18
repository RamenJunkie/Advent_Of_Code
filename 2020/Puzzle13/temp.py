with open('temp.txt') as f:
    lines = [line.rstrip() for line in f]

lines_array = lines[1].split(',')
times = []
counter=0
#First for sample Data Set day13datab.txt, second for real data
#multiplier=152600
multiplier=3
offsets=[]
busses=[]

for i in lines_array:
  if i != 'x':
    busses.append(i)
    offsets.append(lines_array.index(i))

#print busses
#print offsets

while (1):
  for i in offsets:
    times.append(((int(busses[0]))*multiplier)+i)

  #print times
  counter=1
  for j in busses[1:]:
    #print j
    if (times[counter]/float(j)).is_integer():
      counter+=1
    else:
      break
        
  #print times
  #print counter
  if counter == len(busses):
    break
  counter = 0
  times =[]
  multiplier+=1
  #print multiplier

print times
