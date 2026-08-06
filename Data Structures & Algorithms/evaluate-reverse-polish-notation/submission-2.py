class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if tok == "+":
                    stack.append(val2 + val1)
                elif tok == "-":
                    stack.append(val2 - val1)
                elif tok == "*":
                    stack.append(val2 * val1)
                else:
                    stack.append(int(val2 / val1))

        return stack[-1]