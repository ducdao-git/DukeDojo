class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "-", "*", "/"}
        num_stack = []

        for t in tokens:
            if t not in operators:
                num_stack.append(int(t))
                continue

            # pop right term, then left term => need reverse order
            n2, n1 = num_stack.pop(), num_stack.pop()

            if t == "+":
                num_stack.append(n1 + n2)
            elif t == "-":
                num_stack.append(n1 - n2)
            elif t == "*":
                num_stack.append(n1 * n2)
            elif t == "/":
                num_stack.append(int(n1 / n2))

        return num_stack[-1]


## Question URL: https://neetcode.io/problems/evaluate-reverse-polish-notation/question?list=neetcode150
# - if get a num => add to num stack
# - if get an operator => consume the last 2 nums
sol_test = Solution()
print(sol_test.evalRPN(tokens=["1", "2", "+", "3", "*", "4", "-"]))
