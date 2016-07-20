# Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  if str.count("cat") == str.count("dog"):
    return True
  return False
