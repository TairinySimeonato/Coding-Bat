# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  count = ""
  for i in range (len(str)):
    count += str[:i+1]
  return count
