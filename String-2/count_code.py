# Return the number of times that the string "code" appears anywhere in the given string, 
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  count = 0
  
  for idx in range(len(str)):
    if idx + 3 >= len(str):
      break
      
    if str[idx:idx+2] == "co" and str[idx+3] == "e":
      count += 1
    
  return count

# we need to REDO this
