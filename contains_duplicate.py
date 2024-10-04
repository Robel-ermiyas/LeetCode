# brute force solution 
# O(n^2) time and O(1) space complexity.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False

# However, the above solution isn't efficient for large inputs because it has a quadratic time complexity, which may lead to a time exeeded problem. 
# so, can we do better?
# yes, we can use a sliding window technique to make it more efficient and optimale.
# time complexity = O(n) = linear
# space complexity = O(min(n. k)) = linear

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:  
        num_set = set()
        for i in range(len(nums)):
            if i > k:
                num_set.remove(nums[i - k - 1])
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
        return False
