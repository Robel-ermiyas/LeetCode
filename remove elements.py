# time complexity = O(n)
# space compleity = O(1), because the size of k is constant.
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for num in range(len(nums)):
            if nums[num] != val:
                nums[k] = nums[num]
                k += 1
        return k
