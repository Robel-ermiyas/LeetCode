# Example 1:
# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# time complexity = O(nlogn)
#space complexity = O(n)
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if nums != sorted(nums):
            nums.sort()
        list = []
        for i in range(len(nums)):
            if nums[i] == target:
                list.append(i)
        return list
