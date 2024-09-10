# O(n) time complexity
# O(1) space complexity
class Solution:
    def reverse(self, x: int) -> int:
        # Store the sign of x
        sign = -1 if x < 0 else 1
        # Work with the absolute value of x
        x_abs = abs(x)
        reversed_num = 0
        
        # Reverse the digits
        while x_abs != 0:
            reversed_num = reversed_num * 10 + (x_abs % 10)
            x_abs //= 10
        
        # Restore the sign
        reversed_num *= sign
        
        # Check for overflow
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
    
