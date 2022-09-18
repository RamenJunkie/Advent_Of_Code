with open('day4data.txt') as f:
    lines = [line.rstrip() for line in f]

buildline = ''
valid_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
passengers = []
num_fields = len(valid_fields)
#print num_fields
valid_passports=0
num_valid=0

for line in lines:
  if line != '':
    buildline+=' '+line
  else:
    #print buildline
    linearray=buildline.split(' ')
    linearray=linearray[1:]
    for x in linearray:
      #print x[0:3]
      if(x[0:3] in valid_fields):
	num_valid+=1
    #print linearray
    if num_valid == num_fields:
      valid_passports+=1
    
    #passengers.append(linearray)
    num_valid = 0
    buildline = ''

#print passengers
print valid_passports
