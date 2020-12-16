with open('day13data.txt') as f:
    lines = [line.rstrip() for line in f]

def find_largest(array,large):
  largest=0
  for i in array:
    if large > i > largest:
      largest = i
  return largest

lines_array = lines[1].split(',')
times = []
counter=0
#First for sample Data Set day13datab.txt, second for real data
#multiplier=152600
multiplier=91550886066360
offsets=[]
busses=[]

#strip out non existent busses and add indexes to an array
for i in lines_array:
  if i != 'x':
    busses.append(int(i))
    offsets.append(lines_array.index(i))

#sort both lists based on busses list
large=1000000
while(1):
  largest=find_largest(busses,large)
  if largest ==0:
    break

  #print largest
  large = largest
  move = busses.index(largest)
  busses.pop(move)
  busses.append(largest)
  move_off=offsets.pop(move)
  offsets.append(move_off)

#print busses
#print offsets

while (1):
  for i in offsets:
    times.append(((int(busses[-1]))*multiplier)+i)

  print times
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

print busses
print times
