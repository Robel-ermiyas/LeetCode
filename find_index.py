# By Robel E.
# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Time complexity: O(n * m), where n is the length of the haystack string and m is the length of the needle string. 
# This is because the find() method has a time complexity of O(n * m) in the worst case scenario, where the needle string is not found in the haystack string.
# Space complexity: O(1), as we are not using any additional data structures that scale with the input size.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
