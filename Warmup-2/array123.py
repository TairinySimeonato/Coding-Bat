# Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.

def array123(nums):
  if 1 in nums and 2 in nums and 3 in nums:
    return True
  return False
