# Question Link : https://leetcode.com/problems/reverse-string/description/
# Solution 

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # in place using in-built method 
        # s.reverse()

        # way 2 not in place
        """ newS = s[::-1]
        s.clear()
        s += newS """
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
