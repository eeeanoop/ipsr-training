'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

'''



def is_paliandrome(input_string: str) -> bool:

  # Two pointer problme
  # start from both sides, compare chars, if they don't match return false
  # if the the loop  completes return true

  left, right = 0, len(input_string)-1
  while left < right:
    while left < right  and not input_string[left].isalnum():
      left +=1

    while left < right and not input_string[right].isalnum():
      right -=1

    if input_string[left].lower() == input_string[right].lower():
      left += 1
      right -= 1
    else:
      return False

  return True


print(is_paliandrome("A man, a plan, a canal: Panama"))

print(is_paliandrome("'''"))
  