# problem link ( premimum ): https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
# problem Link : https://neetcode.io/problems/lowest-common-ancestor-of-a-binary-tree-iii/question?list=allNC
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        i = j = 0

        while i < len(s) and j < n:
            if s[i] == t[j]:
                j += 1
            i += 1
        return n - j

sol = Solution()
print(sol.appendCharacters("coaching","coding"))