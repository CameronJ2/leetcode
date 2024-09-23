'''
I had the brute force method of this solution down, but I didn't figure out the trick of
only moving the pointer with LESS HEIGHT in. I instead, did a nested o(n^2) loop. I had
some quality optimizations by checking the height with its previous height, but the optimal
solution is still o(n), so it'll always be faster.
'''



from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        h: int
        w: int
        area: int
        largestArea: int = 0
        prevIHeight = 0
        prevJHeight = 0
        
        for i in range(len(height)):
            j = len(height) - 1
            while j != i:
                if (height[i] < prevIHeight or height[j] < prevJHeight):
                    j -= 1
                    continue
                h = min(height[i], height[j])
                w = j - i
                area = int(h * w)
                
                if area > largestArea:
                    largestArea = area
                    prevIHeight = height[i]
                    prevJHeight = height[j]
                j -= 1
        
        return largestArea


mySol = Solution()

numbers = [1,8,6,2,5,4,8,3,7]

print(mySol.maxArea(numbers))
        