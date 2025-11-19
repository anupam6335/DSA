# Question Link : https://leetcode.com/problems/valid-palindrome/description/

# Solution 1 : 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for ch in s:
            if ch.isalnum():
                newS += ch
        n = len(newS)
        l, r = 0, n - 1

        while l < r:
            if newS[l].lower() != newS[r].lower():
                return False
            l += 1
            r -= 1
        return True