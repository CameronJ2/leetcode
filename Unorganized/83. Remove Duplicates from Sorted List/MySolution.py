#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp: ListNode = head
     
        while temp != None and temp.next != None:
            if temp.next.val == temp.val:
                temp.next = temp.next.next
                continue
            temp = temp.next
        return head
             

             