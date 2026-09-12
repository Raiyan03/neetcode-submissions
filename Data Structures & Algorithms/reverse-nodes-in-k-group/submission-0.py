# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        group = 0
        while curr and group != k:
            curr = curr.next
            group += 1
        
        if curr:
            curr = self.reverseKGroup(curr, k)
        if group == k:
            prev = curr
            itr = head
            for i in range(k):
                temp = itr.next
                itr.next = prev
                prev = itr
                itr = temp
            return prev
        return head

                