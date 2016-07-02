# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string.

def missing_char(str, n):
  return str[:n] + str [n+1:]
