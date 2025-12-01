# Ransom Note — #383
# problem Link : https://leetcode.com/problems/ransom-note/

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """ freq = {}
        for mag in magazine:
            if mag not in freq:
                freq[mag] = 0
            freq[mag] += 1
        
        for ran in ransomNote:
            if ran not in freq or freq[ran] == 0:
                return False
            freq[ran] -= 1
        return True """
        freq = Counter(magazine)
        for ran in ransomNote:
            if freq[ran] == 0:
                return False
            freq[ran] -= 1
        return True
sol = Solution()
print(sol.canConstruct("aa", "aab"))