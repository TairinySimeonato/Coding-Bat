"""
Given a number n, return True if n is in the range 1..10, inclusive. 
Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
"""

def in1to10(n, outside_mode):
  if not outside_mode and (n >= 1 and n <= 10):
    return True
  if outside_mode and (n <= 1 or n >= 10):
    return True
    
  return False
