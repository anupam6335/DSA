# Two Sum using hash map 
# Question Link : https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}  # value -> index

        for pos, key in enumerate(nums):
            find = abs(target - key) 
            if find in nums_map:
                return [nums_map[find], pos]
            nums_map[key] = pos



sol = Solution()
print(sol.twoSum([2, 7, 2, 11, 15 ],17 ))


""" 
ALGORITHM :

1. Start with an empty dictionary.

2. For each element in the array, calculate the value needed to reach the target (target - current_value).

3. Check if this required value already exists in the dictionary.

4. If it exists, return the stored index (from the dictionary) and the current index.

5. If it does not exist, store the current value and its index in the dictionary.
"""