# Time Complexity:
# push(): O(1)
# pop(): O(1)
# top(): O(1)
# getMin(): O(1)
# Space Complexity: O(n)

class MinStack:
    def __init__(self):
        """
        Initializes the stack object.
        """
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to store minimum elements

    def push(self, val: int) -> None:
        """
        Pushes the element val onto the stack.
        """
        self.stack.append(val)
        # If the min_stack is empty or the current element is smaller than the top of min_stack, push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        if self.stack:
            # If the top element of the stack is equal to the top of min_stack, pop it from min_stack as well
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        """
        Gets the top element of the stack.
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None
