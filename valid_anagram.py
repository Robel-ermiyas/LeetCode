# time complexity = O(n)
# space complexity = O(k) where k is the number of unique characters in the strings (which can be at most 26 for lowercase English letters).
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths are equal
        if len(s) != len(t):
            return False
        
        # Count the frequency of each character in both strings
        count_s = Counter(s)
        count_t = Counter(t)image.png
        
        # Compare the two frequency counts
        return count_s == count_t
