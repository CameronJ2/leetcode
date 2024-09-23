from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapList = []
        groupedWords = []
        groupedMaps = []
        flag = False
        for i in range(len(strs)):
            mapList.append({})
            for letter in strs[i]:
                if letter not in mapList[i]:
                    mapList[i][letter] = 1
                    continue
                mapList[i][letter] = mapList[i][letter] + 1
                
        for i in range(len(strs)):
            word = strs[i]
            map = mapList[i]
            if i == 0:
                groupedWords.append([word])
                groupedMaps.append([map])
                continue
            for listIndex in range(len(groupedMaps)):
                if mapList[i] in groupedMaps[listIndex]:
                    groupedWords[listIndex].append(word)
                    # groupedMaps[listIndex].append(map)
                    flag = True
                    break
            if not flag:   
                groupedWords.append([word])
                groupedMaps.append([map])
            flag = False
        return groupedWords
                
            
            
            
                
        
        
solution = Solution()

print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))