# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head) #dummy node to help for the deletion of the head 

        left = dummy 

        right = head 

        #As long as n > 0 : 

        while n > 0 : 

            right = right.next 

            n-= 1 

        #localise and find the position to delete 

        while right : 

            left = left.next 

            right = right.next 

        left.next = left.next.next 

        return dummy.next 
        