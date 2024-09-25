from typing import Dict


class Solution:
    count: int = 0
    def climbStairs(self, n: int, count: int = 0) -> int:
        if (n == 0):
            return count + 1
        if (n < 0):
            return count

        count = self.climbStairs(n - 1, count)
        count = self.climbStairs(n - 2, count)
        
        return count
    
class NeetSolution:
    def climbStairs(self, n: int, count: int = 0) -> int:
        one, two = 1,1
        
        for i in range(n-1):
            temp = one 
            one = one + two
            two = temp
        
        return one
    

class OptimalSolution:
    def climbStairs(self, n: int, memo: None | Dict[int, int]=None) -> int:
        if memo is None:
            memo = {}
        
        # Check if the result is already computed
        if n in memo:
            return memo[n]

        # Base cases
        if n == 0:
            return 1  # One way to stay at the ground
        if n < 0:
            return 0  # No ways to climb if negative

        # Compute the result
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

        return memo[n]
        
        
        
        

mySol: Solution = Solution()
optSol: OptimalSolution = OptimalSolution()
neetSol: NeetSolution = NeetSolution()

# print(mySol.climbStairs(4))
# print(optSol.climbStairs(4))
print(neetSol.climbStairs(4))
