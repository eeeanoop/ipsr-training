class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        left, right = 0, 0
        max_concsecutive_string_len = 0
        char_count = {}

        # Expand the right pointer
        for right in range(len(s)):
            # Take count of chars inside the window

            char_count[s[right]]= char_count.get(s[right],0) + 1

            # window width - max(recurring_char count) > k
            while (right-left+1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1
                left += 1
            max_concsecutive_string_len = max(max_concsecutive_string_len, right-left+1)

        return max_concsecutive_string_len
        