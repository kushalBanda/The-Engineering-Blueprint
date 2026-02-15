class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)

        if len(ransomNote) > len(magazine):
            return False

        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True

solution = Solution()
print(solution.canConstruct("aa", "aab"))