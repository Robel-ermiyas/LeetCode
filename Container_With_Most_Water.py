# brute force solution.
# O(n^2) time complexity.
# O(1) space complexity

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(1, len(height)):
                area = (j-i)*min(height[i], height[j])
                res = max(res, area )
        return res

# can we do better?
# yes! we can, here is the optimal solution with O(n) time complexity and O(1) space complexity.

class Solution:
  def maxArea(self, height: List[int]) -> int:
      result = 0
      left = 0
      right = len(height)-1
      while left < right:
        area = (right-left) * min(height[left], height[right])
        result = max(result, area)
        if height[left] < height[right]:
          left+=1
        else:
          right-=1
      return result
          
