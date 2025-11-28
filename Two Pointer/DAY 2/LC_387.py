# First unique character (LC 387)
# Question Link : https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_map = {}

        # Count frequency
        for ch in s:
            s_map[ch] = s_map.get(ch, 0) + 1

        # Find first unique character by original string order
        for i, ch in enumerate(s):
            if s_map[ch] == 1:
                return i

        return -1

sol = Solution()
print(sol.firstUniqChar("loveleetcode"))

