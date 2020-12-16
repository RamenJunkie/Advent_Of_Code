with open('day9data.txt') as f:
    lines = [line.rstrip() for line in f]

position = 25

while(True):
  valid_nums=lines[position-25:position]
  valid = 0
  current = int(lines[position])
  #print current
  for i in valid_nums:
    check = current - int(i)
    #print str(current) +"-"+ i +"="+str(check)
    if str(check) in valid_nums:
      #print check
      valid=1
  #print valid
  if valid == 1:
    #print position
    position+=1
  else: 
    break
      
print current

start=0
position=start
total=0
sum_array=[]

while(total != current):
  if total < current:
    total+=int(lines[position])
    position+=1
    #print total
  else:
    start+=1
    position=start
    total=0

for i in lines[start:position]:
  sum_array.append(int(i))

sum_array = sorted(sum_array)

print sum_array
print int(sum_array[0])+int(sum_array[-1])

