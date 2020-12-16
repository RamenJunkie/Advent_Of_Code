with open('day10data.txt') as f:
    lines = [line.rstrip() for line in f]

num_ones=1
num_threes=1
jolts=[]

for i in lines:
  jolts.append(int(i))

jolts = sorted(jolts)
#print jolts

for i in jolts:
  if jolts.index(i)+1== len(jolts):
    break

  next=jolts[jolts.index(i)+1]

  #oprint next-i

  if next-i == 1:
    num_ones+=1

  if next-i == 3:
    num_threes+=1

print num_ones
print num_threes
print num_ones*num_threes
