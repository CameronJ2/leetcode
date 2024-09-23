from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString: str = ""
        
        for string in strs:
            stringLength: str = str(len(string))
            encodedString = encodedString + stringLength + "#" + string
        
        return encodedString
    
    
    def decode(self, s: str) -> List[str]:
        decodedString: list[str] = []
        length: str = ""
        lengthInt: int = 0
        i: int = 0
        
        while i < len(s):
            debugChar = s[i]
            if (s[i] != "#"):
                length = length + s[i]
                i += 1
                continue
            lengthInt = int(length)
            decodedString.append(s[i + 1: i + lengthInt + 1])
            i = i + lengthInt + 1
            length = ""
        
        return decodedString
            
            
                
            

solution = Solution()

wordList: List[str] = ["neet","code","love","you"]

encodedString = solution.encode(wordList)
print(encodedString)

print("")

decodedString = solution.decode(encodedString)
print(decodedString)