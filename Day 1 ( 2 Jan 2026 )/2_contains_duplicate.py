# Problem Link : https://leetcode.com/problems/contains-duplicate/description/
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for n in nums:
            if n in seen:
                return True
            seen[n] = True
        return False

sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
