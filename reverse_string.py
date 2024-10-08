# Summary
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left<right:
            s[left], s[right] = s[right], s[left]
            left = left+1
            right = right-1
