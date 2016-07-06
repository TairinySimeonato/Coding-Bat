# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
  if (len(nums) >= 1) and (nums[-1] == nums[0]):
    return True
  return False
