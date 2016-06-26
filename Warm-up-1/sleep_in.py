# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.

def sleep_in(weekday, vacation):
# We sleep in if it isn't a weekday or if we are on vacation:
  if not weekday or vacation:
    return True
# Otherwise, we don't sleep in:
  else:
    return False
