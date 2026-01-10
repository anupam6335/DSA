# Two-Pointer Applications & Patterns

A comprehensive list of two-pointer patterns and their associated problems, grouped by technique.

## Table of Contents
- [I. Converging Pointers (Opposite Ends)](#i-converging-pointers-opposite-ends)
- [II. Parallel Pointers (Same Direction)](#ii-parallel-pointers-same-direction)
- [III. Sliding Window (Dynamic Range)](#iii-sliding-window-dynamic-range)
- [IV. Partition-Based Pointers](#iv-partition-based-pointers)
- [V. Interval & Range Pointers](#v-interval--range-pointers)
- [VI. Multi-Array/Sequence Pointers](#vi-multi-arraysequence-pointers)
- [VII. Multi-Pointer Generalizations (3+ Pointers)](#vii-multi-pointer-generalizations-3-pointers)
- [VIII. Hybrid Patterns & Advanced Applications](#viii-hybrid-patterns--advanced-applications)
- [IX. Problem-Solving Frameworks & Techniques](#ix-problem-solving-frameworks--techniques)
- [X. Practice Progression](#x-practice-progression)

---

## I. Converging Pointers (Opposite Ends)
Pointers start at opposite ends and move toward each other.

### 1. Pair Search & Sum Problems
- Two Sum (sorted array)
- Pair with target sum in sorted array
- Closest pair sum to target
- Minimize abs(arr[i] - arr[j])
- Count pairs with given sum
- Count pairs with difference K
- Count pairs with sum less than K
- Find pairs with given sum in BST (inorder + converging)
- Find pair with maximum sum less than K
- Pairs with sum in a range [L, R]
- Find four elements a, b, c, d such that a + b = c + d
- Pythagorean triplet (a² + b² = c²)

### 2. Multi-Sum Generalizations
- Three Sum (all unique triplets with sum = 0)
- Three Sum Closest (to target)
- Three Sum Smaller (count triplets with sum < target)
- Four Sum (all unique quadruplets)
- K-Sum (generalized using recursion + converging pointers)
- Three Sum with multiplicity
- Valid triangle number (count triplets forming triangle)
- 3Sum with different constraints (non-decreasing, etc.)

### 3. Area & Water Problems
- Container With Most Water (max area)
- Trapping Rain Water (total trapped water)
- Trapping Rain Water II (2D variant with priority queue)
- Pour Water (simulation)
- Max water between two buildings
- Minimum removals to make max-min <= K

### 4. Symmetry & Palindrome Operations
- Palindrome check (string/array)
- Valid palindrome (skip non-alphanumeric)
- Valid palindrome II (allow one deletion)
- Palindrome linked list (convert to array or reverse half)
- Longest palindromic substring (expand around center)
- Longest palindromic subsequence (DP, but has two-pointer flavor)
- Palindrome partitioning (minimum cuts - DP)
- Shortest palindrome to add
- Find all palindromic substrings
- Palindrome pairs (with hash map)

### 5. In-Place Reversal Operations
- Reverse array in-place
- Reverse string in-place
- Reverse words in string (multiple steps)
- Reverse linked list (iterative)
- Reverse linked list II (between positions)
- Reverse nodes in k-group
- Reverse vowels of a string
- Reverse only letters
- Reverse string without affecting special chars

### 6. Boundary Detection & Comparison
- Compare version numbers (split by '.')
- Backspace string compare (process from end)
- Shortest unsorted continuous subarray (find boundaries)
- Squares of sorted array (merge from both ends)
- Sort array by parity (even first, odd last - converging version)
- Sort array by parity II (even at even indices)
- Find k closest elements (binary search + converging)
- Valid mountain array (climb from both ends)
- Find peak element (though typically binary search)

### 7. Greedy Matching & Optimization
- Assign cookies (greedy)
- Boats to save people (minimum boats)
- Maximum number of consecutive 1's (flip at most K zeros)
- Maximize distance to closest person
- Minimize maximum pair difference (in partition)
- Task scheduler (greedy with frequency)
- Candy distribution (two passes)
- Gas station (circular tour)
- Largest number (custom sort + compare)

### 8. Circular & Specialized Variants
- Circular array loop detection
- Next greater element II (circular array)
- Circular array house robber II
- Circular array maximum sum (Kadane's variant)
- Circular tour (gas station problem)
- Find circular queue front/rear

---

## II. Parallel Pointers (Same Direction)
Pointers move in same direction, often at different speeds.

### A. Read/Write (Slow-Fast) Pointers
#### Array/String Operations
- Remove duplicates from sorted array (keep at most K)
- Remove duplicates from sorted array II (allow at most 2)
- Remove element in-place (val to remove)
- Move zeros to end (maintain relative order)
- Move non-zeros to front
- Remove all occurrences of substring
- Remove vowels from string
- Remove all adjacent duplicates in string
- String compression (count and compress)
- Encode and decode strings (run-length encoding)
- Deduplicate string (remove consecutive duplicates)
- In-place URL encoding (replace spaces with %20)
- Shift elements (rotate array in-place)
- Merge sorted arrays (when first has buffer)
- Reshape the matrix (row-major to row-major)

#### Linked List Operations
- Remove duplicates from sorted list
- Remove duplicates from unsorted list (with hash set)
- Remove linked list elements (with given val)
- Delete node in linked list (given node)
- Partition list (around value x)
- Odd even linked list
- Split linked list in parts
- Remove Nth node from end (two passes)
- Swap nodes in pairs

### B. Fast-Slow Pointer (Relative Speed)
- Detect cycle in linked list
- Find start of cycle in linked list
- Find length of cycle
- Middle of linked list
- Happy number (cycle detection in digit square sum)
- Find duplicate number (array as linked list)
- Linked list palindrome (find middle, reverse second half)
- Reorder linked list (find middle, reverse, merge)
- Circular array loop (with direction constraints)
- Find the celebrity (candidate elimination)

### C. Subsequence Matching
- Is subsequence (check if s is subsequence of t)
- Number of matching subsequences (preprocess)
- Longest word in dictionary through deleting
- Shortest way to form string (from subsequences)
- Maximum length of repeated subarray (DP, but pointer like)
- Minimum window subsequence (not substring)
- String matching with wildcards (simplified)
- Custom sort string (relative ordering)

### D. Linked List Structural Operations
- Intersection of two linked lists (find length difference)
- Add two numbers (linked list representation)
- Merge two sorted lists
- Merge k sorted lists (with heap)
- Sort list (merge sort on linked list)
- Reverse nodes in k-group
- Rotate list to right by k places
- Split list into consecutive parts
- Swapping nodes in linked list (kth from start and end)
- Insert into sorted circular linked list

### E. Separate Progress Trackers
- Merge strings alternately
- Interleave strings
- Add strings (large numbers as strings)
- Multiply strings
- Add binary strings
- Compare version numbers (dot separated)
- Zigzag conversion (multiple rows)

---

## III. Sliding Window (Dynamic Range)
A specialized parallel pointer pattern maintaining a window.

### A. Fixed-Length Window
- Maximum sum subarray of size K
- Maximum average subarray of size K
- Maximum of all subarrays of size K (with deque)
- Minimum sum subarray of size K
- Permutation in string (anagram check)
- Find all anagrams in string
- Count occurrences of anagram
- Grumpy bookstore owner (max satisfied with secret power)
- Maximum points from cards (takes from ends)
- Subarray product less than K (but variable in typical)

### B. Variable-Length Window (Longest)
- Longest substring without repeating characters
- Longest substring with at most K distinct characters
- Longest substring with at most two distinct characters
- Longest repeating character replacement
- Longest binary subarray with at most K zeros
- Longest subarray with sum ≤ K (non-negative array)
- Longest turbulent subarray (up-down pattern)
- Fruit Into Baskets (at most 2 types)
- Maximum consecutive ones III (flip at most K zeros)
- Longest nice substring (divide and conquer variant)
- Longest valid parentheses (stack or DP)

### C. Variable-Length Window (Shortest)
- Minimum window substring
- Minimum size subarray sum (sum ≥ target)
- Shortest subarray with sum at least K (with deque, can be negative)
- Minimum window subsequence
- Minimum operations to reduce X to zero (from ends)
- Shortest distance to target color
- Minimum window containing all characters
- Smallest range covering elements from K lists

### D. Window Counting Problems
- Count subarrays with sum exactly K
- Count subarrays with sum ≤ K
- Number of substrings containing all three characters
- Subarrays with K different integers
- Binary subarrays with sum K
- Count number of nice subarrays (at most K odds)
- Subarray product less than K
- Continuous subarray sum (multiple of K)
- Count subarrays with median K

### E. Multi-Pointer Windows
- Longest substring with at most K distinct (with hash map)
- Minimum window with all characters (with frequency map)
- Substring with concatenation of all words
- Find all anagrams in string (multiple start points)
- Sliding window maximum (with deque)
- Sliding window median (with two heaps)

---

## IV. Partition-Based Pointers
Partition data using pointer boundaries.

### 1. Dutch National Flag & Variants
- Sort colors (0, 1, 2)
- Three-way partition around pivot
- Partition array around given value
- Move all negatives to beginning (order doesn't matter)
- Separate 0s and 1s
- Separate even and odd
- Sort array by parity (even first, odd last)
- Sort array by parity II (even at even indices)
- Wiggle sort (nums[0] < nums[1] > nums[2] < nums[3]...)
- Wiggle sort II (with O(n) time, O(1) space)

### 2. QuickSelect & Partition Algorithms
- Kth largest element in array (QuickSelect)
- Kth smallest element
- Top K frequent elements (bucket sort or QuickSelect)
- Partition array into two with equal sum (subset sum variant)
- Partition labels (string S into max parts with letters only in part)
- Partition array into disjoint intervals
- Array partition I (maximize sum of min of pairs)

### 3. Multi-Way Partition
- First missing positive (cyclic sort approach)
- Find all duplicates in array (mark visited)
- Find all numbers disappeared in array
- Set mismatch (find duplicate and missing)
- First missing positive integer
- Missing number (cyclic sort)
- Find the duplicate number (array as linked list + cycle)
- Find all duplicates in O(1) space

### 4. In-Place Transformations
- Rotate array (using reversal or cyclic replacements)
- Rotate image (transpose + reverse)
- Spiral matrix (four pointers for boundaries)
- Diagonal traversal (multiple directions)
- Game of Life (in-place with state encoding)

---

## V. Interval & Range Pointers
Dealing with intervals or ranges.

### 1. Interval Merging & Operations
- Merge intervals
- Insert interval
- Remove covered intervals
- Interval list intersections
- Non-overlapping intervals (minimum removals)
- Minimum number of intervals to cover point
- Employee free time
- Meeting rooms (can attend all meetings)
- Meeting rooms II (minimum rooms needed)
- Car pooling
- Add bold tag in string (interval merging in string)
- Partition labels (interval of characters)

### 2. Range Comparisons
- Check if intervals overlap
- Find right interval for each interval
- Find minimum arrows to burst balloons
- Video stitching
- Maximum number of events that can be attended
- Remove interval
- Data stream as disjoint intervals
- My calendar I/II/III (booking system)

### 3. Multiple List Interval Operations
- Interval intersection (already mentioned)
- Exclusive time of functions (stack based)
- Range module
- Rectangle overlap/area

---

## VI. Multi-Array/Sequence Pointers
Pointers across different sequences.

### 1. Merge Operations
- Merge two sorted arrays (when first has buffer)
- Merge sorted arrays (standard)
- Merge k sorted arrays/lists
- Merge strings alternately
- Intersection of two arrays (with duplicates)
- Intersection of two arrays II (with counts)
- Union of sorted arrays
- Find common elements in sorted arrays
- Smallest difference pair from two arrays
- Find intersection of two linked lists

### 2. Comparison & Alignment
- Compare version numbers
- Add strings (large numbers)
- Multiply strings
- Add binary
- Add two numbers II (linked lists, reverse or stack)
- Compare strings with backspace
- Implement strStr() (needle in haystack - KMP better)
- Repeated string match

### 3. Multiple Sequence Processing
- Longest common prefix (vertical scanning)
- Longest common subsequence (DP, but pointer thinking)
- Edit distance (DP)
- One edit distance
- Sparse vector dot product (compressed format)
- Word distance (shortest distance between words in list)
- Shortest word distance II/III
- Sentence similarity (word by word)

### 4. Pattern Matching
- Wildcard matching (DP, greedy with pointers)
- Regular expression matching (DP)
- Find and replace pattern
- Custom sort string
- Isomorphic strings
- Word pattern
- Strobogrammatic number (pair mapping)

---

## VII. Multi-Pointer Generalizations (3+ Pointers)

### 1. Monotonic Shrinking Pointers
- 3Sum (i, left, right)
- 4Sum (i, j, left, right)
- 3Sum Closest
- 3Sum Smaller
- Valid triangle number
- Next permutation (find decreasing suffix)
- Array partition into three parts with equal sum
- Partition array into K subsets with equal sum (backtracking)

### 2. Multi-Array K-Pointer Problems
- Merge k sorted lists (with heap of k pointers)
- Kth smallest element in sorted matrix
- Find K pairs with smallest sums (from two arrays)
- Smallest range covering elements from K lists
- 4Sum II (from four arrays, use hash map)
- Minimum window substring (with multiple target chars)

### 3. N-Pointer Scanning
- The "celebrity" problem (knows() API, candidate elimination)
- Majority element II (Boyer-Moore for n/3)
- Sort transformed array (parabola peak finding)
- Maximize palindrome length from subsequences
- String transposition (write in zigzag, read row-wise)

### 4. Simultaneous Multi-Sequence
- Zigzag iterator (alternating between lists)
- Flatten nested list iterator (stack of iterators)
- Peeking iterator
- Design phone directory
- Random pick with weight (prefix sum + binary search)

---

## VIII. Hybrid Patterns & Advanced Applications

### A. Two-Pointer with Hash Map
- Longest substring without repeating (hash map of last seen)
- Minimum window substring (character frequency map)
- Find all anagrams in string (frequency comparison)
- Subarray sum equals K (prefix sum with hash map)
- Maximum size subarray sum equals K
- Contiguous array (equal 0s and 1s, treat 0 as -1)
- Subarray sum divisible by K (remainder tracking)

### B. Two-Pointer with Stack
- Next greater element
- Daily temperatures
- Largest rectangle in histogram (though mono-stack)
- Remove k digits (to make smallest number)
- Validate stack sequences
- Asteroid collision
- Score of parentheses

### C. Two-Pointer with Binary Search
- Find K closest elements (binary search + converging)
- Find peak element (though binary search)
- Search in rotated sorted array
- Find first and last position in sorted array
- Capacity to ship packages within D days
- Split array largest sum
- Koko eating bananas

### D. Two-Pointer with Priority Queue
- Merge k sorted lists
- Find median from data stream (two heaps)
- Sliding window median
- Rearrange string k distance apart
- Task scheduler
- Minimum cost to connect sticks

### E. Cyclic Sort & In-Place Marking
- Find all duplicates in array
- Find all numbers disappeared in array
- First missing positive
- Find the duplicate number
- Set mismatch
- Missing number
- Find the corrupt pair

### F. Matrix/2D Pointer Problems
- Search a 2D matrix (rows and columns)
- Search a 2D matrix II (sorted rows and columns)
- Spiral matrix (four boundary pointers)
- Rotate image (transpose + reverse)
- Set matrix zeroes (mark first row/col)
- Game of Life (in-place with encoding)
- Diagonal traverse
- Toeplitz matrix (compare with top-left neighbor)

### G. Graph & Tree Applications (Pointer-like)
- Binary tree inorder traversal (Morris traversal)
- Binary tree flatten to linked list
- Convert sorted array to BST
- Convert sorted list to BST (find middle)
- Populating next right pointers in each node
- Lowest common ancestor (BST)
- Validate BST (inorder traversal)
- Recover BST (find swapped nodes)

### H. Specialized Applications
- Random pointer linked list copy
- LRU Cache (hash map + doubly linked list)
- LFU Cache
- All O(1) data structure
- Design browser history (doubly linked list)
- Text editor (with cursor - two stacks)
- Stock span problem (mono-stack)
- Online stock span

---

## IX. Problem-Solving Frameworks & Techniques

### When to Use Converging Pointers:
1. Sorted array search problems
2. Symmetry operations (palindromes, reversals)
3. Greedy optimizations with sorted data
4. Water/container problems

### When to Use Parallel Pointers:
1. In-place modifications (remove, filter, compress)
2. Subsequence/subarray checks
3. Linked list operations
4. Merge operations on sorted data

### When to Use Sliding Window:
1. Subarray/substring with constraints
2. Fixed or variable window optimizations
3. Frequency/count problems with contiguous elements

### When to Use Partition Pointers:
1. Dutch flag/color sort problems
2. K-way partitioning
3. QuickSelect/order statistics
4. In-place reordering

### Common Optimizations:
1. Early Termination: Stop when condition met
2. Skip Duplicates: In sorted arrays, skip identical elements
3. Pruning: Eliminate impossible candidates early
4. Memoization: Cache results for overlapping subproblems
5. Preprocessing: Sort, compute prefix sums, build frequency maps

### Complexity Patterns:
- O(n): Single pass with two pointers
- O(n log n): Sort + two pointers
- O(n²): Nested loops with inner two-pointer (like 3Sum)
- O(n^k): K-pointer generalizations

---

## X. Practice Progression

### Beginner:
1. Two Sum (sorted)
2. Reverse string/array
3. Remove duplicates from sorted array
4. Valid palindrome
5. Merge sorted arrays

### Intermediate:
1. Container With Most Water
2. 3Sum
3. Trapping Rain Water
4. Longest substring without repeating
5. Minimum window substring
6. Sort colors
7. Remove Nth node from end

### Advanced:
1. K-way merge
2. Sliding window median
3. Longest valid parentheses
4. Wildcard matching
5. First missing positive
6. Find the celebrity
7. Minimum window subsequence