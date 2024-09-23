from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        for i in range(len(nums)):
            # if (i == 0):
            #     complementMap[nums[i]] = i
            complement = target - nums[i]
            if (complement in complementMap):
                return ([complementMap.get(complement), i])
            complementMap[nums[i]] = i
        return [0,0]
    
    
    
solution = Solution()

print(solution.twoSum([4,5,6], 10))