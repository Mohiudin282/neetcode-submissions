class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for num in tokens:
            if num not in operations:
                stack.append(int(num))
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if num == "+":
                    stack.append(val2 + val1)
                elif num == "-":
                    stack.append(val2 - val1)
                elif num == "*":
                    stack.append(val2 * val1)
                else:
                    stack.append(int(val2/val1))
        return stack[-1]