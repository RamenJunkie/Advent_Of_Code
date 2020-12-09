with open('day6data.txt') as f:
    lines = [line.rstrip() for line in f]

lettercount =[]
sum_total=0
first=1
num_groups=0

for line in lines:
  if line == '':
    #print len(lettercount)
    sum_total+=len(lettercount)
    #print sum_total
    lettercount=[]
    first=1
    num_groups+=1
    #print ''
  else:
    if first == 1:
      for i in line:
        lettercount.append(i)
      
      #print lettercount
      #print line
      first=0
    else:
      for i in lettercount:
        if i not in line:
          #print ''
          #print lettercount
          lettercount.remove(i)
          #print i
          #print lettercount

      #print lettercount
      #print line


print sum_total
print num_groups
