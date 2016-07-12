# Given 3 int values, a b c, return their sum. 
# However, if one of the values is the same as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  total = a + b + c
  if a == b and b == c and c == a:
    return 0
  if a == b:
    return c
  if b == c:
    return a
  if c == a:
    return b
    
  return total
