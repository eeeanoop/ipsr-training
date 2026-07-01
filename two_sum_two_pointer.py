# Given an  list of sorted ints, find two elements that adds up to a target sum
# return the indices of the two elements
# input_list = [2,7,11,15], target = 9
# output = [1,2]

def two_sum_second_type(input_list: list[int], target: int) -> list[int]:

  # Two pointer problem
  # Array is sorted

  left = 0
  right = len(input_list)-1

  while left < right:
    if input_list[left] + input_list[right] == target:
      return [left+1, right+1]
    elif input_list[left] + input_list[right] < target:
      left += 1
    else:
      right -= 1

print(two_sum_second_type([2,7,11,15], target = 9))
  
    

  
  
  

