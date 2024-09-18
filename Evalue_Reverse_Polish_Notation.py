time = space complexity = 0(n)
# efficient way
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)  # Note: truncates towards zero
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()  # Get the second operand
                a = stack.pop()  # Get the first operand
                result = operators[token](a, b)  # Perform the operation
                stack.append(result)  # Push the result back onto the stack
            else:
                stack.append(int(token))  # Push numbers onto the stack

        return stack[0]  # The final result


# way two
class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            elif token in ('+', '-', '*', '/'):
                if len(stack) >=2:
                    b = stack.pop()
                    a = stack.pop()
                    if token == '+':
                        result = a+b
                    elif token == '-':
                        result = a-b
                    elif token == '*':
                        result = a*b
                    else:
                        result = int(a/b)
                    stack.append(result)
        return stack[0] if stack else 0
        
