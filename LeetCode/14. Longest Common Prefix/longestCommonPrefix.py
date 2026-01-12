from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sortedList = sorted(strs, key = len)
        shortest = sortedList[0]

        for i in range(len(shortest)):
            for s in sortedList[1:]:
                if s[i] != shortest[i]:
                    return shortest[:i]
        return shortest

solution = Solution()
print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix(["flower","flow","flight"]))