from typing import List

# Come back to this one later, failed to solve it.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        tempList = []
        
        for i in range(len(nums)):
            j: int = len(nums) - 1
            k: int = j - 1
            
            while j != i and j != i + 1:
                while k != i:
                    if nums[i] + nums[k] + nums[j] == 0:
                        tempList.append(nums[i])
                        tempList.append(nums[j])
                        tempList.append(nums[k])
                        tempList.sort()
                        if tempList not in result:
                            result.append(tempList)
                        tempList = []
                    k -= 1
                j -= 1
                k = j - 1
        
        return result
    


mySol = Solution()

nums = [-1,0,1,2,-1,-4]

print(mySol.threeSum(nums)) 