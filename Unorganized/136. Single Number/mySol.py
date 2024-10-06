from typing import List


class BruteForce:
    def singleNumber(self, nums: List[int]) -> int:
        result: List[int] = []
        
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.append(num)
            
        
        return result[0]
    
class Elegant:
    def singleNumber(self, nums: List[int]) -> int:
        result: set[int] = set()
        
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)
            
        
        return result.pop()
    

class Optimal:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR all the numbers
        return result

    

mySol = Elegant()
nums = [4,1,2,1,2]

print(mySol.singleNumber(nums))