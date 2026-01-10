# Problem Link : https://leetcode.com/problems/sort-colors/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        i = k = 0
        j = len(nums) - 1

        # 0,0,1,1,2,2
        #     i
        #       j
        #         k


        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] == 1:
                k += 1
            else: # found 2
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
        return nums


sol = Solution()
print(sol.sortColors([2,0,2,1,1,0, 0, 0, 2, 2, 1, 2, 0, 1]))