with open('day9data.txt') as f:
    lines = [line.rstrip() for line in f]

position = 25

while(True):
  valid_nums=lines[position-25:position]
  valid = 0
  current = int(lines[position])
  print current
  for i in valid_nums:
    check = current - int(i)
    #print str(current) +"-"+ i +"="+str(check)
    if str(check) in valid_nums:
      #print check
      valid=1
  print valid
  if valid == 1:
    print position
    position+=1
  else: 
    print current
    break
      
