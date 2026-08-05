def lengthOfLongestSubstring(self, s: str) -> int:
    substring = ''
    max_substring_length = 0

    for charcter in s:
        if charcter not in substring:
            substring += charcter
            max_substring_length  = max(max_substring_length, len(substring) )
        else:
            substring = substring[substring.index(charcter) + 1 :] + charcter
    return max_substring_length



def return_longest_substring_leng_sliding_window(input_string: str) -> int:
  seen = set()
  left = 0
  max_lengt = 0
  for right in range(len(input_string)):

    while input_string[right] in seen:
      seen.remove(input_string[left])
      left += 1
      
    seen.add(input_string[right])

    max_lengt = max(max_lengt, right-left +1 )
  return max_lengt