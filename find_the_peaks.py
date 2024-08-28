# time = space complexity = O(n), where n is the length of the list.
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain) 
        result = []
        if n <=2:
            return result
        for i in range(1, n-1):
            if mountain[i] > mountain[i+1] and mountain[i] > mountain[i-1]:
                result.append(i)
        return result

# additional way
# using list comprehenison
# time = space complexity = O(n), where n is the length of the list.
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [i for i in range(1, len(mountain) - 1) if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]]
