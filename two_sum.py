# By Robel E.
#concise way
#run time complexity = O(n) b/s it have only one loop.
#space complexity = O(n) b/s of the the dictionary
class Solution(object):
    def twoSum(self, nums, target):
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        storage = {}
        for i in range(len(nums)):
            if target - nums[i] in storage:
                return ([storage[target-nums[i]], i])
            else:
                storage[nums[i]] = i
# brutal force
# run time complexity = O(n^2)
# space complexity = O(1) constant
class Solution(object):
    def twoSum(self, nums, target):
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
       for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return ([i, j])
