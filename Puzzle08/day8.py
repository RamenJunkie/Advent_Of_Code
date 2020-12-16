with open('day8data.txt') as f:
    lines = [line.rstrip() for line in f]


accumulator=0
location=0
commands_executed=[]

while(location<=len(lines)):
  command = lines[location][:3]
  amount = int(lines[location][4:])

  #print command
  #print amount
  
  if command == 'acc':
    accumulator+=amount
    location+=1
  if command == 'jmp':
    location+=amount
  if command == 'nop':
    location+=1
  
  if location not in commands_executed:
    commands_executed.append(location)
  else:
    break
  #print commands_executed



print accumulator
