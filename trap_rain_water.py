class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height)-1

        left_max_height = 0
        right_max_height = 0

        water = 0

        while left_pointer < right_pointer:

            if height[left_pointer] < height[right_pointer]:

                left_max_height = max(left_max_height, height[left_pointer] )
                water += (left_max_height - height[left_pointer])
                left_pointer += 1
            else:
                right_max_height = max(right_max_height, height[right_pointer])
                water += (right_max_height-height[right_pointer])
                right_pointer -=1

        return water