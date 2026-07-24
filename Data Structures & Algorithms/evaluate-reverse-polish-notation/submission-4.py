class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                var2 = stack.pop()
                var1 = stack.pop()
                if i == '+':
                    result = var1 + var2
                    stack.append(result)
                if i == '-':
                    result = var1 - var2
                    stack.append(result)
                if i == '*':
                    result = var1 * var2
                    stack.append(result)
                if i == '/':
                    result = int(var1 / var2)
                    stack.append(result)
        return stack[0]