# Question Link :https://leetcode.com/problems/merge-sorted-array/description
#  Solution : 
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """ so my observation is m and n is valid numbers not placeholders zeros """
        # Method 1
        """ 
            i = m
            j = 0
            while i < m + n:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            nums1.sort()
         """
         # Method 2 in place 
        move1 = m - 1
        move2 = n - 1
        write = m + n - 1

        while move2 >= 0:
            if move1 >= 0 and nums1[move1] > nums2[move2]:
                nums1[write] = nums1[move1]
                move1 -= 1
            else:
                nums1[write] = nums2[move2]
                move2 -= 1
            write -= 1
