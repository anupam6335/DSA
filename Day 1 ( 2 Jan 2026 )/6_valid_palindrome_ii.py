# Problem Link : https://leetcode.com/problems/valid-palindrome-ii/description/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i, j, s):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isPalindrome(i + 1, j, s) or isPalindrome(i, j - 1, s)
        return True

sol = Solution()
print(sol.validPalindrome("aabbdaa"))