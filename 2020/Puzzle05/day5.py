with open('day5data.txt') as f:
    lines = [line.rstrip() for line in f]

row='0b'
col='0b'

largest=0
ids=[]

#binary Exclusion
#0-127
#0-7

for line in lines:
  if line != '':
     for i in line:
       if i == 'F':
         row=row+'0'
       if i == 'B':
         row=row+'1'
       if i == 'L':
         col=col+'0'
       if i == 'R':
         col=col+'1'
     current=(eval(row))*8+eval(col)
     ids.append(current)

     if current>largest:
       largest=current


     row='0b'
     col='0b'

ids=sorted(ids)
#print ids

prev=ids[0]
now=ids[1]

for next in ids[2:]:
   if next-1 != now:
     print next-1
   prev=now
   now=next



print largest
