number_valid = 0
number_of_entries = 0

with open('day2data.txt') as f:
    lines = [line.rstrip() for line in f]

for x in lines:
  first=0
  second=0
  dashloc = x.find("-")
  spaceloc = x.find(" ")
  colloc = x.find(":")
  mincount=int(x[0:dashloc])-1
  maxcount=int(x[int(dashloc)+1:spaceloc])-1
  limitchar=x[int(spaceloc+1):int(colloc)]
  password = x[int(colloc+2):]
  if(password[mincount]==limitchar):
    first=1
  if(password[maxcount]==limitchar):
    second=1
  if ((first==1) or (second==1)):
    if(first !=second):
      number_valid+=1

print number_valid
#print toolow
#print toohigh
#print number_valid+toolow+toohigh
