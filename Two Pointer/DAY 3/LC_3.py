# Longest Substring Without Repeating Characters — #3
# problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        max_len = 0
        start = 0
        curr_len = 0
        if len(s) == 1:
            return 1

        for i, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= start:
                start = last_index[ch] + 1
            last_index[ch] = i
            curr_len = i - start + 1
            max_len = max(max_len, curr_len)
        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring("abba"))