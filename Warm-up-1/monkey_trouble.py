
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


def monkey_trouble(a_smile, b_smile):
  # If both monkeys are smiling, return True
  if a_smile and b_smile:
    return True
    
  # If no monkey is smiling, return True  
  elif not a_smile and not b_smile:
    return True
    
  # If one monkey is smiling and the other is not, return False
  return False
