def change_seats(current):
  global counter
  hcount = 0
  wcount = 0
  newseats=[]

  for i in current:
    newline=""
    for j in i:
      occ_count=0
    
      for h in range(hcount-1,hcount+1):
        for w in range(wcount-1,wcount+1):
          #print str(h+hcount)+" "+str(w+wcount)
          if (0 <= h < len(current)-1) and (0 <= w < len(i)):
#            if current[h][w] == "." and not (h == hcount and w == wcount):
#              print "LookBeyond"
            if not (h == hcount == w):  
              if current[h][w] == "O":
                print str(h)+" "+str(w)+" "+current[h][w]
                occ_count +=1

      if j == 'L' and occ_count == 0:
        newline+='O'
      elif j == 'O' and occ_count >= 4:
        newline+='L'
      else:
        newline+=current[hcount][wcount]
      wcount+=1
    hcount+=1
    wcount = 0
    newseats.append(newline)
  hcount=0



  # print the new array
  #for i in newseats:
  #  print i

  #count seats
  occupancy = 0
  for i in newseats:
    occupancy += i.count("O")
  print occupancy

  counter+=1
  if counter <= 1:
    change_seats(newseats)


with open('day11data.txt') as f:
    lines = [line.rstrip() for line in f]

counter=0
change_seats(lines)


