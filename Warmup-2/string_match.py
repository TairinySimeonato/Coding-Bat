
# REDO THIS
def string_match(a, b):
  matches = 0
  
  string_to_check = a
  if len(b) < len(a):
    string_to_check = b
    
  for idx, val in enumerate(a):
    if idx+1 >= len(a) or idx+1 >= len(b):
      break
    
    if a[idx:idx+2] == b[idx:idx+2]:
      matches += 1
  
  return matches

# REDO THIS
