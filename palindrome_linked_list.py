# time complexity = O(n)
# space complexity = O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
       # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare the two halves
        left, right = head, prev
        while right:  # Only need to check the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True  # If all values matched, it's a palindrome
