# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or head.next is None:
            return True 
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        prev = None 
        curr = slow 
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        h1 = head 
        h2 = prev
        while h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        return True