# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newList = []
        node = ListNode(0)
        for i in lists:
            itr = i
            while itr:
                newList.append(itr.val)
                itr = itr.next
        newList.sort()
        
        itr = node
        for i in newList:
            itr.next = ListNode(i)
            itr = itr.next
        return node.next