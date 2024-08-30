# time complexity = O(n)
# space complexity = O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      # creat a dummy node to handle edge cases.
      dummy = ListNode(0)   
        dummy.next = head
        temp = dummy
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next
