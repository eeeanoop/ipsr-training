# Give a list or unorderd ints, return the length of the longest sequence of integers
# input array length <= 100,000
# Value of element -1B and +1B
# nums = [-1,-2,3,1,2,5,4,10]
# length = 5

def longestConsecutive(self, nums: List[int]) -> int:
    nums_set = set(nums)
    max_length = 0
    for num in nums_set:
        if num-1 not in nums_set:
            length = 1
            while num+length in nums_set:
                length +=1
            max_length = max(max_length, length )
    return max_length


# Ideas of longest sequence of integers
# two loops
# First loop is to find the starting point of the sequence
# Second loop to find the max length of the sequence