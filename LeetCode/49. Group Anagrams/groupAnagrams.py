from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in hashMap:
                hashMap[sorted_str] = [str]
            else:
                hashMap[sorted_str].append(str)
        return list(hashMap.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))