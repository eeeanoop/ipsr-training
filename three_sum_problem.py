# three sum problem

# Given a list of integers, return a list of triplets which adds upto zero
# Solution should not contain duplicate triplets
'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

sorted_nums = [-1,-1,0,1,2,-4]


'''

# sort
# use 1 anchor and two pointers left & right
# increment left and decrement right, sum up with anchor to get the targe value
# skip duplicate values for anchor, left & pointer


def three_sum(nums: list[int]) -> list[list[int]]:
  nums.sort()
  result:[list[list[int]]] = []
  
  for i in range(len(nums)):

    if i > 0 and nums[i] == nums[i-1]:
      continue

    left, right = i + 1, len(nums)-1

    while left < right:
      # print(i, left, right)
      # print([nums[i],nums[left],nums[right]])
      if nums[i] + nums[left] + nums[right] < 0:
        left += 1
      elif nums[i] + nums[left] + nums[right] > 0:
        right -= 1
      else:
        result.append([nums[i],nums[left],nums[right]])
        left += 1
        right -= 1
        # Skip all duplicate elements for left
        while left < right and nums[left] == nums[left-1]:
            left += 1
        
        while left < right and  nums[right] == nums[right+1]:
            right -= 1
 
  return result
      
    

print(three_sum([1,1,1,1,1,0,-1,-1,-1]))
'''
anchor = -2 [0]
  left = 0  [1] 
  right = 2 [4]

# not valid
anchor = 0 [1]
left = 0   [2]
right = 2   [4] 

anchor = 2  [3]
left = 2    [4]
right = 2   [4]
'''