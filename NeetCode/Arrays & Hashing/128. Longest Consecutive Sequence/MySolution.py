from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        collectionSet: set = set()
        
        for number in nums:
            collectionSet.add(number)
            
        longestSeqence: int = 0
        currentSequence: int = 0
        for number in nums:
            currentNumber = number
            while currentNumber in collectionSet:
                currentSequence += 1
                currentNumber += 1
            
            if currentSequence > longestSeqence:
                longestSeqence = currentSequence
            currentSequence = 0
        
        return longestSeqence
    
    
solution = Solution()

nums = [0,3,7,2,5,8,4,6,0,1]

print(solution.longestConsecutive(nums))