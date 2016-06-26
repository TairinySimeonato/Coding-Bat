# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0...23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  # If the parrot is talking before 7 or after 20, we are in trouble, so, return True
  if talking and ((hour < 7) or (hour > 20)):
    return True
    
  # if parrot is talking between 7 and 20, return false. We are not in trouble  
  return False
