class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        listStr = s.split()
        return (len(listStr[-1]))

solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))