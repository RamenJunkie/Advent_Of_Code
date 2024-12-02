#Lets comment the heck out of this one and flow with the process.  So it may look a little ugly.

# I am essentially just... blogging in real time, in the comments now....

#Until the end, I am using the sample data set
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9

# I started by copying Day01, then modifying the top lines to read my Day02Input.txt file, because, lazy.
# Then just deleting everything else below the set processing, because none of it is real useful.
with open("Day02Input.txt") as file:
    data = file.read()

sets = [each.split(" ") for each in data.split("\n")]

# Then I want to test it so I add a print of the result, just to make sure it looks right against the sample data set. 
##### NOTE Removed code will just be commented out, to follow the comments.  I'll mark these as ##
# Tehre will be a lot of prints removed.  These are used gratuitously to verify things are working.

##print(sets)

# This gives
# [['7', '6', '4', '2', '1'], ['1', '2', '7', '8', '9'], ['9', '7', '6', '2', '1'], ['1', '3', '2', '4', '5'], ['8', '6', '4', '4', '1'], ['1', '3', '6', '7', '9'], ['']]
# For some reason I keep getting black sets on these, so I'm just gonna do like day one and clip it.
sets.pop()

##print(sets)

# Part of the test on this one is if the digits are ascending or descending, I have an idea to test this out quickly
# Lets see if it works.

##for each in sets:
##   print(each)
##   if each == each.sort():
##      print("Ascending")
##   print(each.sort())
# Ok, I ran into a prolem here, because it's reading everything in as strings and not integers.

# There is probably a more elegant way to do this but this will work.
int_sets = []

for each in sets:
   int_sets.append(list(map(int, each)))

## print(int_sets)

# [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
# Perfect, let's try again.
# Also it looks like I needed to use a different sort, for reasons.
# https://stackoverflow.com/questions/403421/how-do-i-sort-a-list-of-objects-based-on-an-attribute-of-the-objects

##for each in int_sets:
##   if each == sorted(each):
##      print("Ascending")
##   else:
##      print("Bad")

# Bad
# Ascending
# Bad
# Bad
# Bad
# Ascending

# Ok, but I also need Descending Lists

##for each in int_sets:
##   if each == sorted(each):
##      print("Ascending")
##   elif each == sorted(each, reverse=True):
##      print("Descending")
##   else:
##      print("Bad")

# Descending
# Ascending
# Descending
# Bad
# Descending
# Ascending

# Ok, things are working well, I probably need a counter for the number of good lists though.
# Despite these tess and comments, I am still "at the top" of the pure code so.

good_lists = 0

# I also need to check for the other condition in the test
# Any two adjacent levels differ by at least one and at most three.

# Since I am still "at the top", I will go ahead and just make a function to check this here.
# Note to self, post a clean version of the code below.

def check_range(a,b):
##  print(f"{a},{b}")
##  print(abs(b-a))
##  if abs(b-a) >= 3 and abs(b-a) <= 1:
  if abs(b-a) <= 3 and abs(b-a) >= 1:
##    print("OK")
    return True
  return False

# I am also going to clean up my ascending/Descending loop a bit.

##for each in int_sets:
##   if each == sorted(each) or each == sorted(each, reverse=True):
##      for i in range(len(each)-1):
##         print(i)
##         print(f"{each[i]},{each[i+1]}")
##         check_range(each[i], each[i+1])
##      print("Good")
##   else:
##      print("Bad")

# Something is not working right, so I'm modifying the defined function above a bit and adding some prints to test.

# I found it, my Greater than less than signs were reversed, oops.
# Also, all this commenting is seriously slowing this whole process

# I'm copying the above loop though, for posterity, before finding a good way to track good loops.

for each in int_sets:
   if each == sorted(each) or each == sorted(each, reverse=True):
# Lets assume a set is true
      good_set = True
      for i in range(len(each)-1):
# If the set is still good, keep checking, otherwise, don't.
         if good_set:
           good_set = check_range(each[i], each[i+1])
# I hate having these conditionals like this, but this is starting to get exhausting typing this, and it's easy.
# If the set is still good after checking the digits, add one to the total number of good sets.
      if good_set:
         good_lists +=1
# I removed the else, because I don't care if it's bad.

print(good_lists)
# This gives 2, as expected, for the sample dataset.
# Time to adjust for my personal data set as input.

# This gives 326 (data sets and answers very by person).
# This is the correct answer, on to Part 2.

# For Part 2, the system can tolorate a single bad level.  Those are what I am checking for in "check_range'.
# Normally I would modify my code to do both tests at once, but for TODAY, i am just going to make a second version.
# Basically, if a bad pair happens, it needs to try matching with the next higher number.  But it only needs to try it once.

good_lists_p2 = 0

##for each in int_sets:
##   if each == sorted(each) or each == sorted(each, reverse=True):
##      print(each)
##      good_set = True
##      dampened = False
##      for i in range(len(each)-1):
##         if good_set:
##           good_set = check_range(each[i], each[i+1])
##           if not good_set and not dampened:
##              print(f"Trying {each[i]} and {each[i+2]}")
##              print(good_set)
##              good_set = check_range(each[i], each[i+2])
##              print(good_set)
##              dampened = True
##      print(good_set)
##      if good_set:
##         good_lists_p2 +=1
##      print(good_lists_p2)

# So, this is not working out.  It's mostly working, but it's failing my Ascending/Descending check.
# Specifically, this one in the sample data fails. "1 3 2 4 5"

# What I need, is a new way to check Ascending and Descending lists.  An annoying way, that is ugly.
# I could build this in to the existing checks, but at this point, I don't want to, I just need a yes/no check
# And all these notes and comments are getting annoying.

def check_order(list):
   if list[-1] > list[0]:
     direction = "Asc"
   elif list[-1] < list[0]:
     direction = "Desc"
   else:
     direction = "Equal"
#   print(direction)

   for n in range(len(list)-1):
      if list[n+1] > list[n] and direction == "Desc":
        if n+2 < len(list):
          if list[n+2] > list[n]:
             return False
      if list[n+1] < list[n] and direction == "Asc":
        if n+2 < len(list):
          if list[n+2] < list[n]:
             return False
   return True

for each in int_sets:
#   print(each)
   if check_order(each):
      good_set = True
      dampened = False
      for i in range(len(each)-1):
         if good_set:
           good_set = check_range(each[i], each[i+1])
           if not good_set and not dampened and i+2 < len(each):
#             print(f"Trying {each[i]} and {each[i+2]}")
#             print(good_set)
              good_set = check_range(each[i], each[i+2])
#              print(good_set)
              dampened = True
#      print(good_set)
      if good_set:
         good_lists_p2 +=1
#      print(good_lists_p2)






print(good_lists_p2)


# 415 too high
# 414 too high
# 400 too high
# Ok, I started Guessing
# I got it
# 381 for my data set.







