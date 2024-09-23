class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleIndex: int
        
        for charIndex in range(len(haystack)):
            if haystack[charIndex] != needle[0]:
                continue
            
            needleIndex = charIndex
            haystackIndex = charIndex
            for subIndex in range(len(needle)):
                if (haystackIndex >= len(haystack) or needle[subIndex] != haystack[haystackIndex]):
                    break
                if subIndex == len(needle) - 1:
                    return needleIndex
                
                haystackIndex += 1
        return -1
                

mySol = Solution()
needle = "aaa"
haystack = "aaaa"

print(mySol.strStr(haystack, needle))

