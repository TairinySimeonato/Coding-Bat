# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  count = ""
  for i in range(len(str)):
    if i % 2 == 0:
      count += str[i]
  return count
