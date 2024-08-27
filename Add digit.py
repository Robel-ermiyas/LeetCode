# Given an integer `nums`, repeatedly adds all its digits until the result has only one digit, and returns it.
# time complexity = O(log(n))
# space complexity = O(1)
class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num

# more efficient implementation
# time complexity = O(1)
# space complexity = 0(1)
class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
