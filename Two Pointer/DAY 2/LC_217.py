# Contains Duplicate — #217
# Problem Link : https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for n in nums:
            if n in seen:
                return True
            seen[n] = True
        return False