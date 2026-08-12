
def search_in_a_sorted_array(input_nums: list[int], search_value:int ) -> int:

  left, right = 0, len(input_nums)-1
  # find the middle value
 

  while left <= right :
    mid_index = left + (right-left)//2

    # see if the search value is i the right side of the middle index
    if search_value == input_nums[mid_index]:
      return mid_index
    elif search_value > input_nums[mid_index]:
      left = mid_index + 1
    else:
      right = mid_index -1
      
  return -1


print(search_in_a_sorted_array([-1,0,3,5,9,12],search_value=12))