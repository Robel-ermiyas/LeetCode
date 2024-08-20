# By Robel E. 
# Time complexity: O(n) for both best and worst case 
# Worst case: when all digits are 9.
# Space complexity: O(1) constatnt
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    # Iterate from the rightmost digit
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
    # If all digits are 9, add a new digit 1 at the beginning
        return [1] + digits
