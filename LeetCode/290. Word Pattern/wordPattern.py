class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = {}
        pattern = list(pattern)
        s = list(s.split())

        if len(pattern) != len(s):
            return False

        for idx, p in enumerate(pattern):
            if p not in hashMap:
                if s[idx] in hashMap.values():
                    return False
                hashMap[p] = s[idx]
            elif s[idx] != hashMap[p]:
                return False
        return True

solution = Solution()
print(solution.wordPattern("aaa", "aa aa aa aa"))