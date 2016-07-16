# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

def has22(nums):
  for idx, val in enumerate(nums):
    if ((val == 2) and (nums[idx - 1] == 2) and idx != 0):
      return True
  return False

# I had trouble with this one - we need to redo it later
# we want more solution variants to ensure tai knows it
# 1) look-behind using indexes
# 2) look-behind using variables to save off last value
