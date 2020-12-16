
def sum(arr):
    result = sum(arr)
    return result

def bagcheck(quantity, current):
  total=int(quantity)
  #print checked  
  for line in lines:
    endloc = line.find("contain")
    if current in line[:endloc]:
      content = line[endloc+7:-1].split(',')
      #print content
      for i in content:
        if i != ' no other bags':
          #print total
          if i[-1] == "s":
            i=i[:-1]
          #print i[1]
          #print i[3:]
          if i not in checked:
            check.append(i)
            checked.append(i)
          #total += int(i[1])
          total += int(quantity) * bagcheck(i[1], i[3:])
        else: total=quantity
       
  print current+" has inside "+str(total)+" and there are "+quantity+" of them, total of "+str(total)
  return int(total)

with open('day7data.txt') as f:
    lines = [line.rstrip() for line in f]

bags=0
check=[" 1 shiny gold"]
checked=[]
total=0

if check[0] != ' no other bags':
  bags=(bagcheck(check[0][1],check[0][3:]))
    #print bags

print bags-1

