with open('day1data.txt') as f:
    lines = [line.rstrip() for line in f]

for x in lines:
  for y in lines:
    if((int(x)+int(y))==2020):
      print int(x)*int(y)
