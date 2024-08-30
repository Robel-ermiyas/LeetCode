# time complexity = space complexity = O(1) = constant
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

# additional solution
# direct way of solving
# time complexity = space complexity = O(1) = constant 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, node):
      first = node
      second = first.next
      third = second.next
      first.value = second.value
      first.next = third
      second.next = None # optional
      
