# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Algorithm:
        - Floyd Cycle Detection algorithm
        - Use 2 pointers - slow and fast
        """
        if head == None:
            return False
        
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False