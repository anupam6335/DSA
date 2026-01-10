# problem Link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 1 : 
# T : O ( n + n )
# S : O (1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # compute length
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        prev = dummy
        # curr = head
        i = 0

        while i < length - n:
            prev = prev.next
            # curr = curr.next
            i += 1

        # prev.next = curr.next
        prev.next = prev.next.next
        return dummy.next

# Approach 2 :  More Optimal
# T : O ( n )
# S : O (1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        curr = head
        for _ in range(n):
            curr = curr.next

        prev = dummy

        while curr:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next
        return dummy.next


# Helper: list -> linked list
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Helper: linked list -> list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# ---- Test ----
sol = Solution()
head = build_linked_list([1, 2, 3, 4, 5])
new_head = sol.removeNthFromEnd(head, 2)
print(linked_list_to_list(new_head))  # [1, 2, 3, 5]

