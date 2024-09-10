# Space and Time Complexity Analysis
# Time Complexity: The time complexity of this function is O(n) because it iterates through all numbers from 1 to n once.
# Space Complexity: The space complexity is also O(n) since we are storing the results in a list that grows linearly with n.
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        my_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                my_list.append("FizzBuzz")
            elif i % 3 == 0:
                my_list.append("Fizz")
            elif i % 5 == 0:
                my_list.append("Buzz")
            else:
                my_list.append(str(i))
        return my_list;  
