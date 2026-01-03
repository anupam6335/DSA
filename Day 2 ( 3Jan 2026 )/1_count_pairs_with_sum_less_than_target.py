# problem link : https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        cnt = 0
        j = n - 1

        while i < j:
            curr_sum = nums[i] + nums[j]
            if curr_sum < target:
                cnt += ( j - i)
                i += 1
            else:
                j -= 1
        return cnt
    
sol = Solution()
print(sol.countPairs([-1,1,2,3,1], 2))