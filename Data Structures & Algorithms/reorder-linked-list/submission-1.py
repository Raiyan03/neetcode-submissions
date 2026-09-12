# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get midpoint
        slow = fast = head
        while fast and fast.next:
            print("Finding mid point ")
            slow = slow.next
            fast = fast.next.next
        prev = None

        #Reversing the second half
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        first, second = head, prev
        while second and second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
