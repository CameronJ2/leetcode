from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        largestArea = 0

        while i < j:
            # Calculate the height and width for the current pair of points
            h = min(height[i], height[j])
            w = j - i
            area = h * w

            # Update the largest area if the current area is bigger
            largestArea = max(largestArea, area)

            # Move the pointer that has the smaller height inward
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return largestArea


mySol = Solution()

numbers = [1,8,6,2,5,4,8,3,7]

print(mySol.maxArea(numbers))
        