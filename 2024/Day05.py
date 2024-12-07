with open("Day05Input.txt") as file:
    data = file.read()


rules = data.split("\n\n")[0].split("\n")
pages = data.split("\n\n")[1].split("\n")
#pages.pop()
bad_pages = []

#Verify Inputs
#for each in pages:
#for each in rules:
#  print(each)

total = 0
total2 = 0
total3 = 0

for each in pages:
  these_pages = each.split(",")
  goodset = True
  running = True
#  print(these_pages)
  while running:
#    print(these_pages)
    running = False
    restart = False 
    for p1 in these_pages:
      for p2 in these_pages[these_pages.index(p1):]:
        if p1 != p2:
          pair = f"{p1}|{p2}"
          if pair in rules:
            #print("Good")
            pass
          else:
#            print(these_pages.index(p1))
            p1pos = these_pages.index(p1)
            p2pos = these_pages.index(p2)
            these_pages[p1pos] = p2
            these_pages[p2pos] = p1
#            print(these_pages.index(p1))
            #print("Bad")
            #print(pair)
            running = True
            goodset = False
 #           print("---")
 #           print(these_pages)
  if goodset:
    #print(f"Set {pages.index(each)} is good")
    total += int(these_pages[int((len(these_pages) - 1)/2)])
  else:
    bad_pages.append(these_pages)
    total2 += int(these_pages[int((len(these_pages) - 1)/2)])



for these_pages in bad_pages:
  goodset = True
  running = True
#  print(these_pages)
  while running:
#    print(these_pages)
    running = False
    restart = False 
    for p1 in these_pages:
      for p2 in these_pages[these_pages.index(p1):]:
        if p1 != p2:
          pair = f"{p1}|{p2}"
          if pair in rules:
            #print("Good")
            pass
          else:
            these_pages.append(these_pages.pop(p1))
#            print(these_pages.index(p1))
#            print(these_pages.index(p1))
            #print("Bad")
            #print(pair)
            running = True
            goodset = False
 #           print("---")
 #           print(these_pages)
  total3 += int(these_pages[int((len(these_pages) - 1)/2)])




print(total)
print(total2)
# Part 1 - 7365
#5692 Low
#5700 Low
#5800 Too High
#5750 - Wrong
#5730 - Wrong
print(total3)
## Its not working but the answer for future reference is 5770
