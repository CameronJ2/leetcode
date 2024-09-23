class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (2 * t)




mySol = Solution()

num = 3
t = 2

print(mySol.theMaximumAchievableX(num, t))