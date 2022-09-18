with open('day13data.txt') as f:
    lines = [line.rstrip() for line in f]

time = int(lines[0])
raw = lines[1].split(',')
busses= [] 

for i in raw:
  if i != 'x':
    busses.append(int(i))

print time
print busses

for x in busses:
  bus_time=x*(round((float(time)/float(x))+.5))
  wait=bus_time-time
  print "For bus "+str(x)+": "+str(bus_time)+" and you will wait: "+str(wait)+" Ans: "+str(x*wait)

