# Given an array of ints length 3, figure out which is larger between the first and last elements in the array, 
# and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
  if nums[0] >= nums[2]:
    return [nums[0], nums[0], nums[0]]
  return [nums[2], nums[2], nums[2]]
  
  # alternative solution
  m = max(nums[0], nums[2])
  return [m, m, m]
