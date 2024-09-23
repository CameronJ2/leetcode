from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {')': '(', ']': '[', '}': '{'}
        parenStack: List[str] = []
        
        for char in s:
            if char in parenMap.values():
                parenStack.append(char)
            elif char in parenMap:
                if not parenStack or parenStack.pop() != parenMap[char]:
                    return False
            else:
                return False
        
        return len(parenStack) == 0








solution = Solution()

inputString = "]"

print(solution.isValid(inputString))