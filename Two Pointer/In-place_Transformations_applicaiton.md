Here are LeetCode problems for **in-place transformations using the two-pointer technique**, categorized by their core operation.

### 📝 Problems for In-place Transformations

| Problem Category | LeetCode # & Name | Difficulty | Key Two-Pointer Insight |
| :--- | :--- | :--- | :--- |
| **String & Character Reversal** | **344. Reverse String** | Easy | Use left/right pointers to swap characters until they meet. |
| | **541. Reverse String II** | Easy | Process the string in fixed-size (2k) chunks with pointers. |
| | **557. Reverse Words in a String III** | Easy | Use pointers to find word boundaries and reverse each word in-place. |
| | **151. Reverse Words in a String** | Medium | Reverse entire string, then reverse each word; uses pointers for word bounds. |
| | **917. Reverse Only Letters** | Easy | Pointers skip non-letters and swap only letters. |
| **Array Reversal & Rotation** | **189. Rotate Array** | Medium | Reverse entire array, then reverse first `k` and remaining `n-k` parts. |
| | **186. Reverse Words in a String II** (Premium) | Medium | Reverse the entire character array, then reverse each word. |
| | **396. Rotate Function** | Medium | Mathematical transformation, but in-place calculation uses pointer-like iteration. |
| **In-place Deletion/Deduplication**| **26. Remove Duplicates from Sorted Array** | Easy | Slow pointer holds last unique element, fast pointer finds the next one. |
| | **80. Remove Duplicates from Sorted Array II** | Medium | Extend the above logic, allowing at most two duplicates. |
| | **27. Remove Element** | Easy | One pointer scans, another holds the position for non-target values. |
| **Specialized Swapping & Arrangement**| **283. Move Zeroes** | Easy | One pointer finds non-zero elements to swap with zeros tracked by another. |
| | **905. Sort Array By Parity** | Easy | Pointers from left and right swap odd/even numbers to group them. |
| | **922. Sort Array By Parity II** | Easy | Pointers find mis-placed odd/even elements and swap them. |
| **Advanced In-place Manipulation**| **48. Rotate Image** | Medium | Perform a **transpose** (swap `matrix[i][j]` with `matrix[j][i]`), then reverse each row. |
| | **88. Merge Sorted Array** | Easy | Start filling from the **end** of the first array using three pointers to avoid overwriting. |
| | **75. Sort Colors** (Dutch Flag) | Medium | Use **three pointers** (`low`, `mid`, `high`) to partition 0s, 1s, and 2s in one pass. |

# LeetCode In-place Transformation Problems Using Two-Pointer Technique

## **Easy Problems**

1. **Reverse String** (344) - **Classic Problem**
   - Reverse a string in-place with O(1) extra memory
   ```
   Input: ["h","e","l","l","o"]
   Output: ["o","l","l","e","h"]
   ```

2. **Reverse String II** (541)
   - Reverse first k characters for every 2k characters
   ```
   Input: s = "abcdefg", k = 2
   Output: "bacdfeg"
   ```

3. **Reverse Vowels of a String** (345)
   - Reverse only vowels in a string
   ```
   Input: "hello"
   Output: "holle"
   ```

4. **Reverse Only Letters** (917)
   - Reverse only English letters, leave other characters in place
   ```
   Input: "ab-cd"
   Output: "dc-ba"
   ```

5. **Rotate String** (796)
   - Check if one string is rotation of another
   ```
   Input: s = "abcde", goal = "cdeab"
   Output: true
   ```

6. **Reverse Words in a String III** (557)
   - Reverse each word in a string while preserving whitespace
   ```
   Input: "Let's take LeetCode contest"
   Output: "s'teL ekat edoCteeL tsetnoc"
   ```

## **Medium Problems**

7. **Reverse Words in a String** (151) - **Important Problem** ⭐
   - Reverse the order of words, trim multiple spaces
   ```
   Input: "the sky is blue"
   Output: "blue is sky the"
   ```

8. **Rotate Array** (189) - **Classic Problem** ⭐
   - Rotate array to the right by k steps
   ```
   Input: nums = [1,2,3,4,5,6,7], k = 3
   Output: [5,6,7,1,2,3,4]
   ```

9. **Rotate List** (61)
   - Rotate linked list to the right by k places
   ```
   Input: 1→2→3→4→5→NULL, k = 2
   Output: 4→5→1→2→3→NULL
   ```

10. **Rotate Image** (48) - **Important Problem** ⭐
    - Rotate n×n matrix 90 degrees clockwise in-place
    ```
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
    ```

11. **Spiral Matrix** (54)
    - Return all elements in spiral order (not exactly in-place but uses pointer manipulation)
    ```
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
    ```

12. **Spiral Matrix II** (59)
    - Generate n×n matrix with numbers 1 to n² in spiral order
    ```
    Input: n = 3
    Output: [[1,2,3],[8,9,4],[7,6,5]]
    ```

13. **Reverse Nodes in k-Group** (25) - Hard but important
    - Reverse linked list nodes in groups of k
    ```
    Input: 1→2→3→4→5, k = 2
    Output: 2→1→4→3→5
    ```

14. **Swap Nodes in Pairs** (24)
    - Swap every two adjacent nodes in linked list
    ```
    Input: 1→2→3→4
    Output: 2→1→4→3
    ```

15. **Reverse Linked List II** (92)
    - Reverse portion of linked list from position m to n
    ```
    Input: 1→2→3→4→5→NULL, m = 2, n = 4
    Output: 1→4→3→2→5→NULL
    ```

16. **Reorder List** (143)
    - Reorder L0→L1→...→Ln-1→Ln to L0→Ln→L1→Ln-1→...
    ```
    Input: 1→2→3→4
    Output: 1→4→2→3
    ```

17. **Palindrome Linked List** (234)
    - Check if linked list is palindrome in O(n) time, O(1) space
    ```
    Input: 1→2→2→1
    Output: true
    ```

18. **Reverse Integer** (7)
    - Reverse digits of 32-bit integer
    ```
    Input: 123
    Output: 321
    ```

19. **Transpose Matrix** (867)
    - Transpose matrix (not square case)
    ```
    Input: [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]
    ```

## **Hard Problems**

20. **Text Justification** (68)
    - Arrange words in justified text (in-place pointer manipulation)
    ```
    Input: words = ["This","is","an","example","of","text","justification."], maxWidth = 16
    Output: ["This    is    an","example  of text","justification.  "]
    ```

21. **Integer to English Words** (273)
    - Convert non-negative integer to English words (in-place string building)
    ```
    Input: 1234567
    Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    ```

22. **Reverse Nodes in Even Length Groups** (2074)
    - Reverse nodes in groups of even length
    ```
    Input: 5→2→6→3→9→1→7
    Output: 5→6→2→3→9→1→7
    ```

23. **Reverse Substrings Between Each Pair of Parentheses** (1190)
    - Reverse substrings in each pair of parentheses
    ```
    Input: "(abcd)"
    Output: "dcba"
    ```

## **Patterns & Templates**

**Reverse Array/String:**
```python
def reverse(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

**Reverse Words in String (with trimming spaces):**
```python
def reverseWords(s):
    # Convert to list for in-place modification
    chars = list(s)
    
    # Step 1: Reverse the entire string
    reverse(chars, 0, len(chars)-1)
    
    # Step 2: Reverse each word
    start = 0
    for end in range(len(chars)):
        if chars[end] == ' ':
            reverse(chars, start, end-1)
            start = end + 1
    reverse(chars, start, len(chars)-1)
    
    # Step 3: Clean up extra spaces
    return ''.join(cleanSpaces(chars))
```

**Rotate Array Using Reversal:**
```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    
    # Reverse entire array
    reverse(nums, 0, n-1)
    # Reverse first k elements
    reverse(nums, 0, k-1)
    # Reverse remaining elements
    reverse(nums, k, n-1)
```

**Rotate Image (Matrix):**
```python
def rotate(matrix):
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

## **Practice Problems by Frequency**

**Most Common Interview Questions:**
1. **Rotate Array** (189) - ⭐ Top 50
2. **Reverse Words in a String** (151) - Very Common
3. **Rotate Image** (48) - ⭐ Top 50
4. **Reverse Linked List** (206) - Fundamental
5. **Palindrome Linked List** (234) - Common

**Important Variations:**
6. **Reverse Nodes in k-Group** (25) - Advanced linked list
7. **Reorder List** (143) - Combines multiple techniques
8. **Spiral Matrix** (54) - 2D array traversal

## **Key Insights for In-place Transformations**

1. **Three main reversal techniques:**
   - Two-pointer swap (for arrays/strings)
   - Three-pointer reversal (for linked lists)
   - Recursive reversal (for linked lists)

2. **Rotation patterns:**
   - Array rotation: Reversal algorithm (Juggling algorithm alternative)
   - Matrix rotation: Transpose + Reverse or Layer-by-layer rotation

3. **Space constraints:**
   - True in-place: O(1) extra space (excluding input storage)
   - Often requires modifying input directly

4. **Common patterns:**
   - Reverse entire then reverse parts
   - Find middle then reverse second half
   - Use fast-slow pointers to find middle in linked list

## **Common Mistakes to Avoid**

1. **Off-by-one errors** in reversal boundaries
2. **Not handling k > n** in rotation problems
3. **Forgetting to trim spaces** in string reversal problems
4. **Modifying list while iterating** (in linked list problems)
5. **Not preserving node connections** when reversing linked lists
6. **Edge cases**: empty strings, single element, k = 0 or k = n

## **Problem Progression for Learning**

**Beginner:**
- Reverse String (344)
- Reverse Integer (7)
- Reverse Vowels (345)

**Intermediate:**
- Reverse Words in a String (151) - Must know
- Rotate Array (189) - Must know
- Palindrome Linked List (234)
- Swap Nodes in Pairs (24)

**Advanced:**
- Rotate Image (48) - Must know
- Reverse Nodes in k-Group (25)
- Reorder List (143)
- Spiral Matrix (54)

**Expert:**
- Integer to English Words (273)
- Text Justification (68)

## **Specialized Techniques**

**Linked List Reversal Patterns:**
```python
# Iterative reversal of full list
def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# Reversal between positions m and n
def reverseBetween(head, m, n):
    if not head or m == n:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move prev to position before m
    for _ in range(m-1):
        prev = prev.next
    
    # Reverse from m to n
    curr = prev.next
    for _ in range(n-m):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    
    return dummy.next
```

**Matrix Rotation Techniques:**
1. **Transpose + Reverse rows** (for clockwise 90°)
2. **Reverse rows + Transpose** (for counter-clockwise 90°)
3. **Layer-by-layer rotation** (for any n×n matrix)

**Insight**: In-place transformation problems test your ability to manipulate data structures without extra space. They often combine multiple pointer techniques and require careful attention to boundary conditions. The reversal algorithm is particularly powerful and appears in many different forms across array, string, and linked list problems.

### 🎯 Strategic Practice Guide
Here is how to approach your practice session for efficient learning:

*   **Start with the Fundamentals**: Build intuition by solving **String reversal** (344, 541) and **in-place deletion** (26, 27) problems first. They use the classic fast/slow or opposite-direction pointer patterns.
*   **Understand the Constraint**: The key challenge in these problems is **modifying the data structure without using significant extra space** (often O(1)). Always ask: "Can I swap or overwrite elements instead of creating a new array?"
*   **Recognize the Pattern**: Many in-place transformations are variations of **reversal, partitioning, or merging**. For instance, rotating an array (189) and reversing words in a string (151) use the same reversal subroutine.
*   **Tackle Advanced Problems**: Once comfortable, solve **Sort Colors (75)**. It's a classic interview problem that generalizes the two-pointer approach to **three pointers** for partitioning.

I hope this structured list helps you master in-place transformations. Would you like a similar breakdown for another two-pointer category, such as **Sliding Window** problems?
