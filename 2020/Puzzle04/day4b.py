with open('day4data.txt') as f:
    lines = [line.rstrip() for line in f]

buildline = ''
valid_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
valid_eyes = ['amb','blu','brn','gry','grn','hzl','oth']
valid_color = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
passengers = []
num_fields = len(valid_fields)
#print num_fields
valid_passports=0
num_valid=0
is_valid=0

for line in lines:
  if line != '':
    buildline+=' '+line
  else:
    #print buildline
    linearray=buildline.split(' ')
    linearray=linearray[1:]
    for x in linearray:
      if(x[0:3] == "byr" and len(x[4:]) == 4):
        if 1920<=int(x[4:])<=2002:
          num_valid+=1  
        
      if(x[0:3] == "iyr" and len(x[4:]) == 4):
        if 2010<=int(x[4:])<=2020:
          num_valid+=1

      if(x[0:3] == "eyr" and len(x[4:]) == 4):
        if 2020<=int(x[4:])<=2030:
          num_valid+=1

      if(x[0:3] == "ecl"):
        if x[4:] in valid_eyes:
          num_valid+=1

      if(x[0:3] == "pid") and (len(x[4:]) == 9):
          num_valid+=1

      if(x[0:3] == "hgt" and x[-2:] == 'cm'):
          if 150<=int(x[4:-2]) <= 193:
            num_valid+=1 
      if(x[0:3] == "hgt" and x[-2:] == 'in'):
          if 59<=int(x[4:-2]) <= 76:
            num_valid+=1

      if(x[0:3] == 'hcl' and len(x[4:]) == 7):
          #print x[4:]
          #for n in x[5:]:
           # if n not in valid_color:
            #  is_valid=0
          num_valid+=1

    if num_valid == num_fields:
      valid_passports+=1
    
    #passengers.append(linearray)
    is_valid = 0
    num_valid = 0
    buildline = ''

#print passengers
print valid_passports
