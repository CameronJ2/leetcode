from typing import List

# I actually had the solution right, just fumbled the execution a bit. It's
# important to full think through the process and potential hangups before coding.


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        runningStack = []
        operator = ""
        operand1 = ""
        operand2 = ""
        stringifiedExpression = ""
        result: int
        
        for item in tokens:
            if item not in operands:
                runningStack.append(item)
            else:
                operator = item
                operand2 = runningStack.pop()
                operand1 = runningStack.pop()
                stringifiedExpression = operand1 + operator + operand2
                result = int(eval(stringifiedExpression))
                runningStack.append(str(result))
                
        return int(runningStack.pop())
                
        


mySolution: Solution = Solution()

tokens = ["2","1","+","3","*"]

print(mySolution.evalRPN(tokens))