# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
# If the int is less or equal 21:
  if n <= 21:
# return its absolute difference between n and 21:
    return abs(21 - n)
    
# If the int is greater than 21:
  else:
# return a value that is double the absolute difference between n and 21:
    return abs(n - 21) * 2
