# problem Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            curr_sum = numbers[i] + numbers[j]
            if curr_sum < target:
                i += 1
            elif curr_sum > target:
                j -= 1
            else:
                return [i + 1, j + 1]
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))