# Problem Link : https://leetcode.com/problems/squares-of-a-sorted-array/description/
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1
        k = n - 1
        res = [0]*n

        while i <= j:
            x = nums[i] * nums[i]
            y = nums[j] * nums[j]
            
            if x < y:
                res[k] = y
                j -= 1
            else:
                res[k] = x
                i += 1
            k -= 1
        return res

sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
