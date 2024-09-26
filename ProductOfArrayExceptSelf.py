# time complexity = space complexity = O(n)
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    
    # Calculate product of all elements to the left of each element
    left_product = 1
    for i in range(n):
        res[i] *= left_product
        left_product *= nums[i]
    # Calculate product of all elements to the right of each element
    right_product = 1
    for i in range(n-1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i] 
    return res
