from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        j: int = 0
        i: int = 0
        while m != 0 and i < len(nums1):
            while j < n:
                if nums2[j] <= nums1[i]:
                    nums1.insert(i, nums2[j])
                    i += 1
                    j += 1
                    continue
                break
            i += 1
        test = len(nums1)
        while j < n:
            nums1.insert(len(nums1), nums2[j])
            j+= 1
        
        
            
            
            

mySol: Solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

mySol.merge(nums1, m, nums2, n)
