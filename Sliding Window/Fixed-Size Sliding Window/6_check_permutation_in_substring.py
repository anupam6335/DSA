#  https://www.geeksforgeeks.org/problems/check-if-permutation-is-substring/1


""" 
## 1. Problem Decomposition

Sub-tasks List:
 Task 1: Generate all permutations of the pattern string
 Task 2: Check if any permutation exists as a substring in the text
 Task 3: For each substring of text with length equal to pattern, check if it's an anagram of pattern
 Task 4: Compare character frequencies instead of generating permutations
 Task 5: Use sliding window with frequency tracking for efficiency


 """
# brute force 
from itertools import permutations

class Solution:
    def search(self, txt, pat):
        unique_perms = set(''.join(p) for p in permutations(pat))
        print(unique_perms)
        n = len(txt)
        k = len(pat)
        
        for i in range(n - k + 1):
            substring = txt[i:i + k]
            print(substring)
            if substring in unique_perms:
                return True
        return False

# brute force slight improve

def check_permutation_brute_force2(txt, pat):
    """
    Alternative brute force: Check each substring if it's an anagram of pattern
    """
    n = len(txt)
    k = len(pat)
    
    # Sort the pattern once for comparison
    sorted_pat = sorted(pat)
    
    # Check each substring of length k
    for i in range(n - k + 1):
        substring = txt[i:i + k]
        # Check if substring is an anagram of pattern
        if sorted(substring) == sorted_pat:
            return True
    
    return False
""" 

Why this is inefficient:
    - Time Complexity: O(n × k! × k) for the first approach (generating k! permutations)
    - Time Complexity: O(n × k log k) for the second approach (sorting each substring)
    - Both are too slow for large inputs (n up to 10^5, k up to 10^5)
    - The first approach has factorial complexity which is catastrophic
    - The second approach has O(n × k log k) which is still too slow for large k

 """

# First Optimization Attempt

def check_permutation_optimized1(txt, pat):
    """
    First optimization: Use frequency counting instead of sorting
    """
    n = len(txt)
    k = len(pat)
    
    if k > n:
        return False
    
    # Create frequency map for pattern
    pat_freq = {}
    for char in pat:
        pat_freq[char] = pat_freq.get(char, 0) + 1
    
    # Check each substring using frequency comparison
    for i in range(n - k + 1):
        substring = txt[i:i + k]
        
        # Create frequency map for substring
        substr_freq = {}
        for char in substring:
            substr_freq[char] = substr_freq.get(char, 0) + 1
        
        # Compare frequency maps
        if substr_freq == pat_freq:
            return True
    
    return False

""" 

Optimization explanation:

Replaced sorting with frequency counting using dictionaries

Time Complexity: O(n × k) - better than O(n × k log k)

Still not efficient enough for large inputs (n × k could be 10^10 operations)

We're recomputing the frequency map for each substring from scratch

 """


# Final optimization 

def check_permutation_optimized_final(txt, pat):
    """
    Final optimized solution: Sliding window with frequency tracking
    """
    n = len(txt)
    k = len(pat)
    
    if k > n:
        return False
    
    # Frequency map for pattern
    pat_freq = {}
    for char in pat:
        pat_freq[char] = pat_freq.get(char, 0) + 1
    
    # Frequency map for current window
    window_freq = {}
    
    # Initialize the first window
    for i in range(k):
        char = txt[i]
        window_freq[char] = window_freq.get(char, 0) + 1
    
    # Check if first window matches
    if window_freq == pat_freq:
        return True
    
    # Slide the window through the text
    for i in range(k, n):
        # Remove the character leaving the window
        left_char = txt[i - k]
        window_freq[left_char] -= 1
        if window_freq[left_char] == 0:
            del window_freq[left_char]
        
        # Add the new character entering the window
        right_char = txt[i]
        window_freq[right_char] = window_freq.get(right_char, 0) + 1
        
        # Check if current window matches pattern
        if window_freq == pat_freq:
            return True
    
    return False

# Even more optimized version (using array instead of dictionary)
def check_permutation_optimized_array(txt, pat):
    """
    Most efficient solution: Using fixed array for frequency counting
    """
    n = len(txt)
    k = len(pat)
    
    if k > n:
        return False
    
    # Use array of size 26 for lowercase English letters
    pat_count = [0] * 26
    window_count = [0] * 26
    
    # Fill pattern frequency array
    for char in pat:
        pat_count[ord(char) - ord('a')] += 1
    
    # Initialize first window
    for i in range(k):
        window_count[ord(txt[i]) - ord('a')] += 1
    
    # Check first window
    if window_count == pat_count:
        return True
    
    # Slide the window
    for i in range(k, n):
        # Remove left character
        left_idx = ord(txt[i - k]) - ord('a')
        window_count[left_idx] -= 1
        
        # Add right character
        right_idx = ord(txt[i]) - ord('a')
        window_count[right_idx] += 1
        
        # Check if windows match
        if window_count == pat_count:
            return True
    
    return False



""" 


Final optimization explanation:

    -Sliding Window Technique: Instead of recomputing frequencies for each window, we update the frequency map incrementally

    -Constant Time Updates: Adding/removing one character from frequency map takes O(1) time

    -Array vs Dictionary: Using fixed array is more efficient than dictionary for comparison

    -Time Complexity: O(n) - linear time, perfect for large inputs

    -Space Complexity: O(1) - fixed size arrays (26 elements each)

Key insights:

    -We don't need to generate permutations - just check character frequencies

    -Sliding window allows incremental updates to frequency counts

    -Array comparison is faster than dictionary comparison for small alphabets

    -The solution efficiently handles the worst-case constraints

The final solution is optimal with O(n) time complexity and O(1) space complexity, perfectly suited for the given constraints.
 """