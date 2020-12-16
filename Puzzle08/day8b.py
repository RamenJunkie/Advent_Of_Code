def solver(accumulator, location, commands_executed, switcher):

  while(True):
    if lines[location] == "":
      print accumulator
      return False

    command = lines[location][:3]
    amount = int(lines[location][4:])

    #print command
    #print amount
  
    if switcher==1 and command == 'jmp':
      switcher = 0
      command = 'nop'
    if switcher==1 and command == 'nop':
      switcher = 0
      command = 'jmp'


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

  return True


with open('day8data.txt') as f:
    lines = [line.rstrip() for line in f]


accumulator=0
location=0
breaker = True
commands_executed=[]

while(breaker):
  while(True):
    command = lines[location][:3]
    amount = int(lines[location][4:])

    #print command
    #print amount
    if command == "":
      print accumulator

    if command == 'acc':
      accumulator+=amount
      location+=1
    if command == 'jmp':
      breaker = solver(accumulator,location, commands_executed, 1)
      location+=amount
    if command == 'nop':
      breaker = solver(accumulator,location, commands_executed, 1)
      location+=1

    if location not in commands_executed:
      commands_executed.append(location)
    else:
      break
    #print commands_executed



