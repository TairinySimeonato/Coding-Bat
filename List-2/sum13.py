# Return the sum of the numbers in the array, returning 0 for an empty array. 
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  count = 0
  previous_number = 0
  
  for current_number in nums:
    if current_number != 13 and previous_number != 13:
      count += current_number
  
    previous_number = current_number
  return count

