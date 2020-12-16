number_valid = 0
toolow = 0
toohigh = 0
number_of_entries = 0

with open('day2data.txt') as f:
    lines = [line.rstrip() for line in f]

for x in lines:
  dashloc = x.find("-")
  spaceloc = x.find(" ")
  colloc = x.find(":")
  mincount=int(x[0:dashloc])
  maxcount=int(x[int(dashloc)+1:spaceloc])
  limitchar=x[int(spaceloc+1):int(colloc)]
  password = x[int(colloc+2):]
  checkvalue = int(password.count(limitchar))
  if(mincount <= checkvalue <= maxcount):
    number_valid=number_valid+1
  if(checkvalue<mincount):
    toolow+=1
  if(checkvalue>maxcount):
    toohigh+=1
  if(mincount>=maxcount):
    print "Problem?"

print number_valid
#print toolow
#print toohigh
#print number_valid+toolow+toohigh
