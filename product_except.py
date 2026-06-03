print('hello, world')

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 def product_except_i(x: list[int]) -> list[int]:

Example 1:

Input: nums = [1,2,3,4]
[1,1,2,6]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

# 1. loop through the list
# sub-lit except that number
# sub-list

def product_execept_optimized(x: list[int]) -> list[int]:
  left = 1
  result:list[int] = []
  for i in range(len(x)):
    result.append(left)
    left *= x[i]
 
  right = 1
  for j in range(len(x)-1,-1,-1):
    result[j] *= right
    right *= x[j]
  print(result)
    

  
    


def product_except(x:list[int])->list[int]:

  result = []
  for i in x:
    product: int = 1
    for j in x:
      if j != i:
        product *= j
    result.append(product)
  print(result)
    
    
product_execept_optimized([1,2,3,4])
    


