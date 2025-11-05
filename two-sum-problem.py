# nums = [1, 2, 4, 6, 7, 11, 15], target = 9
# Find two element in this list which will add up to 9
from math import floor


# This is inefficient because of n2 runtime
def twoSum(nums, target):
    k = 0
    j = 1
    for i in range(len(nums)-1):
        if nums[k] + nums[k+j] == target:
            return [nums[k], nums[k+j]]
        else:
            j += 1

# Try with hashmap
# Time complexity
# n

    # for i, num in enumerate(nums):
    #     print(hash_map)
    #     if (target-num) in hash_map:
    #         return hash_map[target-num],i
    #     hash_map[num] = i

def twoSum2(nums, target):
    result = {}
    for i, j in enumerate(nums):
        print(i, j)
        if result.get(target - j):
            print(f'from list = {i}, from dict = {result.get(target - j)}')
            print(f'from list value = {nums[i]}, from dict = {nums[result.get(target - j)]}')
        result[target - j] = i


def twoSum3(nums , target):
    hash_map = {}
    for i, num in enumerate(nums):
        print(hash_map)
        if (target-num) in hash_map:
            return hash_map[target-num],i
        hash_map[num] = i

if __name__ == '__main__':
    nums = [1, 3, 2, 4, 6, 7, 11, 15, 4, 6]
    target = 9
    print(twoSum3(nums, target))