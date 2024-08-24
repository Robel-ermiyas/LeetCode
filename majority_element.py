# Boyer-Moore Majority Vote Algorithm:
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# run time complexity = o(n)
# space complesity = o(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0   
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
