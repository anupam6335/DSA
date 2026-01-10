# Problem Link : https://leetcode.com/problems/valid-palindrome/description/
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[j].lower() != s[i].lower():
                    return False
                i += 1
                j -= 1
        return True

sol = Solution ()
print(sol.isPalindrome( "A man, a plan, a canal: Panama"))