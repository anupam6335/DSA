# Problem Link : https://leetcode.com/problems/two-sum/description/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, n in enumerate(nums):
            key = target - n
            if key in mp:
                return [mp[key], i]
            mp[n] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))