class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredString: str = ""
        for char in s:
            if char.isalnum():
                filteredString += char.lower()
        
        if filteredString == "":
            return True
        
        for charIndex in range(len(filteredString)):
            if charIndex >= int(len(filteredString) / 2):
                return True
            if filteredString[charIndex] != filteredString[len(filteredString) - (charIndex + 1)]:
                return False
    
    
mySol = Solution()
test = "a"

print(mySol.isPalindrome(test))