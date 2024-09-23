from typing import List



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array first
        nums.sort()
        result = []
        
        # Iterate through the array
        for i in range(len(nums)):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate elements for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move the pointers after handling duplicates
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum
    
        return result
    


mySol = Solution()

nums = [-1,0,1,2,-1,-4]

print(mySol.threeSum(nums)) 