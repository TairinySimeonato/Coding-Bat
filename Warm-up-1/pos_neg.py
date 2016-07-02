# Given 2 int values, return True if one is negative and one is positive. 
# Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
  # return True if one is negative and one is positive. 
  if (negative == False) and ((a > 0 and b < 0) or (a < 0 and b > 0)):
    return True

  #  Except if the parameter "negative" is True, then return True only if both are negative.
  if negative:
    if a < 0 and b < 0:
      return True
  
  return False
