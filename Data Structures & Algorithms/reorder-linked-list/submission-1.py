# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Slow and fast pointer 

        slow, fast = head, head.next 

        while fast and fast.next : 

            slow = slow.next 

            fast = fast.next.next 

        #Look for the middle value and then split the list in hamf 

        second = slow.next 

        prev = slow.next = None 

        #Reverse the second half of the list 

        while second : 

            tmp = second.next 

            second.next = prev 

            prev = second 

            second = tmp

        #Reverse one element from the left and another one from the right 

        first, second = head, prev 

        while second : 

            tmp1, tmp2 = first.next, second.next 

            first.next = second 

            second.next = tmp1 

            first, second = tmp1, tmp2
        