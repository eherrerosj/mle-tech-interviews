"""
Given the head of a linked list, return the list after sorting it in ascending order.
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:
    The number of nodes in the list is in the range [0, 5 * 104].
    -105 <= Node.val <= 105
"""
from typing import List


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        s = []
        current = self
        while current:
            s.append(current.val)
            current = current.next
        return str(s)


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        sol = ListNode()
        sol_ref = sol
        while head:
            sol_ref.val = self.minVal(head)
            print("min: ", sol_ref.val)
            # breakpoint()
            sol_ref.next = ListNode()
            sol_ref = sol_ref.next
            head = head.next

        print("sol", sol)
        return sol

    @staticmethod
    def minVal(head: ListNode) -> ListNode:
        current_min = None
        while head.next:
            if current_min:
                if head.next.val < current_min:
                    current_min = head.next.val
                    if head.next.next:
                        head.next = head.next.next
            else:
                current_min = head.val
            head = head.next
        return current_min


s = ListNode(val=4)
s.next = ListNode(val=2)
s.next.next = ListNode(val=1)
s.next.next.next = ListNode(val=3)
print(s)
sol = Solution().sortList(head=s)
