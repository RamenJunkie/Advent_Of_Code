with open('day6data.txt') as f:
    lines = [line.rstrip() for line in f]

lettercount =[]
sum_total=0

for line in lines:
  if line == '':
    print len(lettercount)
    sum_total+=len(lettercount)
    lettercount=[]
    print 'space'
  else:
    for i in line:
      if i not in lettercount:
        lettercount.append(i)
        print i


print sum_total
