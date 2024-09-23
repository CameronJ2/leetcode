from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix: str = ""
        numWords: int = len(strs)
        smallestWord:int = 99999
        currentLetter:str
        for word in strs:
            if len(word) < smallestWord:
                smallestWord = len(word)
        for letterIndex in range(smallestWord):
            for wordIndex in range(numWords):
                if wordIndex == 0 :
                    currentLetter = strs[wordIndex][letterIndex]
                    continue
                if strs[wordIndex][letterIndex] != currentLetter:
                    return prefix
            
            prefix += currentLetter
        return prefix


mySolution = Solution

myList = ["Hello", "Hethis", "Heis", "Henot", "HetheEnd"]

print(mySolution.longestCommonPrefix(mySolution, myList))